#HAC
import pandas as pd
from time import time
import numpy as np

import matplotlib.pyplot as plt 
from sklearn.cluster import AgglomerativeClustering as hac
titles = ["Beers", "Bereweries"]


read_beers = pd.read_csv("sub_dataset/5_beers.csv")
read_beers = read_beers[["brewery_name", 
            "review_overall", 
            "review_aroma", 
            "review_appearance", 
            "beer_style", 
            "review_palate",
            "review_taste",
            "beer_name",
            "beer_abv"]]


reviews_beers = read_beers.as_matrix()


read_beweries = pd.read_csv("sub_dataset/5_breweries.csv")
read_beweries = read_beweries[["brewery_name", 
            "review_overall", 
            "review_aroma", 
            "review_appearance", 
            "beer_style", 
            "review_palate",
            "review_taste",
            "beer_name",
            "beer_abv"]]

#print read[:10]
reviews_beweries = read_beweries.as_matrix()

print reviews_beers[:10]
print reviews_beweries[:10]

#reduccion de dimensionalidad con PCA
from sklearn.decomposition import PCA

#print reviews[:int(100),[1,2,3,5,6,8]]

pca = PCA(n_components=2)
pca.fit(reviews_beers[:int(100),[1,2,3,5,6,8]])
beers = pca.transform(reviews_beers[:int(100),[1,2,3,5,6,8]])

pca.fit(reviews_beweries[:int(100),[1,2,3,5,6,8]])
beweries = pca.transform(reviews_beweries[:int(100),[1,2,3,5,6,8]])

data = [beers, beweries]


#######


fig = plt.figure(figsize = (20,10))
fig.suptitle('HAC')
y=range(5)
print y
tiempo=[]
j=0
for X,i in zip(data,range(2)):
    #Agglomerative Clustering
    start_time = time()	
    clustering = hac(linkage = "ward", n_clusters = 5, affinity="euclidean")
    clustering.fit(X)

    final_time = time() - start_time
    tiempo.append(final_time)

    HAC_labels = clustering.labels_

    #Normalization
    x_min, x_max = np.min(X, axis = 0), np.max(X, axis = 0)
    X = (X - x_min) / (x_max - x_min)
    
    #Visualitation
    ax = fig.add_subplot(1,2,i+1)
    ax.set_xlabel("x pca")
    ax.set_ylabel("y pca")

    plt.title( 'Grafico: ' + titles[i] )

    
    for i in range(X.shape[0]):
        plt.text(X[i,0], X[i,1], str(y[j]),
        color=plt.cm.spectral(clustering.labels_[i]/10.+0.1),
        fontdict={'weight': 'bold', 'size': 8})
    j = j+1

    ax.set_xticks(())
    ax.set_yticks(())
    ax.axis([0,1.05,0,1.05])

print "Tiempo de ejecucion:", np.median(tiempo),"[s]"
plt.show()