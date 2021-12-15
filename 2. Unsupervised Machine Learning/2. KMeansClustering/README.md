# [K Means Clustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)

![KMC](KMC.jpg)
---

## [Synopsis](https://en.wikipedia.org/wiki/K-means_clustering)
K-means clustering was first proposed by Stuart Lloyd in 1957. It is an unsupervised machine learning algorithm used as a method of vector quantization that attempts to partition a dataset into k clusters. A feature vector is assigned to the closest cluster centroid. This algorithm minimizes the variance within a cluster by optimizing the squared errors of the feature vectors in the cluster. This optimization is computationally difficult, however heuristics exist that that allow the algorithm to converge quickly to a local optimum. 

Computing the centroids of K-means is easily understood. Centroids are randomly placed, typically by assigning them as a datapoint. It then computes the distance of each datapoint from its assigned centroid, and updates the centroid to minimize this distance. This will lead the centroids to center onto concentration points of data following the equations below:

$
S_i^t = [x_p:\|x_p-m_i^t\|^2 \leq \|x_p-m_j^t\|^2 \forall j,1\leq j \leq k] \\
$

where

$
m_i^{t+1} = \frac{1}{|S_j^t|}\sum_{x_j\in S_j^t}x_j
$

## Error Analysis
K Means Clustering is an unsupervised machine learning algorithm. We, therefore do not know how many clusters there should be and are using an algorithm to determine it. To determine the correct number of clusters, we will employ the 'elbow' method. This method computes the distance score between the centroid and the datapoints within the cluster. As clusters increase, this value will decrease. There should exist a point where this score decreases rapidly, then levels to a point where each additional cluster does cause a large decrease in the score. This point is called the 'elbow' and signals the correct number of clusters. 
