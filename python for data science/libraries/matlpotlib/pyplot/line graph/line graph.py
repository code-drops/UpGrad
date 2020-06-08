# A line graph is used to present continuous time-dependent data. It accurately depicts the trend of a variable over a specified time period

import numpy as np
import matplotlib.pyplot as plt

# data
months = np.array(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
sales = np.array([241268.56, 184837.36, 263100.77, 242771.86, 288401.05, 401814.06, 258705.68, 456619.94, 481157.24, 422766.63, 555279.03, 503143.69])

# setting the title and labels  for axis
plt.title("Sales over months in 2015")
plt.xlabel("Months")
plt.ylabel("Sales")

# rotate the labels to avoid overlapping
plt.xticks(rotation=90)

# plotting points on graph with green color and showing them with 'o'... other option can be 'x'
plt.plot(months,sales,color="green",marker="o")
plt.show()