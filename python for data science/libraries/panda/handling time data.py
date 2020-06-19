import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv("C:/Users/dell/Desktop/weather_data.csv",index_col=["Date_Time"],parse_dates=["Date_Time"])

# data between two dates
print(weather.loc["2010-05-10":"2010-06-10"])

# data between two time
print(weather.loc["2010-05-10 9:00:00":"2010-05-10 22:00:00"])

# plotting the line graph based on temperature between particular dates
dec = weather.loc["2010-12-15":"2010-12-31"]
dec[["Temperature"]].plot(kind="line")
plt.show()