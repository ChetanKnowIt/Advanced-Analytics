import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

pizza = pd.read_csv("pizza.csv")

lr = LinearRegression()

X = pizza[['Promote']]
y = pizza['Sales']

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
print(poly.get_feature_names_out())

lr.fit(X_poly,y)
print(lr.intercept_)
print(lr.coef_)
# yi^
y_pred = lr.predict(X_poly)

print(r2_score(y, y_pred))

############## insure auto #####################
insure = pd.read_csv("Insure_auto.csv")

X = insure[['Home','Automobile']]
y = insure['Operating_Cost']

poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)
print(poly.get_feature_names_out())

lr.fit(X_poly,y)
print(lr.intercept_)
print(lr.coef_)
# yi^
y_pred = lr.predict(X_poly)

print(r2_score(y, y_pred))

############ Boston #######################
boston = pd.read_csv("Boston.csv")

X = boston.drop('medv', axis=1)
y = boston['medv']
lr = LinearRegression()
lr.fit(X,y)
print(lr.intercept_)
print(lr.coef_)
y_pred = lr.predict(X)
print(r2_score(y, y_pred))

# deg = 2
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
print(poly.get_feature_names_out())

lr.fit(X_poly,y)
print(lr.intercept_)
print(lr.coef_)
# yi^
y_pred = lr.predict(X_poly)

print(r2_score(y, y_pred))

# deg = 3
poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)
print(poly.get_feature_names_out())

lr.fit(X_poly,y)
print(lr.intercept_)
print(lr.coef_)
# yi^
y_pred = lr.predict(X_poly)

print(r2_score(y, y_pred))
