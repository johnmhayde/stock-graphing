import yfinance as yf

stocks = ["AAPL", "GOOGL"];

data = yf.download(stocks, start="2020-01-01", end="2020-12-01");

print(data.head(10));
