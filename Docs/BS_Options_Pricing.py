#!/usr/bin/env python
# coding: utf-8

# In[1]:


from SD import Financial_Analysis
import math
import pandas as pd
from pandas_datareader import data as pdr
import numpy as np
from scipy import stats


# In[2]:


class Option_Pricing:
    '''Class for the documentation of the Option Pricing methods
    X: Excercise Price
    r: Risk Free rate of Interest
    T: time to maturity of option (in year)
    S: Current Stock Price'''
    def __init__(self,ticker,X,r,T,start,end):
        self.tk=ticker
        self.X = X
        self.r = r
        self.T = T
        self.start = start
        self.end = end
        all_data = pdr.get_data_yahoo(self.tk, start=self.start, end=self.end)
        self.stock_data = pd.DataFrame(all_data['Adj Close'], columns=["Adj Close"])
        self.S=self.stock_data.iloc[-1]
        
    def standard_deviation(self):
        '''Standard Deviation is utilized for the calculation of Volatility'''
        pct_change = self.stock_data.pct_change()
        pct_change.dropna(inplace=True)
        std = pct_change.std()
        return std
    
    def volatility(self):
        '''Volatility is required for the calculation of Option Pricing'''
        volatility=self.standard_deviation()*math.sqrt(250)
        return volatility
    
    def d1(self):
        '''d1=(LN(S/X)+(r+0.5*sigma^2)*T)/(sigma*SQRT(T))'''
        d1=((np.log(self.S/self.X))+(self.r+(0.5*((self.volatility()**2)*self.T))))/(self.volatility()*math.sqrt(self.T))
        return d1

    def d2(self):
        '''d2= d1-sigma*SQRT(T)'''
        d2=self.d1()-(self.volatility()*math.sqrt(self.T))
        return d2
    
    def call_price(self):
        '''Call Price=S*N(d1)-X*exp(-r*T)*N(d2)'''
        call_price = float((self.S * stats.norm.cdf(self.d1())) - (self.X * np.exp(-self.r * self.T) * stats.norm.cdf(self.d1())))
        return call_price
    
    def put_price(self):
        '''Put price=X*exp(-r*T)*N(-d2) - S*N(-d1)'''
        put_price = float((self.X * np.exp(-self.r * self.T) * stats.norm.cdf(self.d2()*-1)) - (self.S * stats.norm.cdf(self.d1()*-1)))
        return put_price


# In[3]:


AAPL=Option_Pricing("AAPL",15,0.04,0.75, start="2016-01-01", end="2016-03-01")
AAPL.call_price()

