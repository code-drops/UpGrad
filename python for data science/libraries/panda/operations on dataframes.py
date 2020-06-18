import pandas as pd
import numpy as np

sales = pd.read_excel("C:/Users/dell/Desktop/sales.xlsx")

# changing the values of the sales
sales.Sales = sales.Sales.floordiv(1000)

# renaming the column
sales.rename(columns={"Sales":"Sales in thousands"},inplace=True)
print(sales)

# create a new column for positive profit using lambda functions
sales["Positive Profit"] = sales.Profit.apply(lambda x: np.nan if x<0 else x)
print(sales)