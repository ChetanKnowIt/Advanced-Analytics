from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

milk = pd.read_csv("milk.csv", index_col=0)

scaler = StandardScaler()
milkscaled = scaler.fit_transform(milk)

mergings = linkage(milkscaled,method='average')
#fig_size = plt.rcParams["figure.figsize"]
#fig_size[0] = 12
#fig_size[1] = 8
#plt.rcParams["figure.figsize"] = fig_size
dendrogram(mergings, labels=list(milk.index),
           leaf_rotation=90, leaf_font_size=10)
plt.show()

################# nutrient ####################

nutrient = pd.read_csv("nutrient.csv", index_col=0)

scaler = StandardScaler()
nutrientscaled = scaler.fit_transform(nutrient)

mergings = linkage(nutrientscaled,method='average')
#fig_size = plt.rcParams["figure.figsize"]
#fig_size[0] = 12
#fig_size[1] = 8
#plt.rcParams["figure.figsize"] = fig_size
dendrogram(mergings, labels=list(nutrient.index),
           leaf_rotation=90, leaf_font_size=10)
plt.show()

