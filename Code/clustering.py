import numpy as np
from sklearn.cluster import AgglomerativeClustering

processedDataDir = "ProcessedData"

data = np.load(processedDataDir+"/multiDimData.npy")

clustering = AgglomerativeClustering().fit(data)

print(clustering.labels_)