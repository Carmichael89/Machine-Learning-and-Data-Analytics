# Machine-Learning-and-Data-Analytics
Creator: Christian Carmichael

![Machine Learning](machineLearning.jpg)

This repository is a collection of machine learning algorithms documenting the project development of a typical machine learning project. Machine learning can be subdivided into two major categories - supervised and unsupervised. Supervised learning can be further divided into regression and classification methods. Unsupervised learning can be divided into clustering and anomaly detection. 

This repository follows the flow of a typical machine learning project - data organization and analysis, model selection, and model comparison. The model selection is first divided by supervised and unsupervised, then by regression/classification. The only unsupervised learning method we will discuss will be clustering. Each method uses the same dataset to make comparisons more tractable and to help clarify the differences between the algorithms.

## Supervised vs Unsupervised
Supervised learning is training an algorithm with pre-determined labels and features. A label is the prediction we are interested in and the exact shape and meaning of a label can change from project to project. For example, the label for a computer vision project is typically uses a one-hot encoding method the size of the number of objects the algorithm needs to learn while the label of a regression algorithm is a prediction made by fitting a line to data. 

Unsupervised learning is used to identify patterns and relationships unlabeled data. For example, if you have a large dataset and would like to find how many groups most accurately represent the data you would use an unsupervised learning algorithm to determine the number of clusters. 

## [Regression](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning) vs [Classification](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning)
Regression finds the best line to minimize some cost function. This line can then be used to predict a continuous label based on input features. The most common example of a regression algorithm is a real estate dataset which uses several input features - such as number of bathrooms, number of bedrooms, house size, and lot size - to predict the sale price of a home. 

Classification uses input vectors to determine a 0/1 label predicting if a set of input vectors corresponds to a category or not. If there are multiple categories, this can be accomplished by using one-hot encoding where there are one output for each possible category in which only one output can be 1 at a time. 

## [Clustering](https://scikit-learn.org/stable/modules/clustering.html#clustering) vs [Anomaly Detection](https://scikit-learn.org/stable/modules/outlier_detection.html)
Clustering groups the dataset into a specified number of clusters with the goal of determining how the data is segmented or what groups future data will belong to. Clustering can be used for tasks like market segmentation, search engines, and data analysis. In clustering, the number and specifics of the labels are unknown and the programmer only specifies the number of potential clusters.

Anomaly detection creates a statistical model on what "normal" data looks like and uses it to identify abnormal instances. This helps to identify defective items or new trends without specifying exactly what changes to look for.

## Resources
In this repository, we will experience how each algorithm interprets and trains on the data. This will be accomplished via a mix of [sklearn](https://scikit-learn.org/stable/) methods and self-programmed examples. This will provide the reader with the ability to learn how to implement ready made methods to start their own machine learning project quickly, as well as how to develop their own custom made modules. 

