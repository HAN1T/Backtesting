
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
    '''Class for the documentation of all the Statistical Analysis attributes'''
    def __init__(self, tk, start, end):
        self.tk = tk
        self.start = start
        self.end = end
        all_data = pdr.get_data_yahoo(self.tk, start=self.start, end=self.end)
        self.stock_data = pd.DataFrame(all_data['Adj Close'], columns=["Adj Close"])
        
    def standard_deviation(self):
        '''std attribute of pandas module directly returns standard deviation of time series'''
        pct_change = self.stock_data.pct_change()
        pct_change.dropna(inplace=True)
        std=pct_change.std()
        return std

    def volatility(self):
        '''annualised volatility can be calculated by multiplying SD with the square root of time period
        since our price data is daily, so root of 250, if was montly then root of 12''' 
        volatility=self.standard_deviation()*math.sqrt(250)
        return volatility
