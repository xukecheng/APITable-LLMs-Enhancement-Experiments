# filename: stock_chart.py

import yfinance as yf
import matplotlib.pyplot as plt

# Step 3: Read the stock price data with yfinance
tickers = ['NVDA', 'TSLA']
data = yf.download(tickers, start='2022-01-01')

# Step 5: Plot the stock prices
plt.plot(data.index, data['Close']['NVDA'], label='NVDA')
plt.plot(data.index, data['Close']['TSLA'], label='TSLA')

# Add labels and title to the chart
plt.xlabel('Date')
plt.ylabel('Stock Price ($)')
plt.title('NVDA and TSLA Stock Price Change YTD')

# Add a legend
plt.legend()

# Step 6: Save the plot as a PNG file
plt.savefig('stock_chart.png')

# Output a message confirming the chart is saved
print("Stock chart saved as stock_chart.png")