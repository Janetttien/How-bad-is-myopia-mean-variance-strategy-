#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 11:23:37 2024

@author: yangjiatian
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 5. Perform rebalanced_strategy
# Define the initial wealth
X_0 = 1  

def rebalanced_strategy(df, T, beta, risk_free_rate):
    rebalanced_returns = []
    portfolio_values = []

    # Calculate the equal weights
    N = len(df.columns)  # Number of assets

    # Loop each t
    for t in range(len(df) - T):
        X_t = X_0  # Reset initial wealth for each period
        allocation = (beta * X_t / N) * np.ones(N)  # Initial equal allocation
        
        period_returns = []  # To record returns for each investment period
        
        for i in range(T):
            # Calculate the returns for the next period
            returns = df.iloc[t + i].values / 100  # Convert to decimal
            portfolio_return = np.dot(allocation, returns)  # Calculate portfolio return
            X_t *= (1 + portfolio_return)  # Update total wealth
            allocation = (X_t / N) * np.ones(N)  # Reset asset allocation
            
            period_returns.append(portfolio_return)  # Record return for each period
        
        total_period_return = np.prod([1 + r for r in period_returns]) - 1  # Calculate total period return
        rebalanced_returns.append(total_period_return * 100)  # Convert to percentage
        portfolio_values.append(X_t)

    average_return = np.mean(rebalanced_returns)
    std_dev = np.std(rebalanced_returns)
    variance = np.var(rebalanced_returns)
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
beta = 1  
risk_free_rate = 0.01 # Example risk-free rate of 0.01%

# Process each dataset
for file_name in file_names:
    df = pd.read_csv(file_name, index_col=0)
    df.index = pd.to_datetime(df.index, format='%Y%m').to_period('M')
    rebalanced_strategy(df, T, beta, risk_free_rate)

