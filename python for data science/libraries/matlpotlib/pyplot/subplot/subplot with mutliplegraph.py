# Different plots presented in a single plot object are commonly referred to as subplots
# If you want to analyse the number of purchases across different categories, then you can make multiple bar charts for each category: for instance, one for male buyers and one for female buyers.
# These two charts, placed next to each other, make it easy to compare the buying patterns of the male and female consumers.

import matplotlib.pyplot as plt
import numpy as np

# data
years = np.array(['2012', '2013', '2014', '2015'])
sales_Africa = np.array([127187.27, 144480.70, 229068.79, 283036.44])
sales_Asia_Pacific = np.array([713658.22, 863983.97, 1092231.65, 1372784.40])
sales_Europe = np.array([540750.63, 717611.40, 848670.24, 1180303.95])

fig,ax = plt.subplots(ncols=3 , sharey=True)

africa, = ax[0].plot(years,sales_Africa)
asia, = ax[1].plot(years,sales_Asia_Pacific)
europe, = ax[2].plot(years,sales_Europe)

plt.legend([africa,asia,europe],["Africa","Asia Pacific","Europe"])

plt.show()