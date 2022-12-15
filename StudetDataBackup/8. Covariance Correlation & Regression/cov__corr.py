import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

a = np.array([2,5,6,7,10])
b = np.array([30, 24, 20, 17, 7])
# Variance Covariance Matrix
np.cov(a,b)

pizza = pd.read_csv("pizza.csv")

pizza['Promote'].cov(pizza['Sales'])

# Variance Covariance Matrix
np.cov(pizza['Promote'], pizza['Sales'])
pizza.cov()

# Correlation
pizza['Promote'].corr(pizza['Sales'])

pizza['Promote'].corr(pizza['Promote'])

# Correlation matrix
pizza.corr()
np.corrcoef(pizza['Promote'], pizza['Sales'])

# scatter plot
sns.scatterplot(data=pizza, x='Promote', y='Sales')
plt.show()

############## insure auto #####################
insure = pd.read_csv("Insure_auto.csv")
insure.corr()

sns.heatmap(
    insure.corr(),
    xticklabels=insure.corr().columns, 
    yticklabels=insure.corr().columns, 
    annot=True)
plt.show()

sns.pairplot(insure,diag_kind='kde')
plt.show()

############## iris ##################
iris = pd.read_csv("iris.csv")

sns.heatmap(
    iris.corr(),
    xticklabels=iris.corr().columns, 
    yticklabels=iris.corr().columns, 
    annot=True)
plt.show()

############ Boston #################
boston = pd.read_csv("Boston.csv")

sns.heatmap(
    boston.corr(),
    xticklabels=boston.corr().columns, 
    yticklabels=boston.corr().columns, 
    annot=False)
plt.show()
