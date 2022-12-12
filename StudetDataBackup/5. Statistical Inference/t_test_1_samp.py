import pandas as pd
from scipy.stats import ttest_1samp

pg = pd.read_csv("PlantGrowth.csv")

ttest_1samp(pg['weight'], popmean=6, alternative="two-sided")

ttest_1samp(pg['weight'], popmean=6, alternative="greater")

ttest_1samp(pg['weight'], popmean=6, alternative="less")

############## CO2 ##################

co2 = pd.read_csv("CO2.csv")

ttest_1samp(co2['uptake'], popmean=30, alternative="less")

# Conclusion: Pop mean uptake may be less than 30.

######### Indometh ################
indometh = pd.read_csv("Indometh.csv")
ttest_1samp(indometh['conc'], popmean=0.3, alternative="greater")
# Conclusion: Plasma Conc may be greater than 0.3.
