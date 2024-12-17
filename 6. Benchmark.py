#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 23:30:39 2024

@author: yangjiatian
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 6. Perform naive_1_N_strategy
# Define the initial wealth
X_0 = 1  
risk_free_rate = 0.01 / 100  # Risk-free rate converted to decimal

def equal_weighted_1_N_strategy(df, X_0):
    df = df / 100.0  # Convert the percentage data to decimal form
    N = len(df.columns)  # Number of assets
    allocation = X_0 / N  # Equal allocation per asset
    portfolio_returns = df.sum(axis=1) * (allocation / X_0)
    return portfolio_returns

def process_datasets(file_names, X_0):
    for file_name in file_names:
        df = pd.read_csv(file_name, index_col=0)
        df.index = pd.to_datetime(df.index, format='%Y%m').to_period('M')
        
        portfolio_returns = equal_weighted_1_N_strategy(df, X_0)
        
        # Calculate the average return, standard deviation, variance, and Sharpe ratio
        average_return = portfolio_returns.mean() * 100  # Convert back to percentage
        std_dev = portfolio_returns.std() * 100  # Convert back to percentage
        variance = portfolio_returns.var() * 10000  # Convert back to percentage squared
        sharpe_ratio = ((average_return / 100) - risk_free_rate) / (std_dev / 100) if std_dev != 0 else 0
        
        # Display the results
        print(f'Average Return for {file_name}: {average_return:.2f}%')
        print(f'Standard Deviation for {file_name}: {std_dev:.2f}')
        print(f'Variance for {file_name}: {variance:.2f}')
        print(f'Sharpe Ratio for {file_name}: {sharpe_ratio:.2f}')
        

# List of dataset file names
file_names = [
    '6_Portfolios_ME_BM_2x3.csv',
    '6_Portfolios_ME_DP_2x3.csv',
    '6_Portfolios_ME_EP_2x3.csv',
    '6_Portfolios_ME_INV_2x3.csv',
    '6_Portfolios_ME_OP_2x3.csv'
]

# Process each dataset
process_datasets(file_names, X_0)
