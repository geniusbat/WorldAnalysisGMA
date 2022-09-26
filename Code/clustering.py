import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering, AffinityPropagation, OPTICS
import matplotlib.pylab as plt

processedDataDir = "ProcessedData"


#df2015 = pd.read_csv(processedDataDir+"/Happiness2017")
#dfGdp = pd.read_csv(processedDataDir+"/Gdp")

'''
print(df2015[df2015.isnull().any(axis=1)])

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

'''
def getClasses(year, show=False):
    df2015 = pd.read_csv(processedDataDir+"/Happiness"+year)
    dfGdp = pd.read_csv(processedDataDir+"/Gdp")
    #print(dfGdp[dfGdp.isna().any(axis=1)])
    #print(df2015[df2015.isna().any(axis=1)])
    listData = []
    for index, row in df2015.iterrows():
        element = []
        element.append(dfGdp.loc[dfGdp["Country"]==row["Country"]][year])
        aux = row.values.tolist()
        aux.pop(0)
        aux.pop(0)
        aux.pop(0)
        element.extend(aux)
        listData.append(element)

    data = np.array(listData, dtype=object)

    #clustering : AgglomerativeClustering = AgglomerativeClustering(n_clusters=7).fit(data)
    clustering = AffinityPropagation().fit(data)
    if show:
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
        showText = False
        for team in teams:
            teamData = teams[team]
            x = [data[3] for data in teamData]
            y = [data[0] for data in teamData]
            plt.scatter(x, y)
            if showText:
                for data in teamData:
                    plt.text(data[3],data[0],data[1])
        plt.show()
    return clustering.labels_

if __name__ == "__main__":
    getClasses("2019", True)