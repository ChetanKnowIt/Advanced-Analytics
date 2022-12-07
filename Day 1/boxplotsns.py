import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir(r"C:\Adv Analytics\Datasets")
cars93 = pd.read_csv("Cars93.csv")

sns.boxplot(x="AirBags",y='Price',data=cars93)
plt.title("Boxplot: Prices of cars")
plt.show()
