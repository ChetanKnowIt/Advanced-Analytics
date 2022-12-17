from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

milk = pd.read_csv("milk.csv", index_col=0)

scaler = StandardScaler()
milkscaled = scaler.fit_transform(milk)
# Finding the best cluster based on WSS
wss = []
for i in np.arange(2,10):
    km = KMeans(n_clusters=i, random_state=2022)
    km.fit(milkscaled)
    wss.append(km.inertia_)

plt.scatter(np.arange(2,10), wss)
plt.plot(np.arange(2,10), wss)
plt.title("Scree Plot")
plt.xlabel("Ks")
plt.ylabel("WSS")
plt.show()

# Best cluster
km = KMeans(n_clusters=4, random_state=2022)
km.fit(milkscaled)
labels = km.predict(milkscaled)

milk["Cluster"] = labels
milk.sort_values('Cluster', inplace=True)

# Calculating the centroids
milk.groupby('Cluster').mean()

# Finding the best cluster based on Silhouette
sil = []
for i in np.arange(2,10):
    km = KMeans(n_clusters=i, random_state=2022)
    km.fit(milkscaled)
    labels = km.predict(milkscaled)
    sil.append(silhouette_score(milkscaled, labels))

Ks = np.arange(2,10)
i_max = np.argmax(sil)
best_k = Ks[i_max]
print("Best K =", best_k)

############### nutrient #################

nutrient = pd.read_csv("nutrient.csv", index_col=0)

scaler = StandardScaler()
nutrientscaled = scaler.fit_transform(nutrient)

# Finding the best cluster based on Silhouette
sil = []
for i in np.arange(2,10):
    km = KMeans(n_clusters=i, random_state=2022)
    km.fit(nutrientscaled)
    labels = km.predict(nutrientscaled)
    sil.append(silhouette_score(nutrientscaled, labels))

Ks = np.arange(2,10)
i_max = np.argmax(sil)
best_k = Ks[i_max]
print("Best K =", best_k)

######################### RFM ##########################
import os
os.chdir(r"C:\Training\Academy\Statistics (Python)\Cases\Recency Frequency Monetary")

rfm = pd.read_csv("rfm_data_customer.csv", index_col=0)
rfm.drop('most_recent_visit', axis=1, inplace=True)

scaler = StandardScaler()
rfmscaled = scaler.fit_transform(rfm)

# Finding the best cluster based on Silhouette
sil = []
for i in np.arange(2,10):
    km = KMeans(n_clusters=i, random_state=2022)
    km.fit(rfmscaled)
    labels = km.predict(rfmscaled)
    score = silhouette_score(rfmscaled, labels)
    sil.append(score)
    print("K=",i," Score=", score)
    

Ks = np.arange(2,10)
i_max = np.argmax(sil)
best_k = Ks[i_max]
print("Best K =", best_k)

km = KMeans(n_clusters=best_k, random_state=2022)
km.fit(rfmscaled)
labels = km.predict(rfmscaled)

rfm["Cluster"] = labels
rfm.sort_values('Cluster', inplace=True)

# Calculating the centroids
rfm.groupby('Cluster').mean()


