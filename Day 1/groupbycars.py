import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir(r"C:\Adv Analytics\Datasets")
cars93 = pd.read_csv("Cars93.csv")
print(cars93.groupby('AirBags')['Price'].mean())


cts = cars93.groupby('AirBags')['Price'].mean()
cts1 = cts.reset_index()
sns.barplot(data = cts1, x="AirBags", y="Price")
plt.ylabel("Mean Price")
plt.title("Air Bags for driver and passenger have higher mean price")
plt.show()
