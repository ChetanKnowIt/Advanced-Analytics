import pandas as pd
import numpy as np
import os
os.chdir(r"C:\Training\Academy\Statistics (Python)\Datasets")

X1 = np.array(["A",'A','A','B','B','B','C','C'])
X2 = np.array(['P','Q','P','Q','P','P','Q','Q'])

## Crosstab
pd.crosstab(index=X1, columns=X2)

# Joint Probability Distribution
pd.crosstab(index=X1, columns=X2, normalize='all', margins=True)

# Conditional Probability Distributions for Rows
pd.crosstab(index=X1, columns=X2, normalize='index', margins=True)

# Conditional Probability Distributions for Columns
pd.crosstab(index=X1, columns=X2,normalize='columns',margins=True)

##### cars93
cars93 = pd.read_csv('cars93.csv')

cars93['Type'].value_counts(normalize=True)

cars93['AirBags'].value_counts(normalize=True)

pd.crosstab(cars93['Type'], cars93['AirBags'],
            normalize='all', margins=True)

pd.crosstab(cars93['Type'], cars93['AirBags'],
            normalize='columns', margins=True)
