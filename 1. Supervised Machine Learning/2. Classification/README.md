# Supervised Classification

---

## Synopsis

One of the primary problems machine learning can tackle is to classify data. A properly trained and employed machine learning classification algorithm, for example, can classify handwritting or items in a picture. Classification models make a prediction on if the data should be a label or not, meaning there must be one output per potential label. If we are training an algorithm to determine what digit from 0-9 has been written there must be 10 outputs that can be a 0 or 1 in which only one output is ever a 1. This is called white-hot encoding and can be used on both the output and input sides of the algorithm. 

The 0/1 output of the classification algorithm is achieved via an activation function. The activation function takes data as an input and outputs a number representative of the classification. The sigmoid activation function, for example, will output a number between 0 and 1 while the Tanh function will output a number between -1 and 1. If an output is a fractional number, it is typically rounded to the nearest whole number to make a determination on the classification. In a multi-layer neural network, each hidden layer and output layer can have different activation functions.

## Classification Algorithms

There are several methods to develop a classification algorithm. In this repository, we will examine the following methods:

1. Logistic Regression
2. K-Nearest Neighbors (KNN)
2. Perceptron
3. Multi-Layer Perceptron (MLP)
4. Decision Tree
5. Support Vector Machine (SVM)

Each method has its own benifits and detractors which will be explained in further detail in each algorithms README.md file, however a quick synopsis is below:

### Logistic Regression: 
Pros: Input features can be independant and do not need to follow a normal distribution
Cons: susceptable to overfitting, sensitive to outliers, requires large datasets

### Perceptron and MLPs: 
Pros: Flexible, can easily handle large, non-linear data
Cons: not guaranteed to be convex, difficult to understand or explain what the algorithm is doing, computationally expensive

### KNN: 
Pros: No learning phase, adaptable, robust to noisy data 
Cons: computationaly expensive and requires large dataset

### Decision Tree: 
Pros: Easy pre-processing, doesn't require data scaling, intuitive and easy to explain
Cons: small change in the data can cause large change in structure, can be very complex, computationally expensive

## SVM
Pros: Works well with a clear margin of speration, effective with high dimensional data
Cons: does not perform well with a large dataset, is not resilient to outliers/noisy data

## Data and Error Analysis
Each classification model will use the same data and error valulations to allow us to compare how each algorithm works with our data. We will be using the [diabetes data set](https://archive.ics.uci.edu/ml/datasets/diabetes) from the UCI machine learning repository for all regression models. We will measure and compare the confusion matrix, which measures the number of correct and incorrect labels, and the F score which is a ratio between the precision and recall of an algorithm. These measurements will allow us to measure the effectiveness of each algorithm and compare them to each other to determine the best model. 

