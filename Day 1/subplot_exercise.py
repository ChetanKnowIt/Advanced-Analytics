import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir(r"C:\Adv Analytics\Datasets")
cars93 = pd.read_csv("Cars93.csv")

#subplot demo

plt.subplot(2,2,1)
sns.boxplot(y='Price', data=cars93)
plt.title("Box Plot Prices")

plt.subplot(2,2,2)
sns.histplot(data=cars93, x = 'Price', bins=8)
plt.title("Histogram Prices")

plt.subplot(2,2,3)
sns.scatterplot(data=cars93, x = 'Price',y='MPG.highway')
plt.title("Scatterplot Prices")

plt.subplot(2,2,4)
sns.histplot(data=cars93, x = 'Type', bins=8)
plt.title("Histogram Types")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
