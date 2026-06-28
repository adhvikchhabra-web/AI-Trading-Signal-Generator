import pandas as pd


def load_stock_data(filepath):

    df = pd.read_csv(filepath)

    df.columns = [c.lower() for c in df.columns]

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])

    df = df.sort_values("date")

    df.reset_index(drop=True, inplace=True)

    return df