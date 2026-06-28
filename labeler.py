import pandas as pd
from config import LOOKAHEAD


def create_labels(df):

    future_price = df["close"].shift(-LOOKAHEAD)

    pct_change = (future_price - df["close"]) / df["close"]

    labels = []

    for change in pct_change:
        if pd.isna(change):
            labels.append(None)
        elif change > 0.02:
            labels.append(1)      # BUY
        elif change < -0.02:
            labels.append(-1)     # SELL
        else:
            labels.append(0)      # HOLD

    df["signal"] = labels

    df = df.dropna().reset_index(drop=True)

    return df


def label_distribution(df):

    mapping = {-1: "SELL", 0: "HOLD", 1: "BUY"}

    counts = df["signal"].map(mapping).value_counts()

    return counts.to_dict()