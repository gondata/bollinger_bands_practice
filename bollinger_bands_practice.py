# First of all we have to import the libraries that we are going to use

from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

yf.pdr_override()

# Then we have to download the data

ticker = ['GOOG']
startdate = '2018-01-01'
enddate = '2023-02-02'

data = pdr.get_data_yahoo(ticker, start=startdate, end=enddate)

# Variables

data['MA'] = data['Adj Close'].rolling(20).mean()
data['std'] = data['Adj Close'].rolling(20).std()

# Bollinger bands

data['Up'] = data['MA'] + 2 * data['std']
data['Down'] = data['MA'] - 2 * data['std']

# Graphs

ax = data[['Adj Close', 'Up', 'Down']].plot(color=['blue', 'green', 'red'])
ax.fill_between(data.index, data['Down'], data['Up'], facecolor='orange', alpha=0.1)
plt.show()