import pandas as pd
from scipy.stats import ttest_rel

anorexia = pd.read_csv("anorexia.csv")

cont = anorexia[anorexia['Treat']=="Cont"]
ttest_rel(cont['Prewt'], cont['Postwt'], 
          alternative="less")

cbt = anorexia[anorexia['Treat']=="CBT"]
ttest_rel(cbt['Prewt'], cbt['Postwt'], 
          alternative="less")

ft = anorexia[anorexia['Treat']=="FT"]
ttest_rel(ft['Prewt'], ft['Postwt'], 
          alternative="less")

############## Rheumatic #####################
rhum = pd.read_csv("Rheumatic.csv")
ttest_rel(rhum['Before'], rhum['After'], 
          alternative="less")
# or
ttest_rel(rhum['After'], rhum['Before'], 
          alternative="greater")


################ Plaque ##################
plaque = pd.read_csv("Plaque.csv")

plaq_pivot = pd.pivot_table(plaque, 
                            index=['Id','product'],
                            columns='trt',
                            values='score')

plaq_pivot = plaq_pivot.reset_index()

P1 = plaq_pivot[plaq_pivot['product']=="P1"]
ttest_rel(P1['Before'], P1['After'], 
          alternative="greater")

P2 = plaq_pivot[plaq_pivot['product']=="P2"]
ttest_rel(P2['Before'], P2['After'], 
          alternative="greater")

P3 = plaq_pivot[plaq_pivot['product']=="P3"]
ttest_rel(P3['Before'], P3['After'], 
          alternative="greater")





