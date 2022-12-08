import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import os
os.chdir(r"C:\Training\Academy\Statistics (Python)\Datasets")

cars93 = pd.read_csv("Cars93.csv")
print(cars93.info())

cts = cars93['Type'].value_counts()
cts.plot(kind='bar')
plt.show()

# Matplotlib
plt.bar(cts.index, cts)
plt.show()

cts = cars93.groupby('AirBags')['Price'].mean()
plt.bar(cts.index, cts)
plt.ylabel("Mean Price")
plt.show()

# Seaborn
cts1 = cts.reset_index()
cts1.columns = ['Type', 'Count']
sns.barplot(data=cts1, x='Type', y='Count')
plt.show()

cts = cars93.groupby('AirBags')['Price'].mean()
cts1 = cts.reset_index()
sns.barplot(data=cts1, x='AirBags', y='Price')
plt.ylabel("Mean Price")
plt.show()

#### Histogram
cars93['Price'].plot(kind='hist', bins=15)
plt.show()

# Matplotlib
plt.hist(cars93['Price'], bins=15)
plt.show()

# Seaborn
sns.histplot(data=cars93, x='Price', bins=8)
plt.show()

#### Density Plot / Distribution Plot
cars93['Price'].plot(kind='kde')
plt.show()

# Seaborn
sns.kdeplot(data=cars93, x='Price')
plt.show()

#### Scatter Plot
cars93.plot(kind="scatter", x="EngineSize", y="MPG.highway")
plt.title("Scatter Plot")
plt.xlabel("Engine Size")
plt.ylabel("Milage on Highway")
plt.show()

# Matplotlib
plt.scatter(cars93['EngineSize'],cars93["MPG.highway"])
plt.title("Scatter Plot")
plt.xlabel("Engine Size")
plt.ylabel("Milage on Highway")
plt.show()

no_bags = cars93[cars93["AirBags"] == "None"]
plt.scatter(no_bags['EngineSize'],no_bags["MPG.highway"], 
            label="No Airbags", color="red")
driver = cars93[cars93["AirBags"] == "Driver only"]
plt.scatter(driver['EngineSize'],driver["MPG.highway"], 
            label="Driver Only", color="blue")
d_p = cars93[cars93["AirBags"] == "Driver & Passenger"]
plt.scatter(d_p['EngineSize'],d_p["MPG.highway"], 
            label="Driver & Passenger", color="magenta")
plt.legend(loc="best")
plt.title("Scatter Plot")
plt.xlabel("Engine Size")
plt.ylabel("Milage on Highway")
plt.show()



# seaborn
sns.scatterplot(data=cars93,x="EngineSize",y="MPG.highway")
plt.title("Scatter Plot")
plt.xlabel("Engine Size")
plt.ylabel("Milage on Highway")
plt.show()

sns.scatterplot(data=cars93,x="EngineSize",
                y="MPG.highway", hue="AirBags")
plt.title("Scatter Plot")
plt.xlabel("Engine Size")
plt.ylabel("Milage on Highway")
plt.show()

#### Box Plot
cars93["Price"].plot(kind="box")
plt.title("Box Plot")
plt.show()

cars93["EngineSize"].plot(kind="box")
plt.title("Box Plot")
plt.show()

cars93["Horsepower"].plot(kind="box")
plt.title("Box Plot")
plt.show()

# Matplotlib
plt.boxplot(cars93["Price"])
plt.title("Box Plot")
plt.show()

# Seaborn
sns.boxplot(y='Price', data=cars93)
plt.show()

sns.boxplot(x="AirBags",y='Price', data=cars93)
plt.show()

# =============================================================================
# iris=pd.read_csv("iris.csv")
# iris['Sepal.Width'].plot(kind="box")
# plt.title("Box Plot")
# plt.show()
# =============================================================================

### Facet Grid
g = sns.FacetGrid(cars93, col="AirBags")
g = g.map(plt.scatter, "EngineSize",
          "MPG.highway")
plt.show()

### SubPlot
plt.subplot(1,2,1)
sns.boxplot(y='Price', data=cars93)
plt.title("Box Plot")

plt.subplot(1,2,2)
sns.histplot(data=cars93, x='Price', bins=8)
plt.title("Histogram")

plt.tight_layout()
plt.show()



plt.subplot(2,2,1)
sns.boxplot(y='Price', data=cars93)
plt.title("Box Plot")

plt.subplot(2,2,2)
sns.histplot(data=cars93, x='Price', bins=8)
plt.title("Histogram")

plt.subplot(2,2,3)
sns.scatterplot(data=cars93,x="EngineSize",y="MPG.highway")
plt.title("Scatter Plot")
plt.xlabel("Engine Size")
plt.ylabel("Milage on Highway")

plt.subplot(2,2,4)
cts = cars93["AirBags"].value_counts()
cts1 = cts.reset_index()
cts1.columns = ['AirBags', 'Count']
sns.barplot(data=cts1, x='AirBags', y='Count')
plt.xticks(rotation=10)
plt.tight_layout()
plt.show()

#### Joint Plot
sns.jointplot(data=cars93,x="EngineSize",y="MPG.highway")
plt.xlabel("Engine Size")
plt.ylabel("Milage on Highway")
plt.show()

