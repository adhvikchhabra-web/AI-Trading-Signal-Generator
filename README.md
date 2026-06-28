# 📈 AI Trading Signal Generator

An AI-powered stock trading signal generator that predicts **BUY**, **HOLD**, and **SELL** signals using Machine Learning and technical analysis indicators. The project includes a trained Random Forest model, interactive visualizations, and a Streamlit dashboard for analyzing stock trends.

---

## 🚀 Features

- 📊 Historical stock price analysis
- 🤖 Machine Learning-based Buy/Hold/Sell prediction
- 📈 Technical indicators:
  - RSI (Relative Strength Index)
  - MACD (Moving Average Convergence Divergence)
  - SMA (Simple Moving Average)
  - EMA (Exponential Moving Average)
- 🌲 Random Forest Classifier
- 📉 Interactive stock price visualization
- 🎯 Real-time prediction dashboard using Streamlit
- 💾 Model training and saving using Joblib

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Plotly
- TA (Technical Analysis Library)
- Joblib

---

## 📂 Project Structure

```
AI-Trading-Signal-Generator/
│
├── data/
│   └── AAPL.csv
│
├── models/
│   ├── model.pkl
│   └── scaler.pkl
│
├── app.py
├── train.py
├── trainer.py
├── indicators.py
├── labeler.py
├── backtester.py
├── charts.py
├── data_loader.py
├── config.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/adhvikchhabra-web/AI-Trading-Signal-Generator.git

cd AI-Trading-Signal-Generator
```

Install dependencies

```bash
pip install -r requirements.txt
```

Train the model

```bash
python train.py
```

Launch the dashboard

```bash
streamlit run app.py
```

---

## 📊 Dashboard

The dashboard displays:

- Current Stock Price
- RSI Value
- AI Prediction (BUY / HOLD / SELL)
- Interactive Stock Price Chart

---

## 🤖 Machine Learning Pipeline

1. Load historical stock data
2. Compute technical indicators
3. Generate trading labels
4. Train a Random Forest classifier
5. Evaluate model performance
6. Save trained model
7. Predict future trading signals
8. Visualize results in Streamlit

---

## 📈 Model Performance

Current model:

- Algorithm: **Random Forest Classifier**
- Classification: **BUY / HOLD / SELL**
- Accuracy: **~25%**

> This project is intended as an educational demonstration of applying machine learning to financial time-series data. It should not be used as financial or investment advice.

---

## 🔮 Future Improvements

- Support for multiple stocks
- Live Yahoo Finance API integration
- LSTM / XGBoost models
- Portfolio backtesting
- Feature importance visualization
- Trading performance metrics
- Risk management dashboard
- Model hyperparameter tuning

---

## 📸 Screenshots



<img width="1470" height="612" alt="Screenshot 2026-06-28 at 10 11 24 PM" src="https://github.com/user-attachments/assets/02b2d19a-7c94-4d41-8c91-61a723dce104" />

<img width="1470" height="557" alt="Screenshot 2026-06-28 at 10 11 32 PM" src="https://github.com/user-attachments/assets/b62b5e02-4ec9-486b-943a-d5831c91f4a1" />

<img width="100%" src="images/dashboard.png">
---

## 👨‍💻 Author

**Adhvik Chhabra**

GitHub: https://github.com/adhvikchhabra-web

LinkedIn: *(Add your LinkedIn profile here)*

---

## ⭐ If you found this project useful, consider giving it a star!<img width="1470" height="835" alt="Screenshot 2026-06-28 at 10 11 01 PM" src="https://github.com/user-attachments/assets/e6b9bf18-81ee-42dd-8612-c7e9201fb57f" />
