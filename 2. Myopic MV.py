#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 11:23:51 2024

@author: yangjiatian
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define the initial wealth
X_0 = 1  # Initial wealth in dollars/pounds

def analyze_dataset(file_name, window_size, T, monthly_target_return, X_0):
    # Read datasets
    df = pd.read_csv(file_name, index_col=0)
    
    # Re-structure the date format
    df.index = pd.to_datetime(df.index, format='%Y%m').to_period('M')
    
    # Proceed out-of-sample test
    out_of_sample_returns = []
    for t in range(window_size, len(df) - T):
        window_data = df.iloc[t-window_size:t]
        cov_matrix = window_data.cov()
        mean_returns = window_data.mean().values.reshape(-1, 1)
        inv_Sigma_t = np.linalg.inv(cov_matrix)
        denominator = (mean_returns.T @ inv_Sigma_t @ mean_returns)[0, 0]
        u_myopic = (X_0 * (monthly_target_return - risk_free_rate)) / denominator * (inv_Sigma_t @ mean_returns)
        u_myopic = u_myopic.flatten()
        
        for i in range(1, T + 1):
            next_period_return = np.dot(u_myopic, df.iloc[t + i].values)
            out_of_sample_returns.append(next_period_return / X_0)  # Normalize by initial wealth
            #print(f'Time {df.index[t + i]} (t={t}): Return at t+{i}: {next_period_return:.2f}%')

    # Calculate average return, standard deviation, variance and Sharpe ratio
    average_return = np.mean(out_of_sample_returns)
    std_dev = np.std(out_of_sample_returns)
    variance = np.var(out_of_sample_returns)
    sharpe_ratio = (average_return - risk_free_rate) / std_dev

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

# Parameters setting
window_size = 60
T = 1
monthly_target_return = 1 # Monthly_target_return of 1%
risk_free_rate = 0.01 # Example risk-free rate of 0.01%

# Deal each dataset one by one
for file_name in file_names:
    analyze_dataset(file_name, window_size, T, monthly_target_return, X_0)
