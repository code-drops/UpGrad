import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings

# to remove the warnings
warnings.filterwarnings("ignore")

# read csv file and skipping first two rows
bank = pd.read_csv("bank marketing.csv",skiprows=2,index_col="customerid")

################## Fixing the rows and columns #################################
# # correcting the jobedu column
bank["job"] = bank.jobedu.apply(lambda x:x.split(',')[0])
bank["education"] = bank.jobedu.apply(lambda x:x.split(',')[1])
del bank["jobedu"]

#number of missing values in all columns
print(bank.isnull().sum())

# there are 50 records which have NaN values in them in month column
print(len(bank[bank.month.apply(lambda x: True if type(x)==float else False)==True]))


############ handling the missing values #################################

# dropping the records with missing age
bank = bank[-bank.age.isnull()]

# # # handling missing month
# value and their count
print(bank['month'].value_counts())

mode = bank['month'].mode()[0]

# filling the NA/NaN values
bank['month'] = bank['month'].fillna(mode)

# handling -1 in pdays
# replacing the -1 with NaN value in order to not take them in mean , mode or median operation
bank['pdays'] = bank['pdays'].apply(lambda x: np.NaN if x<0 else x)
print(bank['pdays'].describe())

##### Handling outliers

# watching outliers in age columns
bank['age'].plot(kind="box")              #valid outliers
plt.show()

# outliers in balance column
bank['balance'].plot(kind="box")           # valid outliers
plt.show()

####################### standardizing dataset
# some values are in min and some are in seconds
bank['duration'] = bank['duration'].apply(lambda x : float(x.split(' ')[0])/60 if x.endswith("sec") else x.split(' ')[0])
