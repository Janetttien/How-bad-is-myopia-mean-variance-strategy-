#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 19:50:20 2024

@author: yangjiatian
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 4. Perform buy_and_hold_strategy
# Define the initial wealth
X_0 = 1  

def buy_and_hold_strategy(df, T, alpha, risk_free_rate):
    buy_and_hold_returns = []
    portfolio_values = []

    # Calculate the equal weights
    N = len(df.columns)  # Number of assets
    initial_allocation = alpha * X_0 / N  # Initial asset allocation

    # Loop each t
    for t in range(len(df) - T):
        wealth = np.array([initial_allocation] * N)  # Reset initial wealth for each period
        
        # Calculate compound returns for T periods
        for i in range(T):
            returns = df.iloc[t + i].values / 100  # Convert to decimal
            wealth *= (1 + returns)
        
        portfolio_value = wealth.sum()  # Total portfolio value
        period_return = (portfolio_value / (alpha * X_0)) - 1  # Portfolio return
        buy_and_hold_returns.append(period_return * 100)  # Convert to percentage
        portfolio_values.append(portfolio_value)

    average_return = np.mean(buy_and_hold_returns)
    std_dev = np.std(buy_and_hold_returns)
    variance = np.var(buy_and_hold_returns)
    sharpe_ratio = (average_return - risk_free_rate) / std_dev if std_dev != 0 else 0

    print(f'Average Return for {file_name}: {average_return:.2f}%')
    print(f'Standard Deviation for {file_name}: {std_dev:.2f}')
    print(f'Variance for {file_name}: {variance:.2f}')
    print(f'Sharpe Ratio for {file_name}: {sharpe_ratio:.2f}')
    
    
# List multiple datasets
file_names = [
    '6_Portfolios_ME_BM_2x3.csv',
    '6_Portfolios_ME_DP_2x3.csv',
    '6_Portfolios_ME_EP_2x3.csv',
    '6_Portfolios_ME_INV_2x3.csv',
    '6_Portfolios_ME_OP_2x3.csv'
]

# Set parameters
T = 2
alpha = 1  
risk_free_rate = 0.01  # Example risk-free rate of 0.01%


for file_name in file_names:
    df = pd.read_csv(file_name, index_col=0)
    df.index = pd.to_datetime(df.index, format='%Y%m').to_period('M')
    buy_and_hold_strategy(df, T, alpha, risk_free_rate)

