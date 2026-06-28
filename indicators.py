import ta


FEATURE_COLUMNS = [
    "rsi",
    "macd",
    "macd_signal",
    "sma20",
    "sma50",
    "ema20",
    "volume",
    "daily_return"
]


def add_indicators(df):

    df["rsi"] = ta.momentum.RSIIndicator(
        close=df["close"],
        window=14
    ).rsi()

    macd = ta.trend.MACD(df["close"])

    df["macd"] = macd.macd()

    df["macd_signal"] = macd.macd_signal()

    df["sma20"] = ta.trend.SMAIndicator(
        close=df["close"],
        window=20
    ).sma_indicator()

    df["sma50"] = ta.trend.SMAIndicator(
        close=df["close"],
        window=50
    ).sma_indicator()

    df["ema20"] = ta.trend.EMAIndicator(
        close=df["close"],
        window=20
    ).ema_indicator()

    df["daily_return"] = df["close"].pct_change()

    df = df.dropna().reset_index(drop=True)

    return df