import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir(r"C:\Adv Analytics\Datasets")
cars93 = pd.read_csv("Cars93.csv")

#joint plot demo
sns.jointplot(data=cars93, x = "EngineSize", y="MPG.highway")
plt.xlabel("Engine Size")
plt.ylabel("Milage on Highway")
plt.show()
