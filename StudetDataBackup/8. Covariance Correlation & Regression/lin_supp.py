import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

boston = pd.read_csv("Boston.csv")

X = boston.drop('medv', axis=1)
y = boston['medv']

X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    random_state=2022,
                                                    train_size=0.7)
lr = LinearRegression()
lr.fit(X_train,y_train)

y_pred = lr.predict(X_test)
print(r2_score(y_test, y_pred))

#### degree = 2
poly = PolynomialFeatures(degree=2)
poly.fit(X_train)
X_trn_poly = poly.transform(X_train)
X_tst_poly = poly.transform(X_test)

lr = LinearRegression()
lr.fit(X_trn_poly,y_train)

y_pred = lr.predict(X_tst_poly)
print(r2_score(y_test, y_pred))

#### degree = 3
poly = PolynomialFeatures(degree=3)
poly.fit(X_train)
X_trn_poly = poly.transform(X_train)
X_tst_poly = poly.transform(X_test)

lr = LinearRegression()
lr.fit(X_trn_poly,y_train)

y_pred = lr.predict(X_tst_poly)
print(r2_score(y_test, y_pred))


#### degree = 4
poly = PolynomialFeatures(degree=4)
poly.fit(X_train)
X_trn_poly = poly.transform(X_train)
X_tst_poly = poly.transform(X_test)

lr = LinearRegression()
lr.fit(X_trn_poly,y_train)

y_pred = lr.predict(X_tst_poly)
print(r2_score(y_test, y_pred))

###### Using Pipeline #############
from sklearn.pipeline import Pipeline
poly = PolynomialFeatures(degree=2)
lr = LinearRegression()
pipe = Pipeline([('Polynomial',poly),('LIN',lr)])

pipe.fit(X_train, y_train)

y_pred = pipe.predict(X_test)
print(r2_score(y_test, y_pred))


