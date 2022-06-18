import matplotlib.pylab as plt
import numpy as np
import pandas as pd

processedDataDir = "ProcessedData"
availableYears = ["2015", "2016", "2017", "2018", "2019"]

#Show gdp of first 20 countries
dfGdp = pd.read_csv(processedDataDir+"/Gdp")
x = availableYears
limit = 20
'''
plt.figure()
for index, row in dfGdp.iterrows():
    limit -= 1
    data = [row[year] for year in availableYears]
    plt.plot(x, data, label="{}".format(row["Country"]))
    if limit == 0:
        break
plt.show()
'''

#Happyness
df2015 = pd.read_csv(processedDataDir+"/Happiness2015")
df2016 = pd.read_csv(processedDataDir+"/Happiness2016")
df2017 = pd.read_csv(processedDataDir+"/Happiness2017")
df2018 = pd.read_csv(processedDataDir+"/Happiness2018")
df2019 = pd.read_csv(processedDataDir+"/Happiness2019")
happinessDataframes = {"2015":df2015, "2016":df2016, "2017":df2017, "2018":df2018, "2019":df2019}
plt.figure()
y = [df.loc[df["Country"]=="Spain"]["Score"].values[0] for year, df in happinessDataframes.items()]
plt.stem(availableYears,y,label="Spain")
plt.stem(availableYears,[df.loc[df["Country"]=="Germany"]["Score"].values[0] for year, df in happinessDataframes.items()],label="Germany")
plt.show()

df = pd.read_csv(processedDataDir+"/Happiness2017")
print(df.columns)