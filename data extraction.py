#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 20:36:52 2024

@author: yangjiatian
"""
 
import pandas as pd  
import seaborn as sns
import matplotlib.pyplot as plt

# 1.Data preparation before doing analysis
# Define the function of dealing datasets
def analyze_dataset(file_name):
    # Read datasets
    df = pd.read_csv(file_name, index_col=0)
    
    # Re-structure the date format
    df.index = pd.to_datetime(df.index, format='%Y%m').to_period('M')
    
    # Check the format of dataset
    stock_symbols = df.columns.tolist()
    print(df.head())
    print(df.describe())
    
    # Check missing data
    print(df.isnull().sum())
    
    # Plot boxplot to check outliers
    plt.figure(figsize=(10, 6))
    boxprops = dict(color='black')
    flierprops = dict(marker='o', color='gray', alpha=0.5)
    medianprops = dict(color='black')
    whiskerprops = dict(color='black')
    capprops = dict(color='black')
    df.boxplot(boxprops=boxprops, flierprops=flierprops, medianprops=medianprops, whiskerprops=whiskerprops, capprops=capprops)
    plt.title(f'Boxplot of {file_name}', fontsize=16)
    plt.xlabel('Assets', fontsize=14)
    plt.ylabel('Returns', fontsize=14)
    plt.tight_layout()
    plt.savefig(f'{file_name}_boxplot.png')
    plt.show()
    
    
    # Plot covariance matrix
    covariance_matrix = df.cov()
    print(covariance_matrix)
    plt.figure(figsize=(10, 8))
    sns.heatmap(covariance_matrix, annot=True, fmt=".2f", cmap='Greys', cbar_kws={'label': 'Covariance Value'})
    plt.title(f'Covariance Matrix of {file_name}', fontsize=16)
    plt.xlabel('Assets', fontsize=14)
    plt.ylabel('Assets', fontsize=14)
    plt.tight_layout()
    plt.savefig(f'{file_name}_covariance_matrix.png')
    plt.show()

# List multiple datasets
file_names = [
    '6_Portfolios_ME_BM_2x3.csv',
    '6_Portfolios_ME_DP_2x3.csv',
    '6_Portfolios_ME_EP_2x3.csv',
    '6_Portfolios_ME_INV_2x3.csv',
    '6_Portfolios_ME_OP_2x3.csv'
]

# Deal each dataset one by one
for file_name in file_names:
    analyze_dataset(file_name)