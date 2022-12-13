import pandas as pd

from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

###### Yield ########
agr = pd.read_csv("Yield.csv")
agr_ols = ols('Yield ~ Treatments', data=agr).fit()
table = anova_lm(agr_ols, typ=2)
print(table)

######## Post Hoc Tukey HSD ################
compare = pairwise_tukeyhsd(agr['Yield'], 
                            agr['Treatments'], alpha=0.05)

dd = pd.DataFrame(compare._results_table.data)
dd

agr.groupby('Treatments')['Yield'].mean()

############ Plant Growth ################

pg = pd.read_csv("PlantGrowth.csv")

pg_ols = ols('weight ~ group', data=pg).fit()
table = anova_lm(pg_ols, typ=2)
print(table)

compare = pairwise_tukeyhsd(pg['weight'], 
                            pg['group'], alpha=0.05)

dd = pd.DataFrame(compare._results_table.data)
dd


