# A bar graph is helpful when you have to visualise a numeric feature (fact) across multiple categories.

import numpy as np
import matplotlib.pyplot as plt

# data
product_category = np.array(["furniture","technology","office supplies"])
sales = np.array([4110,4744,3787])

# setting title,color and labels for axis
plt.title("Sales for a product category",fontdict={"color":"red"})
plt.xlabel("Product category",fontdict={"color":"green"})
plt.ylabel("Sales",fontdict={"color":"green"})

# setting the ticks values and labels for the y axis
tick_values = np.arange(0,7000,1000)
tick_labels =["0","1K","2K","3K","4K","5K","6K","7K"]
plt.yticks(tick_values,tick_labels)


# plotting graph and then display it
plt.bar(product_category,sales,color="yellow",edgecolor="blue")
plt.show()
