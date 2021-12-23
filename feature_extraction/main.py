from textwrap import indent
import pandas as pd
import numpy as np
import feature_generation as gen_features

def preprocessing():
    # print("\n OPTIONS:\n 1. MSFT \n 2. GOOG \n Please enter a company index 1 or 2: \n")
    # company_name = str(input())
    filename = "GOOG.csv"
    df = csv_to_df(filename)
    print(df.head())
    df = gen_features.return_features(df)
    # Generation of target values
    df = gen_features.target_value(df)
    # DATA CLEANING
    df = clean_df(df)
    # Generation of technical Indicators
    df = gen_technical_indicator_features(df)
    # Extracting the useful features
    X, y = get_useful_features(df)
    X = X.values
    y = y.values
    df_to_csv(df = pd.DataFrame(X),
                filename="./features_csv/GOOG_features.csv")
    df_to_csv(df = pd.DataFrame(y),
                filename="./features_csv/GOOG_target_values.csv")


def csv_to_df(filename):
    df = pd.read_csv(filename, header=0)
    df.drop(labels="Close", axis=1, inplace=True)
    df.columns = ["date", "open", "high", "low", "close", "volume"]
    df["date"] = pd.to_datetime(df["date"])
    return df

def df_to_csv(df, filename):
    df.to_csv(filename, index=False)

# generation of following technical indicators:
# 1. trend_features
# 2. momentum_features
# 3. volatility_features
# 4. volume_features
def gen_technical_indicator_features(df):
    df = gen_features.trend_features(df)
    df = gen_features.momentum_features(df)
    df = gen_features.volatility_features(df)
    df = gen_features.volume_features(df)
    return df

def get_useful_features(df):
    X = df.loc[200:len(df)-1, ["return", "close_to_open", "close_to_high", "close_to_low",
                               "macd_diff", "ma_50_200", "sar", "stochastic_oscillator",
                               "cci", "rsi", "5d_volatility", "21d_volatility", "60d_volatility",
                               "bollinger", "atr", "on_balance_volume", "chaikin_oscillator"]]
    y = df.loc[200:len(df)-1, ["y"]]
    return X, y

# cleaning dataframe
def clean_df(df):
    df = missing_values(df)
    df = outliers(df)
    return df

def missing_values(df):
    missing_values_count = df.isnull().sum()
    if sum(missing_values_count) == 0:
        return df
    else:
        print("Ffill of missing values necessary")
        df = df.fillna(method="ffill", axis=0).fillna("0")
        missing_values_count = df.isnull().sum()    
        assert sum(missing_values_count) == 0
        return df

def outliers(df):
    df_outliers = df.loc[:, ["date", "return",
                             "close_to_open", "close_to_high", "close_to_low"]]
    column_to_analysts = "return"
    df_smallest = df_outliers.sort_values(
        by=column_to_analysts, ascending=True)
    df_largest = df_outliers.sort_values(
        by=column_to_analysts, ascending=False)
    return df    

if __name__ == "__main__":
    preprocessing()