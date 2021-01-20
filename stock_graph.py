import yfinance as yf
import matplotlib.pyplot as plt

# list of stocks to retrieve
stocks = ["AAPL", "GOOGL"];

# retrieve stock data
data = yf.download(stocks, start = "2010-01-01", end = "2020-12-31");

# print sample of data
print(data.head());

# copy data from Close column
closedStocks = data.loc[:,"Close"].copy();

# plot stock data, save graph as png
closedStocks.plot();
plt.savefig("stock-graph.png");
plt.show();
