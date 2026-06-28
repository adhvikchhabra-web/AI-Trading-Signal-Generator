import streamlit as st

from config import DATA_FILE

from data_loader import load_stock_data

from indicators import add_indicators

from trainer import predict_signals

from backtester import (
    run_backtest,
    compute_metrics
)

from charts import (
    price_chart,
    equity_chart
)

st.set_page_config(
    page_title="AI Trading Signal Generator",
    layout="wide"
)

st.title("📈 AI Trading Signal Generator")

df = load_stock_data(DATA_FILE)

df = add_indicators(df)

df = predict_signals(df)

st.subheader("Latest Signals")

signal_map = {
    -1: "SELL",
    0: "HOLD",
    1: "BUY"
}

latest = df.iloc[-1]

col1, col2, col3 = st.columns(3)

col1.metric("Current Price", f"${latest['close']:.2f}")

col2.metric("RSI", f"{latest['rsi']:.2f}")

col3.metric("Prediction", signal_map[latest["prediction"]])

st.plotly_chart(price_chart(df), use_container_width=True)

bt = run_backtest(df)

metrics = compute_metrics(bt)

st.subheader("Backtest")

c1, c2 = st.columns(2)

c1.metric(
    "Strategy Return",
    f"{metrics['strategy_return']:.2f}%"
)

c2.metric(
    "Buy & Hold",
    f"{metrics['market_return']:.2f}%"
)

st.plotly_chart(
    equity_chart(bt),
    use_container_width=True
)

st.subheader("Latest Data")

st.dataframe(df.tail(20))