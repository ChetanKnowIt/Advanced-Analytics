import pandas as pd
from scipy.stats import chi2_contingency

housing = pd.read_csv("Housing.csv")

ctab = pd.crosstab(housing['prefarea'], housing['gashw'])
test_statistic, p_value, df, expected_frequencies = chi2_contingency(ctab)
print(p_value)
