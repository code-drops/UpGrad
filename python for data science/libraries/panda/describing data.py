# Describing data

import pandas as pd

sales = pd.read_excel("C:/Users/dell/Desktop/sales.xlsx",index_col=1)
print(sales)

# return specific number of rows from top , default : 5
print(sales.head(10))

# return specific number of rows from bottom , default : 5
print(sales.tail(3))

# everything about the data
print(sales.info())

# quantative info about the data
print(sales.describe())

# number of rows and columns in dataframe
print(sales.shape)