# create the following plots (with titles, labels and a legend):

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('weather_data.txt', skipinitialspace = True)

# a. Actual max temperature and actual min temperature on the same line chart (max should be a red line, min should be blue)
data["actual_max_temp"]
plt.plot(data["actual_max_temp"], label = "Actual Max Temp", color = "red")
plt.plot(data["actual_min_temp"], label = "Actual Min Temp", color = "blue")
plt.title("Actual Max Temp and Actual Min Temp")
plt.xlabel("Actual Temp")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# b. A histogram of actual precipitation
data["actual_precipitation"].plot(kind = 'hist')
plt.title("Actual Precipitation")
plt.xlabel("Inches of Rain")
plt.ylabel("Frequency")
plt.legend()
plt.show()