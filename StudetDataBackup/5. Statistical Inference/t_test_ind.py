import pandas as pd
from scipy.stats import bartlett, ttest_ind

co2 = pd.read_csv("CO2.csv")

chilled = co2[co2['Treatment']=='chilled']
unchilled = co2[co2['Treatment']=='nonchilled']

bartlett(chilled['uptake'], unchilled['uptake'])

ttest_ind(chilled['uptake'], unchilled['uptake'],
          equal_var=True)

################# Puromycin ####################
puromycin = pd.read_csv("Puromycin.csv")

treated = puromycin[puromycin['state']=='treated']
untreated = puromycin[puromycin['state']=='untreated']

bartlett(treated['rate'], untreated['rate'])

ttest_ind(treated['rate'], untreated['rate'],
          equal_var=True)

############ Soporific ######################
soporific = pd.read_csv("Soporific.csv")

bartlett(soporific['Drug A'], soporific['Drug B'])

ttest_ind(soporific['Drug A'], soporific['Drug B'],
          equal_var=True)

########## Housing ############################
housing = pd.read_csv("Housing.csv")

preferred = housing[housing['prefarea']=="yes"]
non_pref = housing[housing['prefarea']=="no"]

bartlett(preferred['price'], non_pref['price'])

ttest_ind(preferred['price'], non_pref['price'],
          alternative="greater",
          equal_var=False)

housing.groupby('prefarea')['price'].mean()

# airco
ac = housing[housing['airco']=='yes']
non_ac = housing[housing['airco']=='no']

bartlett(ac['price'], non_ac['price'])

ttest_ind(ac['price'], non_ac['price'],
          alternative="greater",
          equal_var=False)

housing.groupby('airco')['price'].mean()

################ Car93 #######################
cars93 = pd.read_csv("Cars93.csv")

# Origin
usa = cars93[cars93['Origin']=="USA"]
non_usa = cars93[cars93['Origin']=="non-USA"]

bartlett(usa['Price'], non_usa['Price'])

ttest_ind(usa['Price'], non_usa['Price'],
          equal_var=False)

# Conclusion: Means of prices may be equal for different origins

# Transmission
man_trans = cars93[cars93['Man.trans.avail']=="Yes"]
auto_trans = cars93[cars93['Man.trans.avail']=="No"]

bartlett(man_trans['Price'], auto_trans['Price'])

ttest_ind(man_trans['Price'], auto_trans['Price'],
          equal_var=True)



