
import pandas as pd
import numpy as np
import math
import datetime as dt
from pandas_datareader import data as pdr
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import math


class Financial_Analysis:
    def __init__(self, tk, start, end):
        self.tk = tk
        self.start = start
        self.end = end
        all_data = pdr.get_data_yahoo(self.tk, start=self.start, end=self.end)
        self.stock_data = pd.DataFrame(all_data['Adj Close'], columns=["Adj Close"])
        
    def standard_deviation(self):
        pct_change = self.stock_data.pct_change()
        pct_change.dropna(inplace=True)
        #mean = self.df['Close'].mean()
        #np.std(self.df['Close'])
        std=pct_change.std()
        return std

