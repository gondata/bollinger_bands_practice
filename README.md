# Bollinger Bands with Python

This script downloads stock price data for the Google (GOOG) ticker from Yahoo Finance using the pandas_datareader and yfinance libraries, and generates a graph of the Bollinger bands.

## Usage

To run the script, make sure you have Python installed and clone the repository to your local machine. Then, run the following command in your terminal:

```
python bollinger_bands.py
```

The resulting graph will be displayed on the screen.

## Dependencies

This script requires the following libraries to be installed:

. pandas_datareader
. yfinance
. matplotlib

You can install these libraries using pip:

```
pip install pandas-datareader yfinance matplotlib
```

## About Bollinger Bands

Bollinger Bands are a type of statistical chart characterizing the prices and volatility over time of a financial instrument or commodity. Bollinger Bands consist of a moving average and two standard deviation bands, one above and the other below the moving average. The upper and lower bands are typically 2 standard deviations from the moving average, and the bands will expand and contract as the volatility of the asset increases or decreases.
