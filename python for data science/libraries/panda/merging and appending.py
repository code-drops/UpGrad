import pandas as pd

orders = pd.read_excel("C:/Users/dell/Desktop/sales_returns.xlsx",sheet_name="Orders")
returns = pd.read_excel("C:/Users/dell/Desktop/sales_returns.xlsx",sheet_name="Returns")

# merging above two tables , inner join : returns common values in both tables
return_orders = orders.merge(returns,on="Order ID")
print(return_orders.head())

# left join on table
return_orders = orders.merge(returns,on="Order ID",how="left")

# chaning the type of Nan(float) to nan(string)
return_orders["Returned"] = return_orders["Returned"].astype("str")
return_orders["Returned"] = return_orders["Returned"].apply(lambda x:"No" if x=="nan" else "Yes")
print(return_orders.head())

# ***********Appending data frames

df1 = pd.DataFrame({"Name":["Aman","Joy","Roshni","Saif"],
                    "Age":["34","31","22","33"],
                    "Gender":["M","M","F","M"]})

df2 = pd.DataFrame({"Name":["Akhil","Asha","Preeti"],
                    "Age":["31","22","23"],
                    "Gender":["M","F","F"]})

print(df1.append(df2))

df3 = pd.DataFrame(
    {
        "School":["RK public","JSP","Carmel convent","St. Paul"],
        "Marks":['84','89','76','91']
    }
)

# concatenating data frames on columns
print(pd.concat([df1,df3],1))