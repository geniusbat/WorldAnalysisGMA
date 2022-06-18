from typing import Dict
import numpy as np
import pandas as pd

def substituteColumns(df:pd.DataFrame, columns:dict):
    for column, names in columns.items():
        for name in names:
            if name in df.columns.to_list():
                df = df.rename({name:column},axis=1)
    return df

def deleteUnusedColumns(df:pd.DataFrame, columns:dict):
    for columnName in list(df.columns.values):
        if columnName not in list(columns.keys()):
            df = df.drop(columnName,axis=1)
    return df

unprocessedDataDir = "UnprocessedData"
processedDataDir = "ProcessedData"
df2015 = pd.read_csv(unprocessedDataDir+"/HappinessReport/2015.csv")
df2016 = pd.read_csv(unprocessedDataDir+"/HappinessReport/2016.csv")
df2017 = pd.read_csv(unprocessedDataDir+"/HappinessReport/2017.csv")
df2018 = pd.read_csv(unprocessedDataDir+"/HappinessReport/2018.csv")
df2019 = pd.read_csv(unprocessedDataDir+"/HappinessReport/2019.csv")
happinessCountriesSeries = set(df2015["Country"]).intersection(set(df2016["Country"])).intersection(set(df2017["Country"])).intersection(set(df2018["Country or region"])).intersection(set(df2019["Country or region"]))

dfGdp = pd.read_csv(unprocessedDataDir+"/WorldGDP/gdp.csv")

countriesAvailable = list(set(happinessCountriesSeries).intersection(set(dfGdp["Country Name"])))
availableYears = ["2015", "2016", "2017", "2018", "2019"]
requiredColumns = {
    "Country": ["Country", "Country or region"],
    "Rank": ["Happiness Rank", "Overall rank", "Happiness.Rank"],
    "Score": ["Happiness Score", "Score", "Happiness.Score"],
    "Life Expentancy" : ["Health (Life Expectancy)", "Healthy life expectancy", "Health..Life.Expectancy"],
    "Generosity" : ["Generosity"],
    "Corruption" : ["Trust (Government Corruption)", "Perceptions of corruption", "Trust..Government.Corruption"],
    "Freedom" : ["Freedom", "Freedom to make life choices"]
}



newDf2015 = substituteColumns(df2015, requiredColumns); newDf2015 = newDf2015[(newDf2015["Country"].isin(countriesAvailable))]; newDf2015 = deleteUnusedColumns(newDf2015, requiredColumns); newDf2015 = newDf2015.reindex(columns=["Country","Rank","Score","Life Expentancy","Freedom","Corruption","Generosity"])
newDf2016 = substituteColumns(df2016, requiredColumns); newDf2016 = newDf2016[(newDf2016["Country"].isin(countriesAvailable))]; newDf2016 = deleteUnusedColumns(newDf2016, requiredColumns); newDf2016 = newDf2016.reindex(columns=["Country","Rank","Score","Life Expentancy","Freedom","Corruption","Generosity"])
newDf2017 = substituteColumns(df2017, requiredColumns); newDf2017 = newDf2017[(newDf2017["Country"].isin(countriesAvailable))]; newDf2017 = deleteUnusedColumns(newDf2017, requiredColumns); newDf2017 = newDf2017.reindex(columns=["Country","Rank","Score","Life Expentancy","Freedom","Corruption","Generosity"])
newDf2018 = substituteColumns(df2018, requiredColumns); newDf2018 = newDf2018[(newDf2018["Country"].isin(countriesAvailable))]; newDf2018 = deleteUnusedColumns(newDf2018, requiredColumns); newDf2018 = newDf2018.reindex(columns=["Country","Rank","Score","Life Expentancy","Freedom","Corruption","Generosity"])
newDf2019 = substituteColumns(df2019, requiredColumns); newDf2019 = newDf2019[(newDf2019["Country"].isin(countriesAvailable))]; newDf2019 = deleteUnusedColumns(newDf2019, requiredColumns); newDf2019 = newDf2019.reindex(columns=["Country","Rank","Score","Life Expentancy","Freedom","Corruption","Generosity"])
newDfGdp = dfGdp[dfGdp["Country Name"].isin(countriesAvailable)]
newDfGdp = newDfGdp.rename({"Country Name":"Country"},axis=1)
newDfGdp = newDfGdp.drop("Code",axis=1)
#Erase unseen years
for column in newDfGdp.columns:
    if column!="Country":
        if column not in availableYears:
            newDfGdp = newDfGdp.drop(column,axis=1)
#Normalize
maxVal = 0
minVal = None
for year in availableYears:
    bigVal = newDfGdp.loc[newDfGdp[year].idxmax()][year]
    smallVal = newDfGdp.loc[newDfGdp[year].idxmin()][year]
    if bigVal > maxVal:
        maxVal = bigVal
    if minVal == None or smallVal < minVal:
        minVal = smallVal
#print("{}, {}".format(maxVal//10, minVal//10))
#Min-Max scaling
for year in availableYears:
    newDfGdp[year] = (newDfGdp[year]-minVal)/(maxVal-minVal)

newDf2015.to_csv(processedDataDir+"/Happiness2015")
newDf2016.to_csv(processedDataDir+"/Happiness2016")
newDf2017.to_csv(processedDataDir+"/Happiness2017")
newDf2018.to_csv(processedDataDir+"/Happiness2018")
newDf2019.to_csv(processedDataDir+"/Happiness2019")
newDfGdp.to_csv(processedDataDir+"/Gdp")

#Multidimensional
data = []
for country in countriesAvailable:
    row = []#[country]
    row.append(newDf2015.loc[newDf2015["Country"]==country].values.tolist()[0]); row[-1].pop(0)
    row.append(newDf2016.loc[newDf2016["Country"]==country].values.tolist()[0]); row[-1].pop(0)
    row.append(newDf2017.loc[newDf2017["Country"]==country].values.tolist()[0]); row[-1].pop(0)
    row.append(newDf2018.loc[newDf2018["Country"]==country].values.tolist()[0]); row[-1].pop(0)
    row.append(newDf2019.loc[newDf2019["Country"]==country].values.tolist()[0]); row[-1].pop(0)
    row.append(newDfGdp.loc[newDfGdp["Country"]==country].values.tolist()[0]); row[-1].pop(0); row[-1].append(0)
    data.append(row)

data = np.array(data)
np.save(processedDataDir+"/multiDimData.npy", data)

print("Done preprocessing")

