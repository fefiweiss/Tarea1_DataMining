
import pandas as pd 
import numpy, scipy
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler




#beer_reviews = pd.read_csv("beer_reviews.csv")
beer_reviews = pd.read_csv("test.csv")

brewery_name = beer_reviews.brewery_name
review_overall = beer_reviews.review_overall
review_aroma = beer_reviews.review_aroma
review_appearance = beer_reviews.review_appearance
beer_style = beer_reviews.beer_style
review_palate = beer_reviews.review_palate
review_taste = beer_reviews.review_taste
beer_name = beer_reviews.beer_name
beer_abv = beer_reviews.beer_abv


a = set()

for row in beer_name:
	a.add(row)
print len(a)


X = beer_reviews[['review_aroma','review_overall']]
X = StandardScaler().fit_transform(X)




db = DBSCAN(eps=0.3, min_samples=10).fit(X)
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





