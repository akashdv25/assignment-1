import streamlit as st
import yfinance as yf
import pandas as pd
from src import calculate_portfolio_performance


def main():
    st.title("📈 Interactive Stock Portfolio Tracker")
    
    # User input for stock transactions
    st.header("Enter Stock Transactions")
    symbol = st.text_input("Stock Symbol")
    shares = st.number_input("Number of Shares", min_value=0)
    price = st.number_input("Purchase Price", min_value=0.0)
    
    if st.button("Add Transaction"):
        # Add transaction to portfolio
        transaction = {'symbol': symbol, 'shares': shares, 'price': price}
        st.session_state.transactions.append(transaction)
    
    # Display portfolio performance
    st.header("Portfolio Performance")
    total_value = calculate_portfolio_performance(*st.session_state.transactions)
    st.write(f"Total Portfolio Value: ${total_value:.2f}")
    
    # Fetch and display stock data
    st.header("Stock Data")
    if symbol:
        stock_data = yf.download(symbol, start="2025-01-01", end="2025-05-01")
        st.line_chart(stock_data['Close'])

if __name__ == "__main__":
    if 'transactions' not in st.session_state:
        st.session_state.transactions = []
    main()