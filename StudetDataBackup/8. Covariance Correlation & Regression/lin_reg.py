import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

pizza = pd.read_csv("pizza.csv")

lr = LinearRegression()

X = pizza[['Promote']]
y = pizza['Sales']

lr.fit(X,y)
print(lr.intercept_)
print(lr.coef_)

# yi^
y_pred = lr.predict(X)

print(r2_score(y, y_pred))
# numerator = np.sum((y - y_pred)**2)
# denominator = np.sum((y - y.mean())**2)
# 1 - (numerator/denominator)

############## insure auto #####################
insure = pd.read_csv("Insure_auto.csv")

X = insure[['Home']]
y = insure['Operating_Cost']
lr.fit(X,y)
y_pred = lr.predict(X)
print(r2_score(y, y_pred))

X = insure[['Automobile']]
y = insure['Operating_Cost']
lr.fit(X,y)
y_pred = lr.predict(X)
print(r2_score(y, y_pred))

X = insure[['Home','Automobile']]
y = insure['Operating_Cost']
lr.fit(X,y)
print(lr.intercept_)
print(lr.coef_)
y_pred = lr.predict(X)
print(r2_score(y, y_pred))

############ Boston #######################
boston = pd.read_csv("Boston.csv")
X = boston.iloc[:,:-1]
# or
X = boston.drop('medv', axis=1)
y = boston['medv']
lr.fit(X,y)
print(lr.intercept_)
print(lr.coef_)
y_pred = lr.predict(X)
print(r2_score(y, y_pred))




