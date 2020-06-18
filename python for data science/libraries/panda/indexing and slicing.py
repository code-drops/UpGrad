import pandas as pd

sales = pd.read_excel("C:/Users/dell/Desktop/sales.xlsx",index_col=1)
print(sales)

# fetching specific columns
# if used one bracket , it  will return series and if used double brackets, it will return data frame
print(sales["Profit"])                 # return series
print(sales[["Profit","Sales"]])        # return data frame

# fetching rows just like the slicing of array
# start index, end index ,steps
print(sales[2:20:2])

#  extracting a row : list_of_rows,list_of_columns
print(sales.loc[["Canada","Western Africa"],["Profit","Sales"]])        #when the labale of columns are known(label based indexing)
print(sales.iloc[0:5,2:])                                               # when index are known instead of labels(position based indexing)

# conditions on dataframe
print(sales[(sales["Profit"]>0)])
print(sales[(sales["Profit"]>0) & (sales["Market"].isin(["Europe","USCA"]))])