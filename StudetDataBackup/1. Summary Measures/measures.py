import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


import os
os.chdir(r"C:\Training\Academy\Statistics (Python)\Datasets")

cars93 = pd.read_csv("Cars93.csv")
print(cars93.shape)
print(cars93.columns)
print(cars93.dtypes)
# Meta Data
print(cars93.info())

cars93['Price'].mean()
cars93['Price'].median()
cars93['Price'].quantile(q=0.25)
cars93['Price'].quantile(q=0.75)
cars93['Price'].quantile(q=np.array([0.25, 0.5, 0.75]))

cars93['Price'].plot(kind='box')
plt.show()

# Std Deviation
cars93['Price'].std()

# Variance
cars93['Price'].var()

# Coefficient of Variation
cv = cars93['Price'].std()/cars93['Price'].mean()
cv

# Skewness
from scipy.stats import skew
skew(cars93['Price'])
cars93['Price'].skew()

# Kurtosis
from scipy.stats import kurtosis
kurtosis(cars93['Price'], fisher=True)
cars93['Price'].kurtosis() 


############## Group By Aggregation ##############
cars93['Price'].mean()

no_bags = cars93[cars93["AirBags"] == "None"]
driver = cars93[cars93["AirBags"] == "Driver only"]
d_p = cars93[cars93["AirBags"] == "Driver & Passenger"]
print(no_bags['Price'].mean())
print(driver['Price'].mean())
print(d_p['Price'].mean())

cars93.groupby('AirBags')['Price'].mean()
