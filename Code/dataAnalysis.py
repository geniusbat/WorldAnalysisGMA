import matplotlib.pylab as plt
import numpy as np
import pandas as pd
import clustering

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
    plt.legend()
    if limit == 0:
        break
plt.show()
'''

#Happiness
'''
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
'''
'''
#Happiness to GDP
df2015 = pd.read_csv(processedDataDir+"/Happiness2015")
dfGdp = pd.read_csv(processedDataDir+"/Gdp")
scores = []
gdps = []
for country in df2015["Country"].values.tolist():
    scores.append(df2015.loc[df2015["Country"]==country]["Score"].values.tolist()[0])
    gdps.append(dfGdp.loc[dfGdp["Country"]==country]["2015"].values.tolist()[0])
#Normalize scores
maxVal = max(scores); minVal = min(scores)
for i in range(len(scores)):
    scores[i] = (scores[i] - minVal)/(maxVal-minVal)
plt.figure()
plt.scatter(scores,gdps)

for i in range(len(scores)):
    plt.text(scores[i], gdps[i], df2015.iloc[i]["Country"])
plt.show()
'''
#GDP evolution
'''
dfGdp = pd.read_csv(processedDataDir+"/Gdp")
countries = dfGdp["Country"].to_list()[:10]
gdp2015 = dfGdp["2015"].to_list()[:10]
gdp2016 = dfGdp["2016"].to_list()[:10]
gdp2017 = dfGdp["2017"].to_list()[:10]
gdp2018 = dfGdp["2018"].to_list()[:10]
gdp2019 = dfGdp["2019"].to_list()[:10]

X_axis = np.arange(len(countries))

plt.figure()
plt.bar(X_axis-0.4, gdp2015, label="2015")
plt.bar(X_axis-0.2, gdp2016, label="2016")
plt.bar(X_axis, gdp2017, label="2017")
plt.bar(X_axis+0.2, gdp2018, label="2018")
plt.bar(X_axis+0.4, gdp2019, label="2019")
plt.xticks(X_axis, countries)
plt.legend()
plt.show()
'''
#Countries that improved gdp from 2018 to 2019
dfGdp = pd.read_csv(processedDataDir+"/Gdp")
countries = dfGdp["Country"].to_list()
gdp2018 = dfGdp["2018"].to_list()
gdp2019 = dfGdp["2019"].to_list()
countriesThatImproved = {}
countryClass = clustering.getClasses("2015", True)
classesOfCountriesThatImproved = {}
classesOfCountriesThatImproved[-1] = []
for index in range(len(countries)):
    country = countries[index]
    gdpA = gdp2018[index]
    gdpB = gdp2019[index]
    if gdpB >= gdpA:
        countriesThatImproved[country] = gdpB-gdpA
        try:
            key = countryClass[index]
        except:
            key = -1
        if key in classesOfCountriesThatImproved:
            classesOfCountriesThatImproved[key].append(country)
        else:
            classesOfCountriesThatImproved[key] = [country]

plt.figure()
plt.bar(list(countriesThatImproved.keys()), list(countriesThatImproved.values()))
plt.legend()
plt.show()

print(classesOfCountriesThatImproved)