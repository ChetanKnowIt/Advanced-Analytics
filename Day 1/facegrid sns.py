import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir(r"C:\Adv Analytics\Datasets")
cars93 = pd.read_csv("Cars93.csv")

g = sns.FacetGrid(cars93, col = "AirBags")
g = g.map(plt.scatter, "EngineSize", "MPG.highway")
plt.show()
