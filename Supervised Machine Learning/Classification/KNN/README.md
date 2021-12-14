# [K-Nearest Neighbors Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)
*Classification*

![KNN](KNN.png)
---

## [Synopsis](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)
The K-Nearest Neighbors (KNN) algorithm is a machine learning model in which a specified number of neighbors (k) are calculated to determine the classification of the feature vector in question.KNN can be use for both classification and regression taks. This method was first developed by Evelyn Fix and Joseph Hodges in 1951. In classification, a vote is taken amongst the neighbors, and the classification with the highest vote wins. In regression, the average of the k-neighbors is taken as the predicted value of the feature vector. In the case where k=1, the classification or value of the closest neighbor becomes the classification or value of the feature vector. 

Neighbors can also be assigned higher weights the closer they are to the datapoints to perform weighted neighbor classification. Here, weights can be assigned using the follwoing equation:

$
w_{ni} = \frac{1}{k}[1+\frac{d}{2}-\frac{d}{2k^{2/d}}(i^{1+2/d}-(i-1)^{1+2/d})]
$
for $i = 1,2,...,k$
and $w_{ni} = 0$ for $i =k+1,...,n$

KNN works by assigning a (preferably large) training set to the algorithm to act as a lookup table. As such, there is not training time or calculations. Once the training data is assigned, the model will use it as a reference for future data. To calculate the k-neighbors, the algorithm must calculate the distance between the input data and reference data. This can cause an issue if the number of features and training set are large because a distance must be calculated to all reference points to determine the closest neighbors. The computational complexity can be enormous. 

The benifits of an KNN are:
- No training period
- New data can be added seamlessly
- Quick an easy implementation

The issues with an KNN are:
- Large datasets require long calculation times
- High dimensionality causes issues with distance calculation
- Sensitive to noisy data and outliers 


## Prediction
A prediction with KNN is made by comparing a feature vector to the training set. To determing the closest neighbors, a distance must be caculated to all known points using one of many distance calculations. Two most popular and well known are euclidean or manhattan distances. 

### Euclidean Distance
$d_i = \sqrt{\sum{(x^i-y^i)^2}}$

### Manhattan Distance
$d_i = \sum{|x^i-y^i|}$

Once all distances are calculated, the k-closest are deteremined and used to gather votes to perform the classification.

### Calculate Error
The prediction is made using the k-closest neighbors on the training set. Performance can be determined by predicting and comparing the test set, however there is no cost calculated when training the KNN algorithm. 

## Error Analysis
After training the model, we will calculate the confusion matrix and F score to compare to the other models. The confusion matrix shows the predicted vs actual labels in an easily readible format. The F score is a ratio between the precision and recall.

Precision is calculated using the equation:
$
precision = \frac{true positives}{True Positives + False Positives}
$

Recall is calculated using the equation:
$
recall = \frac{True Positives}{True Positives + False Negatives}
$

The F score is calculated using the equation:
$
F = \frac{precision*recall}{precision + recall}
$

These metrics will allow us to easily compare the models.