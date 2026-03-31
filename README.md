# 📊 Stock & Crypto Risk Dashboard

An interactive financial dashboard that analyzes stocks and cryptocurrencies to evaluate risk and performance using real-time market data.

---

## 🚀 Overview

This project allows users to input a stock or crypto ticker (e.g., AAPL, ETH-USD, BTC-USD) and instantly view:

- Risk classification (Low / Medium / High)
- Annualized volatility
- Price trends with moving averages (MA50, MA200)

The goal is to provide quick insights into asset behavior using simple financial metrics.

---

## ⚙️ Features

- 📈 Real-time data using Yahoo Finance API
- 📊 Volatility-based risk classification
- 📉 Moving averages (MA50, MA200)
- 📍 Interactive visualization using Streamlit

---

## 🧠 How It Works

1. Fetches 1-year historical data
2. Calculates daily returns
3. Computes annualized volatility
4. Classifies risk based on volatility
5. Plots price trends with moving averages

---

## 🛠️ Tech Stack

- Python
- Streamlit
- yFinance
- NumPy
- Matplotlib

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
