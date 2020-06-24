import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings

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


##################### univariate analysis - categorical unordered (job,blood group,marital status,department)
# plotting the job column and analysing
bank['job'].value_counts().plot(kind="barh")
plt.show()

# plotting the marital column and analysing
bank['marital'].value_counts(normalize=True).plot(kind="barh")
plt.show()


##################### univariate analysis - categorical ordered(age,month,education)
plotting and analysing education column
bank['education'].value_counts().plot(kind="pie")
plt.show()

# plotting and analysing the poutcome
bank['poutcome'].value_counts().plot(kind="barh")
bank[-(bank['poutcome']=='unknown')]['poutcome'].value_counts().plot(kind="barh")        # removing the unknown category
plt.show()

# plotting and analysing the response variable
bank['response'].value_counts().plot(kind="barh")
plt.show()