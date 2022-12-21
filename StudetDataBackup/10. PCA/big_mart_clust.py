import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import os
os.chdir(r"C:\Training\AV\Big Mart III")

train = pd.read_csv("processed_train.csv")

items_data = train[['Item_Type','i_weight',
                    'Item_Visibility','Item_MRP','Item_Outlet_Sales']]

items_means = items_data.groupby('Item_Type').mean()


scaler = StandardScaler()
i_scaled = scaler.fit_transform(items_means)

mergings = linkage(i_scaled,method='average')

dendrogram(mergings, labels=list(items_means.index),
           leaf_rotation=90, leaf_font_size=10)
plt.show()

#### K-Means
sil = []
for i in np.arange(2,10):
    km = KMeans(n_clusters=i, random_state=2022)
    km.fit(i_scaled)
    labels = km.predict(i_scaled)
    score = silhouette_score(i_scaled, labels)
    sil.append(score)
    print("K=",i," Score=", score)
    
Ks = np.arange(2,10)
i_max = np.argmax(sil)
best_k = Ks[i_max]
print("Best K =", best_k)

################### PCA #############################
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

train = pd.read_csv("processed_train.csv")
X = train.drop(['Item_Identifier','Item_Outlet_Sales',
                  'Outlet_Identifier'],
                 axis=1)
dum_X = pd.get_dummies(X, drop_first=True)

pca = PCA()
scaler = StandardScaler()
pipe = Pipeline([('Scaling',scaler),('PCA',pca)])
prin_comp = pipe.fit_transform(dum_X)

ys = np.cumsum(pca.explained_variance_ratio_*100)
xs = np.arange(1,28)
plt.plot(xs, ys)
plt.title("Scree Plot")
plt.xlabel("Principal Componenents")
plt.ylabel("Cumulative %age variation explained")
plt.show()

pct = 85
print(pct,"% of variation is explanied by",np.sum(ys<=pct),"components")













