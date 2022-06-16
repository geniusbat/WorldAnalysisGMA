import numpy as np
import pandas as pd

unprocessedDataDir = "UnprocessedData"
processedDataDir = "ProcessedData"
df2015 = pd.read_csv(unprocessedDataDir+"/HappinessReport/2015.csv")
df2016 = pd.read_csv(unprocessedDataDir+"/HappinessReport/2016.csv")
df2017 = pd.read_csv(unprocessedDataDir+"/HappinessReport/2017.csv")
df2018 = pd.read_csv(unprocessedDataDir+"/HappinessReport/2018.csv")
df2019 = pd.read_csv(unprocessedDataDir+"/HappinessReport/2019.csv")
happinessCountriesSeries = set(df2015["Country"]).intersection(set(df2016["Country"])).intersection(set(df2017["Country"])).intersection(set(df2018["Country or region"])).intersection(set(df2019["Country or region"]))

dfGdp = pd.read_csv(unprocessedDataDir+"/WorldGDP/gdp.csv")

countriesAvailable = set(happinessCountriesSeries).intersection(set(dfGdp["Country Name"]))
availableYears = ["2015", "2016", "2017", "2018", "2019"]

newDf2015 = df2015[df2015["Country"].isin(countriesAvailable)]
newDf2016 = df2016[df2016["Country"].isin(countriesAvailable)]
newDf2017 = df2017[df2017["Country"].isin(countriesAvailable)]
newDf2018 = df2018[df2018["Country or region"].isin(countriesAvailable)]
newDf2019 = df2019[df2019["Country or region"].isin(countriesAvailable)]
newDfGdp = dfGdp[dfGdp["Country Name"].isin(countriesAvailable)]
for column in newDfGdp.columns:
    if column!="Country Name" and column!="Code":
        if column not in availableYears:
            newDfGdp.drop(column,inplace=True,axis=1)

newDf2015.to_csv(processedDataDir+"/Happiness2015")
newDf2016.to_csv(processedDataDir+"/Happiness2016")
newDf2017.to_csv(processedDataDir+"/Happiness2017")
newDf2018.to_csv(processedDataDir+"/Happiness2018")
newDf2019.to_csv(processedDataDir+"/Happiness2019")
newDfGdp.to_csv(processedDataDir+"/gdp")
print("Done preprocessing")