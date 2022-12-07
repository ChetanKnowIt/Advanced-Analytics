import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir(r"C:\Adv Analytics\Datasets")
cars93 = pd.read_csv("Cars93.csv")
no_bags = cars93[cars93["AirBags"] == "None"]
plt.scatter(no_bags['EngineSize'], no_bags["MPG.highway"], label="No Airbags")
driver = cars93[cars93["AirBags"] == "Driver only"]
plt.scatter(driver['EngineSize'], driver["MPG.highway"], label="Driver only")
d_p = cars93[cars93["AirBags"] == "Driver & Passenger"]
plt.scatter(d_p['EngineSize'], d_p["MPG.highway"], label="Driver & Passenger")
plt.legend(loc = "best")
plt.title("Scatter Plot")
plt.xlabel("Engine Size")
plt.ylabel('Milage on Highway')
plt.show()
