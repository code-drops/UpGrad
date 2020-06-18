# Series and Data Frames structures in Pandas

import pandas as pd
import numpy as np

cars_per_cap = [809, 731, 588, 18, 200, 70, 45]
country = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
drives_right = [False, True, True, True, False, False, False]

# Series data structure
car = pd.Series(country)
print(car)

# Data Frame strcuture
cars_dict = { "cars_per_cap":cars_per_cap , "country":country , "drives_right":drives_right }
cars = pd.DataFrame(cars_dict)
print(cars)


# import data from csv file
car2 = pd.read_csv("C:/Users/dell/Desktop/cars.csv",header=None,index_col=1)
print(car2)

# setting the columns names
car2.columns = ["Region code","Country","cars per capita","drives right"]
print(car2)

# heirarchical indexing
car2 = pd.read_csv("C:/Users/dell/Desktop/cars.csv",header=None,index_col=[0,1])
car2.columns = ["Country","cars per capita","drives right"]
car2.index.names = ["Region code","country code"]
print(car2)