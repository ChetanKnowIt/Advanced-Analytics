import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
import statsmodels.api as sm

pizza = pd.read_csv("pizza.csv")

X = pizza['Promote']
X = sm.add_constant(X)
y = pizza['Sales']
model = sm.OLS(y,X)
results = model.fit()

print(results.params)
print(results.summary())

### Credit Approval
import os
os.chdir(r"C:\Training\Academy\Business Analytics 3e Resources\Excel Datasets\eba3e_datasets_xls")
cred = pd.read_excel("CreditApprovalDecisions.xlsx",sheet_name="Data",
                     usecols="A:F",skiprows=2)
X = cred[['Years of Credit History',
          'Revolving Balance', 'Revolving Utilization']]
y = cred['Credit Score']

X = sm.add_constant(X)

model = sm.OLS(y,X)
results = model.fit()

print(results.params)
print(results.summary())



