import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering, DBSCAN
import matplotlib.pylab as plt

processedDataDir = "ProcessedData"

df2015 = pd.read_csv(processedDataDir+"/Happiness2015") 
dfGdp = pd.read_csv(processedDataDir+"/Gdp")

listData = []
for index, row in df2015.iterrows():
    element = []
    element.append(dfGdp.loc[dfGdp["Country"]==row["Country"]]["2015"])
    aux = row.values.tolist()
    aux.pop(0)
    aux.pop(0)
    aux.pop(0)
    element.extend(aux)
    listData.append(element)

data = np.array(listData, dtype=object)

clustering : AgglomerativeClustering = AgglomerativeClustering(n_clusters=7).fit(data)
#clustering = DBSCAN().fit(data)

print(clustering.labels_)

teams = {}

for ind in range(len(clustering.labels_)):
    label = clustering.labels_[ind]
    aux : list = df2015.iloc[ind].values.tolist()
    aux.pop(0)
    aux.insert(0,dfGdp.loc[dfGdp["Country"]==aux[0]]["2015"].values[0])
    if label in teams:
        teams[label].append(aux)
    else:
        teams[label] = [aux]

plt.figure()
for team in teams:
    teamData = teams[team]
    x = [data[3] for data in teamData]
    y = [data[0] for data in teamData]
    plt.scatter(x, y)
    for data in teamData:
        plt.text(data[3],data[0],data[1])
plt.show()
