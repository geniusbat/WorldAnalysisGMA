import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.tree import _tree
from sklearn.cluster import AgglomerativeClustering, DBSCAN
import matplotlib.pylab as plt

def listData(df, year):
    listData=[]
    for index, row in df.iterrows():
        element = []
        element.append(dfGdp.loc[dfGdp["Country"]==row["Country"]][year])
        aux = row.values.tolist()
        aux.pop(0)
        aux.pop(0)
        aux.pop(0)
        element.extend(aux)
        listData.append(element)
    return np.array(listData, dtype=object)

def get_rules(tree : tree.DecisionTreeClassifier, feature_names, class_names):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]

    paths = []
    path = []
    
    def recurse(node, path, paths):
        
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            p1, p2 = list(path), list(path)
            p1 += [f"({name} <= {np.round(threshold, 3)})"]
            recurse(tree_.children_left[node], p1, paths)
            p2 += [f"({name} > {np.round(threshold, 3)})"]
            recurse(tree_.children_right[node], p2, paths)
        else:
            path += [(tree_.value[node], tree_.n_node_samples[node])]
            paths += [path]
            
    recurse(0, path, paths)

    # sort by samples count
    samples_count = [p[-1][1] for p in paths]
    ii = list(np.argsort(samples_count))
    paths = [paths[i] for i in reversed(ii)]
    
    rules = []
    for path in paths:
        rule = "if "
        
        for p in path[:-1]:
            if rule != "if ":
                rule += " and "
            rule += str(p)
        rule += " then "
        if class_names is None:
            rule += "response: "+str(np.round(path[-1][0][0][0],3))
        else:
            classes = path[-1][0][0]
            l = np.argmax(classes)
            rule += f"class: {class_names[l]} (proba: {np.round(100.0*classes[l]/np.sum(classes),2)}%)"
        rule += f" | based on {path[-1][1]:,} samples"
        rules += [rule]
        
    return rules

processedDataDir = "ProcessedData"
availableYears = ["2015", "2016", "2017", "2018", "2019"]

df2015 = pd.read_csv(processedDataDir+"/Happiness2015")
df2016 = pd.read_csv(processedDataDir+"/Happiness2016") 
df2017 = pd.read_csv(processedDataDir+"/Happiness2017") 
df2018 = pd.read_csv(processedDataDir+"/Happiness2018") 
df2019 = pd.read_csv(processedDataDir+"/Happiness2019") 
dfGdp = pd.read_csv(processedDataDir+"/Gdp")

dfs = [df2015, df2016, df2017, df2018, df2019]

for index in range(len(dfs)):
    df = dfs[index]
    year = availableYears[index]
    data = listData(df, year)
    clustering : AgglomerativeClustering = AgglomerativeClustering(n_clusters=7).fit(data)
    labels = clustering.labels_
    model = tree.DecisionTreeClassifier()
    model = model.fit(data, labels)
    rules = get_rules(model,["gdp","Life Expentancy","Freedom","Corruption","Generosity"], ["0","1","2","3","4","5","6"])
    grouping = {}
    for classNum in ["0","1","2","3","4","5","6"]:
        text = "then class: {}".format(classNum)
        grouping[classNum]=[]
        for rule in rules:
            if text in rule:
                grouping[classNum].append(rule)

    for el in grouping:
        print(grouping[el])