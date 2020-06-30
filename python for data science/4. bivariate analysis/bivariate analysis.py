import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import seaborn as sns

# to remove the warnings
warnings.filterwarnings("ignore")

# read csv file and skipping first two rows
bank = pd.read_csv("bank marketing.csv",skiprows=2,index_col="customerid")

def missing_value_module(bank):
    bank["job"] = bank.jobedu.apply(lambda x: x.split(',')[0])
    bank["education"] = bank.jobedu.apply(lambda x: x.split(',')[1])
    del bank["jobedu"]
    len(bank[bank.month.apply(lambda x: True if type(x) == float else False) == True])
    bank = bank[-bank.age.isnull()]
    mode = bank['month'].mode()[0]
    bank['month'] = bank['month'].fillna(mode)
    bank['pdays'] = bank['pdays'].apply(lambda x: np.NaN if x < 0 else x)
    bank['duration'] = bank['duration'].apply(lambda x: float(x.split(' ')[0]) / 60 if x.endswith("sec") else x.split(' ')[0])
    return bank

bank = missing_value_module(bank)

################# Bivariate analysis ####################

######### numerical to numerical
# scatter plot between age and balance
plt.scatter(bank['age'],bank['balance'])
plt.show()

# pair plot shows all possible combinations between multiple variables
sns.pairplot(data=bank,vars=['salary','balance','age'])
plt.show()

# correlation matrix
bank[['age','salary','balance']].corr()

# using heatmap to represent the coorelation matrix
sns.heatmap(bank[['age','salary','balance']].corr(),annot=True,cmap='Reds')
plt.show()

######## numerical to category
print(bank.groupby('response')['salary'].mean())
print(bank.groupby('response')['salary'].median())

sns.boxplot(data=bank,x='response',y='salary')
plt.show()

print(bank.groupby('education')['salary'].aggregate(['mean','median']))

######## category to category
# education vs response
print(bank.groupby('education')['response'].value_counts(normalize=True))

# marital vs response
bank.groupby('marital')['response'].value_counts(normalize=True).plot(kind='bar')
plt.show()

# loan vs response
bank.groupby('loan')['response'].value_counts(normalize=True).plot(kind='bar')
plt.show()

# age vs response
# making buckets of ages and putting into a new column
bank['age_group'] = pd.cut(bank['age'],[0,30,40,50,60,999],labels=['<30','30-40','40-50','50-60','60+'])

