import pandas as pd

sales = pd.read_excel("C:/Users/dell/Desktop/sales.xlsx",index_col=[0,1])

# group by market
print(sales[["No_of_Orders"]].groupby("Market").sum())

# group by sales
print(sales[["Sales"]].groupby("Market").sum())

# max orders
print(sales[["No_of_Orders"]].groupby("Market").max())

# average profit per market
print(sales[["Profit"]].groupby("Market").mean())