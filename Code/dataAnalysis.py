from cProfile import label
import matplotlib.pylab as plt
import numpy as np
import pandas as pd
processedDataDir = "ProcessedData"
availableYears = ["2015", "2016", "2017", "2018", "2019"]

dfGdp = pd.read_csv(processedDataDir+"/gdp")
spainData = [dfGdp.loc[dfGdp["Country Name"]=="Spain"][year] for year in availableYears]
germanData = [dfGdp.loc[dfGdp["Country Name"]=="Germany"][year] for year in availableYears]
x = availableYears

plt.figure()
plt.plot(x, spainData, label="Spain")
plt.plot(x, germanData, label="Germany")
plt.legend()
plt.show()