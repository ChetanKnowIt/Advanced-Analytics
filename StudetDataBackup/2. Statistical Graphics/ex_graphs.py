import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import os
os.chdir(r"C:\Training\Academy\Statistics (Python)\Datasets")

df = pd.read_csv("Housing.csv")
print(df.columns)

# 1.
df['price'].skew() # Postively Skewed
df['price'].kurtosis() # Somewhat Peaked
sns.histplot(data=df, x='price')
plt.show()


# 2.
sns.scatterplot(data=df,x="lotsize",y="price",
                hue="airco")
plt.title("Scatter Plot")
plt.xlabel("Area")
plt.ylabel("Price")
plt.show()

# 3.
sns.boxplot(x="bedrooms",y='lotsize', data=df)
plt.show()

sns.boxplot(x="bathrms",y='price', data=df)
plt.show()

# 4.
plt.subplot(2,2,1)
sns.boxplot(y='price', data=df)
plt.title("Box Plot")

plt.subplot(2,2,2)
sns.histplot(data=df, x='price')
plt.title("Histogram")

plt.subplot(2,2,3)
sns.scatterplot(data=df,x="lotsize",
                y="price", hue="bedrooms")
plt.legend(loc="best")
plt.title("Scatter Plot")
plt.xlabel("Area")
plt.ylabel("Price")

plt.subplot(2,2,4)
cts = df["bathrms"].value_counts()
cts1 = cts.reset_index()
cts1.columns = ['bathrms', 'Count']
sns.barplot(data=cts1, x='bathrms', y='Count')

plt.tight_layout()
plt.show()

# 5.
g = sns.FacetGrid(df, col="bathrms")
g = g.map(plt.scatter, "lotsize",
          "price")
plt.show()

# 6.
sns.jointplot(data=df,x="lotsize",y="price")
plt.xlabel("Area")
plt.ylabel("Price")
plt.show()
