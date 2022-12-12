import pandas as pd
from scipy.stats import bartlett, ttest_ind

co2 = pd.read_csv("CO2.csv")

chilled = co2[co2['Treatment']=='chilled']
unchilled = co2[co2['Treatment']=='nonchilled']

bartlett(chilled['uptake'], unchilled['uptake'])
