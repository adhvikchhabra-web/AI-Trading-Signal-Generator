import plotly.graph_objects as go


def price_chart(df):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["date"],
            y=df["close"],
            name="Close Price"
        )
    )

    fig.update_layout(
        title="Stock Price",
        xaxis_title="Date",
        yaxis_title="Price"
    )

    return fig


def equity_chart(bt):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            y=bt["strategy_equity"],
            name="Strategy"
        )
    )

    fig.add_trace(
        go.Scatter(
            y=bt["market_equity"],
            name="Buy & Hold"
        )
    )

    fig.update_layout(
        title="Backtest"
    )

    return fig