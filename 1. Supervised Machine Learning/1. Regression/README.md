# Supervised Regression

---

## Synopsis

One of the primary problems machine learning can tackle is to predict an outcome for a given set of inputs. A classic example of regression is predicting the sale price of a house based its features (i.e. house size, number of floors, number of bathrooms, etc.). This is determined by identifying the "best-fit" line of the data to minimize some cost function $J(\theta)$. The 2-d linear case of predicting from a single feature is easily visualized and explained as $\hat{y} = mx+b$ where $\hat{y}$ is the predicted result, $x$ is the input feature, $m$ is the weight applied to the feature, and $b$ is the bias. The weight $m$ is typically written as $\theta$ for machine learning applications. $\theta$ is borrowed from statistics to represent the fact we are estimating the "true" weight applied to the feature to obtain an accurate result. The bias $b$ can also be thought of as a weight $\theta$ multiplied by 1, yielding the equation: $\hat{y} = \theta^1x^1 + \theta^0x^0$ where $x^1$ is the input feature, $x^0$ is one and $\theta^1$ and $\theta^0$ are the weights applied to $x^1, x^2$.

Regression algorithms apply a function to input data to produce a prediction. This prediction is then compared to the real value (when training or testing) to calculate the error, and the weights adjusted (when training) to produce the optimal function that minimizes the error. To evaluate the performance of an algorithm, the data needs to be partitioned so the model has not been exposed to every element. This allows us to see how accurate a prediction will be compared to an actual label. 

## Regression Algorithms

There are several methods to develop a regression algorithm. In this repository, we will examine the following methods:

1. Linear Regression
2. Gradient Descent
3. K-Nearest Neighbors Regression (KNN)*
4. Tree Regression*
5. Support Vector Machine Regression (SVMR)*

The methods in the list above marked with an * are classification methods, however they can also be adapted to regression tasks. Each method has its own benefits and detractors which will be explained in further detail in each algorithms README.md file, however a quick synopsis is below:

### Linear Regression: 
Pros: Simple, fast and easily explainable 
Cons: susceptible to overfitting.

### Gradient Descent: 
Gradient Descent is a way to find the optimal $\theta$ values for a regression algorithm, but it is so common and important I have separated it for emphasis.
Pros: will always find a local minimum, can converge quickly
Cons: may not find global minimum, have to test to ensure learning rate will allow convergence

### KNN: 
Pros: No learning phase, adaptable, robust to noisy data 
Cons: computationally expensive and requires large dataset

### Tree Regression: 
Pros: Easy to interpret, adaptable, can easily prevent overfitting 
Cons: computationally expensive and does not perform well with continuous variables

### SVMR: 
Pros: Works well with high-dimensional data, memory efficient, and can be determined based off of acceptable error
Cons: does not work well with large or noisy datasets

## Data and Error Analysis
Each regression model will use the same data and error valuations to allow us to compare how each algorithm works with our data. We will be using the [real estate valuation data set](https://archive.ics.uci.edu/ml/datasets/Real+estate+valuation+data+set) from the UCI machine learning repository for all regression models. We will measure and compare the mean squared error (MSE) and the mean average error (MAE) score for each model. This is a standard performance measurement that is simple to calculate by hand and is provided by Scikit-Learn methods. The lower the MSE the better the model. 

