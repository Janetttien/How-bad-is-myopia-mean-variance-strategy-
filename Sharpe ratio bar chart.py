#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:30:46 2024

@author: yangjiatian
"""

import matplotlib.pyplot as plt
import numpy as np

# # List of data names
datasets = [
    'Size and Book-to-Market',
    'Size and Operating Profitability',
    'Size and Investment',
    'Size and Dividend Yield',
    'Size and Earnings/Price'
]
myopic_sharpe_ratios = [0.16, 0.29, 0.18, 0.18, 0.14]
dynamic_sharpe_ratios = [0.20, 0.23, 0.29, 0.19, 0.22]

x = np.arange(len(datasets))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, myopic_sharpe_ratios, width, label='Myopic MV', color='skyblue')
rects2 = ax.bar(x + width/2, dynamic_sharpe_ratios, width, label='Dynamic MV', color='orange')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Datasets')
ax.set_ylabel('Sharpe Ratio')
ax.set_title('Sharpe Ratio Comparison: Myopic vs Dynamic MV Strategies')
ax.set_xticks(x)
ax.set_xticklabels(datasets, rotation=45, ha='right')
ax.legend()

# Remove the top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add gridlines
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Add bar labels
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(rects1)
add_labels(rects2)

fig.tight_layout()

plt.show()

