import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

milk = pd.read_csv("milk.csv",index_col=0)
scaler = StandardScaler()
scaler.fit(milk)
milkscaled=scaler.transform(milk)

pca = PCA()
prin_comp = pca.fit_transform(milkscaled)
print(milk.shape)
print(prin_comp.shape)

pd_PC = pd.DataFrame(prin_comp, columns=['PC1','PC2','PC3','PC4','PC5'])

pd_PC.var() # or
print(pca.explained_variance_)
# %age variation explained
print(pca.explained_variance_ratio_*100)

### Scree Plot
ys = np.cumsum(pca.explained_variance_ratio_*100)
xs = np.arange(1,6)
plt.plot(xs, ys)
plt.title("Scree Plot")
plt.xlabel("Principal Componenents")
plt.ylabel("Cumulative %age variation explained")
plt.show()

############ biplot ##############
from pca import pca
milk = pd.read_csv("milk.csv",index_col=0)
scaler = StandardScaler()
scaler.fit(milk)
milkscaled=scaler.transform(milk)
milkscaled = pd.DataFrame(milkscaled, 
                          columns=milk.columns, index=milk.index)

model = pca()
results = model.fit_transform(milkscaled)
fig, ax = model.biplot(label=True,legend=False)

######## iris ####################
import seaborn as sns
iris = pd.read_csv("iris.csv")

pca = PCA()
scaler = StandardScaler()
iris_num = iris.drop('Species', axis=1)
iris_scaled = scaler.fit_transform(iris_num)
prin_comp = pca.fit_transform(iris_scaled)

# or
# Using pipeline
from sklearn.pipeline import Pipeline
pca = PCA()
scaler = StandardScaler()
pipe = Pipeline([('Scaling',scaler),('PCA',pca)])
prin_comp = pipe.fit_transform(iris_num)

# %age variation explained
print(pca.explained_variance_ratio_*100)

pd_PC = pd.DataFrame(prin_comp, 
                     columns=['PC1','PC2','PC3','PC4'])
pd_PC['Species'] = iris['Species']


sns.scatterplot(data=pd_PC,x='PC1',
                y='PC2', hue= 'Species')
plt.title("Scatter Plot")
plt.show()

############### Wine ###############
wine = pd.read_csv("wine.csv")
wine_num = wine.drop('Class', axis=1)

pca = PCA()
scaler = StandardScaler()
pipe = Pipeline([('Scaling',scaler),('PCA',pca)])
prin_comp = pipe.fit_transform(wine_num)

# %age variation explained
print(pca.explained_variance_ratio_*100)

pd_PC = pd.DataFrame(prin_comp, 
                     columns=['PC'+str(i) for i in np.arange(1,14)])
pd_PC['Class'] = wine['Class']
pd_PC['Class'] = pd_PC['Class'].astype('category')

sns.scatterplot(data=pd_PC,x='PC1',
                y='PC2', hue= 'Class')
plt.title("Scatter Plot")
plt.show()

##################### Protein ######################
protein = pd.read_csv("Protein.csv", index_col=0)


pca = PCA()
scaler = StandardScaler()
pipe = Pipeline([('Scaling',scaler),('PCA',pca)])
prin_comp = pipe.fit_transform(protein)

# %age variation explained
print(pca.explained_variance_ratio_*100)

ys = np.cumsum(pca.explained_variance_ratio_*100)
xs = np.arange(1,10)
plt.plot(xs, ys)
plt.title("Scree Plot")
plt.xlabel("Principal Componenents")
plt.ylabel("Cumulative %age variation explained")
plt.show()

prot_scaled = scaler.fit_transform(protein)
prot_scaled = pd.DataFrame(prot_scaled, 
                          columns=protein.columns, 
                          index=protein.index)
from pca import pca
model = pca()
results = model.fit_transform(prot_scaled)
fig, ax = model.biplot(label=True,legend=False)

## Clustering
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
# Finding the best cluster based on Silhouette
sil = []
for i in np.arange(2,10):
    km = KMeans(n_clusters=i, random_state=2022)
    km.fit(prot_scaled)
    labels = km.predict(prot_scaled)
    sil.append(silhouette_score(prot_scaled, labels))

Ks = np.arange(2,10)
i_max = np.argmax(sil)
best_k = Ks[i_max]
print("Best K =", best_k)

# Generating the labels corressponding to best K
km = KMeans(n_clusters=best_k, random_state=2022)
km.fit(prot_scaled)
labels = km.predict(prot_scaled)

pd_PC = pd.DataFrame(prin_comp, 
                     columns=['PC'+str(i) for i in np.arange(1,10)])
pd_PC['Cluster'] = labels

pd_PC['Cluster'] = pd_PC['Cluster'].astype('category')
sns.scatterplot(data=pd_PC,x='PC1',
                y='PC2', hue= 'Cluster')
plt.title("Scatter Plot")
plt.show()

