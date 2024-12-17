#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 17:36:08 2024

@author: yangjiatian
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 3. Perform dynamic mean-variance strategy

def dynamic_mean_variance(df, window_size, T, monthly_target_return, risk_free_rate):
    out_of_sample_returns = []
    
    for t in range(window_size, len(df) - T):
        window_data = df.iloc[t-window_size:t]
        cov_matrix = window_data.cov()
        mean_returns = window_data.mean().values.reshape(-1, 1)
        inv_Sigma_t = np.linalg.inv(cov_matrix)
        
        B = np.prod([1 - (mean_returns.T @ inv_Sigma_t @ mean_returns)[0, 0] for _ in range(T)])
        
        # If B >= 1 then skip
        if B >= 1:
            continue
        
        X0 = 1
        prod_rk = 1
        for k in range(t+1, t+T):
            prod_rk *= 1 / (1 + risk_free_rate)
        
        mu_bar_T = monthly_target_return
        term1 = (X0 * prod_rk) * (mu_bar_T / (1 - B))
        term2 = (np.prod([1 + risk_free_rate for _ in range(T)]) * B / (1 - B))
        rt_Xt = risk_free_rate * X0
        
        for i in range(1, T + 1):
            u_dynamic = (term1 - term2 - rt_Xt) * inv_Sigma_t @ mean_returns
            u_dynamic = u_dynamic.flatten()
            
            next_period_return = np.dot(u_dynamic, df.iloc[t + i].values)
            out_of_sample_returns.append(next_period_return)
            
            # Update X0 and rt_Xt for the next period
            X0 = X0 * (1 + next_period_return)
            rt_Xt = risk_free_rate * X0
    
    average_return = np.mean(out_of_sample_returns)
    std_dev = np.std(out_of_sample_returns)
    variance = np.var(out_of_sample_returns)
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

# Parameters setting
window_size = 60
T = 1
monthly_target_return = 1 # Monthly_target_return of 1%
risk_free_rate = 0.01  # Example risk-free rate of 0.01%

# Deal each dataset one by one
for file_name in file_names:
    df = pd.read_csv(file_name, index_col=0)
    df.index = pd.to_datetime(df.index, format='%Y%m').to_period('M')
    dynamic_mean_variance(df, window_size, T, monthly_target_return, risk_free_rate)
