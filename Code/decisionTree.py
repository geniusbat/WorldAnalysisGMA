import numpy as np
import pandas as pd
from sklearn import tree

import matplotlib.pylab as plt

processedDataDir = "ProcessedData"

df2015 = pd.read_csv(processedDataDir+"/Happiness2015") 
dfGdp = pd.read_csv(processedDataDir+"/Gdp")

'''
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

labels = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 3, 5, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2,
2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

labels = np.array(labels)
data = np.array(listData, dtype=object)

model = tree.DecisionTreeClassifier()
model = model.fit(data, labels)


plt.figure(figsize=(10,10))
_ = tree.plot_tree(model, class_names=["0","1","2","3","4","5","6"], feature_names=["gdp","Score","Life Expentancy","Freedom","Corruption","Generosity"],
                   filled=True)
plt.show()
'''

listData = []
for index, row in df2015.iterrows():
    element = []
    element.append(dfGdp.loc[dfGdp["Country"]==row["Country"]]["2015"])
    aux = row.values.tolist()
    aux.pop(0)
    aux.pop(0)
    aux.pop(0)
    aux.pop(0)
    element.extend(aux)
    listData.append(element)

labels = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 3, 5, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2,
2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

labels = np.array(labels)
data = np.array(listData, dtype=object)

model = tree.DecisionTreeClassifier()
model = model.fit(data, labels)


plt.figure(figsize=(25,25), dpi=150)
_ = tree.plot_tree(model, class_names=["0","1","2","3","4","5","6"], feature_names=["gdp","Life Expentancy","Freedom","Corruption","Generosity"],
                   filled=True)
plt.show()