from cProfile import label
from os import scandir
import matplotlib.pylab as plt
import numpy as np
import pandas as pd
from sklearn import preprocessing

processedDataDir = "ProcessedData"
availableYears = ["2015", "2016", "2017", "2018", "2019"]

dfGdp = pd.read_csv(processedDataDir+"/gdp")
spainData = [dfGdp.loc[dfGdp["Country Name"]=="Spain"][year] for year in availableYears]
germanData = [dfGdp.loc[dfGdp["Country Name"]=="Germany"][year] for year in availableYears]
x = availableYears

scaler = preprocessing.RobustScaler()
spainScaled = scaler.fit_transform(np.array(spainData).reshape(-1,1))
germanScaled = scaler.fit_transform(np.array(germanData).reshape(-1,1))



plt.figure()
#plt.plot(x, spainData, label="Spain")
plt.plot(x, spainScaled, label="Spain scaled")
plt.plot(x, germanScaled, label="Germany")
plt.legend()
plt.show()