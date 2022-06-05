import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1
space = pd.read_csv("space.csv", delimiter = ';')

empresasUsa = space[space['Location'].str.contains('USA')]
empresasChina = space[space['Location'].str.contains('China')]

empresasUsaUnique = empresasUsa["Company Name"].unique()
empresasChinaUnique = empresasChina["Company Name"].unique()

NumUsa = len(empresasUsaUnique)
NumChina = len(empresasChinaUnique)

plt.title("Space companies of USA and China")
plt.bar(x = [0,1], height = [NumUsa, NumChina], color = ['green', 'red'])
plt.ylabel("Companies numbers")
plt.xlabel("Countries")
plt.xticks(ticks=[0,1], labels=["USA", "China"])
plt.show()


#2
paises = pd.read_csv("paises.csv", delimiter = ';')

BirthRate = paises.loc[paises["Region"].str.contains("NORTHERN AMERICA"), ["Country", "Birthrate"]]
DeathRate = paises.loc[paises["Region"].str.contains("NORTHERN AMERICA"), ["Country", "Deathrate"]]

plt.title("Northern America countries Birthrate vs Deathrate")
plt.xlabel("Countries")
plt.ylabel("Tax of Birthrate and Deathrate")
plt.plot(np.arange(len(BirthRate)), BirthRate["Birthrate"], color = "green", marker= "v", linestyle = ":", label = "Birthrate")
plt.plot(np.arange(len(DeathRate)), DeathRate["Deathrate"], color = "red", marker= "x", linestyle = ":", label = "Deathrate")
plt.xticks(ticks = np.arange(len(BirthRate)), labels=BirthRate["Country"])
plt.legend()
plt.show()