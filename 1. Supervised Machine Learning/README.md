# [Supervised Learning](https://en.wikipedia.org/wiki/Supervised_learning)

---

![supervisedlearning](supervisedlearning.jpg)

Supervised Learning is a category of machine learning where algorithms are trained with both input feature vectors and input labels. Training a supervised learning algorithm follows the predict-compare-update cycle where the algorithm uses a feature vector to predict a label, the label is compared to the "true" label and a cost is calculated, and the cost is used to update the weights to make future predictions.  

Supervised learning can be further seperated into classificationa and regression tasks. Classification tasks assign a *classification* to an input vector in the form of a 1 or 0 where 1 represents a "yes" and a 0 represents a "no". This allows for multiple classification problems where each potential classification is encoded with a 0 or a 1. Regression attempts to fit a line to the data that minimizes some cost function. Regression outputs are continuous and are used in problems where you cannot classify every feasible solution.

In supervised learning, preparing the data should follow these steps:
1. Make all data computer readable (i.e modify yes/no/positive/female etc to 1s and 0s)
2. Shuffle the data to ensure it is well mixed and minimize the chances of high bias due to runs of the same label
3. Partition the data into training and testing data. The training data can be further partitioned into training and validation data. I typically use a partition of 90% training and validation and 10% testing or 81% training, 9% validation, and 10% testing. 
4. Split the feature vectors and labels from each feature vector.
5. Insert a column of ones to act as the bias 

Once the above steps are completed, we can train the algorithm, then use it to predict the test labels and compare the results with other algorithms to determine the best one. 

## Error Analysis
Once the algorithms are trained, we will conduct error analysis to determine how well each algorithm performs. To provide comparable information, I have selected two datasets - one for regression and one for classification - to use for every model. The regression data set is the [real estate valuation data set](https://archive.ics.uci.edu/ml/datasets/Real+estate+valuation+data+set) from the University of California-Irving machine learning repository. The classification dataset will be the [diabetes data set](https://archive.ics.uci.edu/ml/datasets/Real+estate+valuation+data+set) from the same repository. 

To compare the data, each regression algorithm will provide the means squared error and the mean absolute error error. Each classification algorithm will provide the confusion matrix and F1 score. Because each type of algorithm will be trained using the same data, we can compare which model works the best, why, and ways to shape the data to improve the results. 
