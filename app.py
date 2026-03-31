import streamlit as st
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Risk Dashboard", layout="centered")

st.title("Stock / Crypto Risk Dashboard")
st.write("Enter a ticker like AAPL, ETH-USD, or BTC-USD, then click Analyze.")

ticker = st.text_input("Enter Ticker", "ETH-USD")

if st.button("Analyze"):
    data = yf.download(ticker, period="1y")

    if data.empty:
        st.error("Invalid ticker or no data found.")
    else:
        data["Returns"] = data["Close"].pct_change()
        data["MA50"] = data["Close"].rolling(50).mean()
        data["MA200"] = data["Close"].rolling(200).mean()

        volatility = data["Returns"].std() * np.sqrt(252)

        if volatility < 0.20:
            risk = "Low Risk"
        elif volatility < 0.50:
            risk = "Medium Risk"
        else:
            risk = "High Risk"

        st.subheader("Results")
        st.write(f"Ticker: {ticker}")
        st.write(f"Risk Level: {risk}")
        st.write(f"Annualized Volatility: {volatility:.4f}")

        fig, ax = plt.subplots()
        ax.plot(data.index, data["Close"], label="Close Price")
        ax.plot(data.index, data["MA50"], label="MA50")
        ax.plot(data.index, data["MA200"], label="MA200")
        ax.set_title(f"{ticker} Price Chart")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        ax.legend()
        st.pyplot(fig)
