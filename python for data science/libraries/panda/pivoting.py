import matplotlib.pyplot as plt
import pandas as pd

users = pd.DataFrame({
    "weekday": ["Sun","Sun","Mon","Mon"],
    "city":["Austin","Dallas","Austin","Dallas"],
    "visitors":[139,237,326,456],
    "signups":[7,12,3,5]
})
users.set_index("weekday",inplace=True)
users.plot(kind="bar")
plt.show()

# identify unique city and fetch only visitors value
visitors_pivot = users.pivot(columns="city",values="visitors")
visitors_pivot.plot(kind="bar")
plt.show()

visitors = users.pivot(columns="city")
visitors["visitors"].plot(kind="bar")
visitors["signups"].plot(kind="bar")
plt.show()