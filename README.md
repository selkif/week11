# KAIM_Week11
# Stock Market Analysis and Forecasting

This project involves fetching, preprocessing, analyzing, forecasting, and optimizing a portfolio using historical stock market data. The goal is to understand the volatility of Tesla (TSLA), Vanguard Total Bond Market ETF (BND), and S&P 500 ETF (SPY), and to forecast Tesla's stock price using time series models.

## Project Overview

### Task 1: Preprocess and Explore the Data

1. **Fetch Historical Data**: Download stock data from Yahoo Finance (YFinance) for TSLA, BND, and SPY.
2. **Data Cleaning**: Handle missing values, check data types, and normalize if required.
3. **Exploratory Data Analysis (EDA)**:
   - Visualize closing prices over time.
   - Analyze daily percentage change and volatility.
   - Detect outliers based on returns.
   - Identify seasonality and trends using decomposition.

### Task 2: Develop Time Series Forecasting Models

1. **Model Selection**:
   - ARIMA (AutoRegressive Integrated Moving Average)
   - SARIMA (Seasonal ARIMA)
   - LSTM (Long Short-Term Memory Neural Network)
2. **Model Training & Evaluation**:
   - Split data into training and testing sets.
   - Train models and optimize parameters (using `auto_arima` for ARIMA/SARIMA).
   - Evaluate using MAE, RMSE, and MAPE.

### Task 3: Forecast Future Market Trends

1. **Generate Future Price Predictions** (6-12 months ahead).
2. **Analyze Trends, Volatility, and Risk**.
3. **Assess Market Opportunities and Risks**.

### Task 4: Optimize Portfolio Based on Forecast

1. **Portfolio Composition**:
   - Tesla (TSLA) – High risk, high return.
   - Vanguard Bond ETF (BND) – Stability and low risk.
   - S&P 500 ETF (SPY) – Diversified market exposure.
2. **Compute Returns & Risk Metrics**:
   - Calculate annual return and volatility.
   - Optimize asset allocation using the Sharpe Ratio.
   - Measure Value at Risk (VaR).
3. **Portfolio Optimization**:
   - Adjust asset allocations to maximize returns and minimize risk.
   - Visualize portfolio performance based on forecasted returns.

## Requirements

Install dependencies before running the script:

```bash
pip install yfinance numpy pandas matplotlib seaborn statsmodels pmdarima scipy scikit-learn
```

## How to Run

1. **Fetch & Preprocess Data**
   - Run the script to download data and perform initial analysis.
2. **Train a Forecasting Model**
   - Choose ARIMA, SARIMA, or LSTM and train it on TSLA stock data.
3. **Generate & Analyze Forecasts**
   - Forecast future prices and visualize trends.
4. **Optimize Portfolio Allocation**
   - Adjust asset weights to maximize the Sharpe Ratio.

## Results

- **Stock Trends**: Identified volatility and long-term trends.
- **Forecasting**: ARIMA/SARIMA provided insights into Tesla’s future stock performance.
- **Portfolio Optimization**: Adjusted asset allocation to maximize risk-adjusted returns.

## Future Improvements

- Implement deep learning models like LSTM for more accurate forecasting.
- Add real-time data fetching and updates.
- Expand to include more assets for broader market analysis.

##

