import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_datareader.data import DataReader
from datetime import datetime
import io

pi = pd.read_csv('personInf.csv')


def personPiechar(name):
    pi = pd.read_csv(os.path.join(os.getcwd(),'personInf.csv'))
    tech_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN']

# Set up End and Start times for data grab
    end = datetime.now()
    start = datetime(end.year , end.month, end.day)

#For loop for grabing yahoo finance data and setting as a dataframe
    for stock in tech_list:   
    # Set DataFrame as the Stock Ticker
       globals()[stock] = DataReader(stock, 'yahoo', start, end)
    company_list = [AAPL, GOOG, MSFT, AMZN]
    company_name = ["APPLE", "GOOGLE", "MICROSOFT", "AMAZON"]

    for company, com_name in zip(company_list, company_name):
        company["company_name"] = com_name
    
    comp = pd.concat(company_list, axis=0)
    comprice = comp['Close'].values
    user = pi[pi['Name'] == name]
    stock = user[['AAPL','GOOG','MSFT','AMZN']].values
    moneydist = comprice * stock
    labels = ['AAPL','GOOG','MSFT','AMZN']
    plot = plt.pie(moneydist,labels = labels, autopct = '%3.2f%%')
    plt.title('Here is your Stock Account',fontsize='large')
    plt.axis('equal')
    fig = plt.figure()
    fig.savefig('stockaccount.png', dpi=fig.dpi)
    plt.show()
