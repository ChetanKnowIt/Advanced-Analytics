import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir(r"C:\Adv Analytics\Datasets")
housing = pd.read_csv("housing.csv")

#subplot demo

plt.subplot(2,2,1)
sns.boxplot(y='price', data=housing)
plt.title("Box Plot: Prices")

plt.subplot(2,2,2)
sns.histplot(data=housing, x = 'price', bins=8)
plt.title("Histogram Prices")


plt.subplot(2,2,3)
sns.scatterplot(data=housing, x = 'lotsize', y='price', hue='bedrooms')
plt.title("Scatterplot Area - Prices")

plt.subplot(2,2,4)
cts = housing["bathrms"].value_counts()
cts1 = cts.reset_index()
cts1.columns = ['bathrms', 'count']
sns.barplot(data = cts1, x = 'bathrms', y='count')
plt.xlabel('Bathrooms')
plt.ylabel('Count')
plt.title("Box Plot: Prices")



plt.tight_layout()
plt.show()


g = sns.FacetGrid(housing, col = 'bathrms')
g = g.map(plt.scatter, "lotsize", "price")
plt.show
