import numpy as np
import pandas as pd

x = np.array([0, 1, 2, 3, 4, 5])
p = np.array([0.3, 0.2, 0.15, 0.1, 0.13, 0.12])
cp = np.cumsum(p)

rnd = np.array([0.33,0.98,0.38,0.22,0.52,0.49,0.51])

prob = 0.22
i_sim = np.sum(cp<prob)
x[i_sim]

simulated = []
for prob in rnd:
   i_sim = np.sum(cp<prob)
   simulated.append(x[i_sim]) 

########### Supply ################
x = np.array([10, 20, 30, 40, 50])
c = np.array([40, 50, 190, 150, 70])
p = c/500
cp = np.cumsum(p)

rnd_supp = np.array([0.34,0.9,0.22,0.45,0.68])

sim_supp = []
for prob in rnd_supp:
   i_sim = np.sum(cp<prob)
   sim_supp.append(x[i_sim]) 

############ Demand ##############

x = np.array([10, 20, 30, 40, 50])
c = np.array([50,110,200,100,40])
p = c/500
cp = np.cumsum(p)

rnd_dem = np.array([0.98,0.35,0.89,0.3,0.48])

sim_dem = []
for prob in rnd_dem:
   i_sim = np.sum(cp<prob)
   sim_dem.append(x[i_sim]) 

df = pd.DataFrame({'Supply Rnd':rnd_supp,
                   'Sim Supply':sim_supp,
                   'Demand Rnd':rnd_dem,
                   'Sim Demand':sim_dem})

df['Sold Qty'] = np.minimum(df['Sim Supply'],
                            df['Sim Demand'])
df['Wasted Qty'] = df['Sim Supply'] - df['Sold Qty']
df['Profit'] = df['Sold Qty']*10
df['Loss'] = df['Wasted Qty']*8
df['Net P/L'] = df['Profit'] - df['Loss']