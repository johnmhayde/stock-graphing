import yfinance as yf
import numpy as np
import pandas as pd

# variable declaration
stocks = ["AAPL", "GOOGL"];
startDate = "2020-01-01";
endDate = "2020-12-01"

# make list of date range
dateList = pd.date_range(startDate, endDate);

# initialize arrays with size of list
numElements = len(dateList);
x = [];
y = np.zeros(numElements);
# print(numElements);

# store dates in x array
for i in range(0, numElements):
	line = str(dateList[i]).split();
	x.append(line[0]);

# pull data from yfinance
data = yf.download("GOOGL", start=startDate, end=endDate, group_by="ticker");

closedStocks = data.loc[:,"Close"].copy();

print(closedStocks)
