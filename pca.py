



# License: BSD 3 clause

import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

from sklearn import decomposition
from sklearn import datasets

numpy.random.seed(5)

centers = [[1, 1], [-1, -1], [1, -1]]
iris = datasets.load_iris()
X = iris.data
beer_reviews = pd.read_csv("test.csv")
X = beer_reviews[['review_palate','review_appearance','review_aroma','review_taste']].as_matrix()



pca = decomposition.PCA(n_components=4)
pca.fit(X)
X = pca.transform(X)
print X


#X = StandardScaler().fit_transform(X)




db = DBSCAN(eps=0.3, min_samples=7).fit(X)
core_samples_mask = numpy.zeros_like(db.labels_, dtype = bool)
core_samples_mask[db.core_sample_indices_] = True

labels = db.labels_
unique_labels = set(labels)

colors = plt.cm.Spectral(numpy.linspace(0, 1, len(unique_labels)))

for k, col in zip(unique_labels, colors):
	if k == -1:
		col = 'k'

	class_member_mask = (labels == k)

	xy = X[class_member_mask & core_samples_mask]
	plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=10)
	xy = X[class_member_mask & ~core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=6)

plt.title("DBSCAN")
plt.show()





