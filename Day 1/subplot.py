import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir(r"C:\Adv Analytics\Datasets")
cars93 = pd.read_csv("Cars93.csv")

#subplot demo

plt.subplot(1,2,1)
sns.boxplot(y='Price', data=cars93)
plt.title("Box Plot: Prices")

plt.subplot(1,2,2)
sns.histplot(data=cars93, x = 'Price', bins=8)
plt.title("Histogram")

plt.tight_layout()
plt.show()
