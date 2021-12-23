import matplotlib.pyplot as plt

import warnings


def chart_macd(df):
    fig, axes = plt.subplots(2, 1, figsize=(10, 10))
    fig.tight_layout()
    plt.suptitle("GOOG", fontsize=24)
    plt.subplots_adjust(left=0.1, top=0.9, hspace=0.4)
    ax1 = axes[0]
    ax1.set_title("Price")
    ax1.set_ylabel("$")
    df.tail(300)[["date", "close"]].plot(x="date", kind="line", ax=ax1)
    ax2 = axes[1]
    ax2.set_title("MACD")
    df.tail(300)[["date", "macd_line", "macd_9_day"]].plot(
        x="date", kind="line", ax=ax2, secondary_y=False)
    fig.savefig("feature_charts/macd.png")


def chart_ma(df):
    fig, axes = plt.subplots(1, 1, figsize=(10, 10))
    fig.tight_layout()
    plt.suptitle("GOOG Moving Average 50 day - 200 day", fontsize=24)
    plt.subplots_adjust(left=0.1, top=0.9, right=0.9, hspace=0.4)
    axes.set_ylabel("$")
    df.tail(1500)[["date", "close"]].plot(
        x="date", kind="line", ax=axes, secondary_y=False)
    df.tail(1500)[["date", "ma_50_day"]].plot(
        x="date", kind="line", ax=axes, secondary_y=False)
    df.tail(1500)[["date", "ma_200_day"]].plot(
        x="date", kind="line", ax=axes, secondary_y=False)
    df.tail(1500)[["date", "ma_50_200"]].plot(
        x="date", kind="line", ax=axes, secondary_y=True)
    fig.savefig("feature_charts/ma.png")


def chart_sar(df):
    fig, axes = plt.subplots(1, 1, figsize=(10, 10))
    fig.tight_layout()
    plt.suptitle("GOOG SAR", fontsize=24)
    plt.subplots_adjust(left=0.1, top=0.9, right=0.9, hspace=0.4)
    axes.set_ylabel("$")
    df.tail(100)[["date", "close"]].plot(
        x="date", kind="line", ax=axes, secondary_y=False)
    df.tail(100)[["date", "sar"]].plot(
        x="date", style=".", ax=axes, secondary_y=False)
    fig.savefig("feature_charts/sar.png")


def chart_stochastic_oscillator(df):
    fig, axes = plt.subplots(1, 1, figsize=(10, 10))
    fig.tight_layout()
    plt.suptitle("GOOG Stochastic Oscillator", fontsize=24)
    plt.subplots_adjust(left=0.1, top=0.9, right=0.9, hspace=0.4)
    df.tail(100)[["date", "close"]].plot(
        x="date", kind="line", ax=axes, secondary_y=False)
    df.tail(100)[["date", "stochastic_oscillator"]].plot(
        x="date", kind="line", ax=axes, secondary_y=True)
    fig.savefig("feature_charts/stochastic_oscillator.png")


def chart_commodity_channel_index(df):
    fig, axes = plt.subplots(1, 1, figsize=(10, 10))
    fig.tight_layout()
    plt.suptitle("GOOG Commodity Channel Index (CCI)", fontsize=24)
    plt.subplots_adjust(left=0.1, top=0.9, right=0.9, hspace=0.4)
    df.tail(300)[["date", "close"]].plot(
        x="date", kind="line", ax=axes, secondary_y=False)
    df.tail(300)[["date", "cci"]].plot(
        x="date", kind="line", ax=axes, secondary_y=True)
    fig.savefig("feature_charts/commodity_channel_index.png")


def chart_rsi(df):
    fig, axes = plt.subplots(1, 1, figsize=(10, 10))
    fig.tight_layout()
    plt.suptitle("GOOG Relative Strength Index (RSI)", fontsize=24)
    plt.subplots_adjust(left=0.1, top=0.9, right=0.9, hspace=0.4)
    df.tail(100)[["date", "close"]].plot(
        x="date", kind="line", ax=axes, secondary_y=False)
    df.tail(100)[["date", "rsi"]].plot(
        x="date", kind="line", ax=axes, secondary_y=True)
    fig.savefig("feature_charts/rsi.png")


def chart_bollinger(df):
    fig, axes = plt.subplots(1, 1, figsize=(10, 10))
    fig.tight_layout()
    plt.suptitle("GOOG Bollinger Bands", fontsize=24)
    plt.subplots_adjust(left=0.1, top=0.9, right=0.9, hspace=0.4)
    df.tail(100)[["date", "close"]].plot(
        x="date", kind="line", ax=axes, secondary_y=False)
    df.tail(100)[["date", "bollinger"]].plot(
        x="date", kind="line", ax=axes, secondary_y=True)
    fig.savefig("feature_charts/bollinger.png")


def chart_average_true_range(df):
    fig, axes = plt.subplots(1, 1, figsize=(10, 10))
    fig.tight_layout()
    plt.suptitle("GOOG Average True Range (ATR)", fontsize=24)
    plt.subplots_adjust(left=0.1, top=0.9, right=0.9, hspace=0.4)
    df.tail(100)[["date", "close"]].plot(
        x="date", kind="line", ax=axes, secondary_y=False)
    df.tail(100)[["date", "atr"]].plot(
        x="date", kind="line", ax=axes, secondary_y=True)
    fig.savefig("feature_charts/average_true_range.png")


def chart_on_balance_volume(df):
    fig, axes = plt.subplots(1, 1, figsize=(10, 10))
    fig.tight_layout()
    plt.suptitle("GOOG On Balance Volume (OBV)", fontsize=24)
    plt.subplots_adjust(left=0.1, top=0.9, right=0.9, hspace=0.4)
    df.tail(100)[["date", "close"]].plot(
        x="date", kind="line", ax=axes, secondary_y=False)
    df.tail(100)[["date", "on_balance_volume"]].plot(
        x="date", kind="line", ax=axes, secondary_y=True)
    fig.savefig("feature_charts/on_balance_volume.png")


def chart_chaikin_oscillator(df):
    fig, axes = plt.subplots(1, 1, figsize=(10, 10))
    fig.tight_layout()
    plt.suptitle("GOOG Chaikin Oscillator", fontsize=24)
    plt.subplots_adjust(left=0.1, top=0.9, right=0.9, hspace=0.4)
    df.tail(100)[["date", "close"]].plot(
        x="date", kind="line", ax=axes, secondary_y=False)
    df.tail(100)[["date", "chaikin_oscillator"]].plot(
        x="date", kind="line", ax=axes, secondary_y=True)
    fig.savefig("feature_charts/chaikin_oscillator.png")
