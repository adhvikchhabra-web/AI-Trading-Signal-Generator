import pandas as pd


def run_backtest(df):

    strategy_returns = []

    market_returns = []

    for i in range(1, len(df)):

        market_return = (
            df["close"].iloc[i] -
            df["close"].iloc[i - 1]
        ) / df["close"].iloc[i - 1]

        market_returns.append(market_return)

        signal = df["prediction"].iloc[i - 1]

        if signal == 1:

            strategy_returns.append(market_return)

        elif signal == -1:

            strategy_returns.append(-market_return)

        else:

            strategy_returns.append(0)

    result = pd.DataFrame()

    result["strategy"] = strategy_returns

    result["market"] = market_returns

    result["strategy_equity"] = (
        1 + result["strategy"]
    ).cumprod()

    result["market_equity"] = (
        1 + result["market"]
    ).cumprod()

    return result


def compute_metrics(bt):

    strategy = bt["strategy_equity"].iloc[-1]

    market = bt["market_equity"].iloc[-1]

    return {
        "strategy_return": (strategy - 1) * 100,
        "market_return": (market - 1) * 100
    }