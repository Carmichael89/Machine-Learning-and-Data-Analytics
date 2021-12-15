# [Decision Tree Classification](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
*Classification*

![DTC](Decision_Tree.jpg)
---

## [Synopsis](https://en.wikipedia.org/wiki/Decision_tree_learning)
Decision tree classifiers are an evolution of the classification chart, which have been used throughout history. The decision tree is a model that predicts the value of a target variable based on input variables. Each node in the tree is labeled with an input feature and the arcs of the feature are labeled with possible values (i.e. x2 >= 1, x2 =< 1). Each node splits possible values of each feature until arriving at a position in which (ideally) one class is described by the set of inequalities preceding the node. A decision the programmer must make is the acceptable mixture of classes within a leaf node. Only allowing pure nodes could expose the model to overfitting. This is an example of a greedy algorithm. 

Two methods to determine the purity of a node are *Gini* and *Entropy*. The Gini impurity is calculated with the equation:
$
G_i = 1 - \sum_{k=1}^{n}(p_{i,k}^2)
$

Where $p_{i,k}$ is the ratio of class k instances among the training instances of the ith node. A node is pure if the Gini score = 0. For example, if a dataset has 3 classifications, Gini will sum the number of instances in each class, squared, then subtract that value from one.

Entropy is calculated with the equation:
$H_i = - \sum_{k=1}^n p_{i,k}log_2(p_{i,k})$

Like Gini, a pure node will have an entropy of 0. 

The decision between Gini and Entropy is essentially preference. Choosing one over the other does not typically cause a difference. However, Gini is slightly faster, while entropy produces a more balanced tree. 

The Decision Tree works essentially the same as other machine learning models - it must be trained, tested, and reviewed. 

The benefits of a decision tree are:
- Does not require much data pre-processing
- Intuitive and easy to explain

The issues with an decision tree are:
- Small changes in the data can cause large changes in the tree
- Can produce much more complicated calculations than other models
- Computationally expensive

The decision tree can be used for both regression and classification tasks. For a regression implementation of the decision tree, see the Regression folder in this repository. 

## Prediction
To predict a value with the decision tree, a feature vector is essentially filtered into a classification using the inequalities on the nodes until it reaches a leaf node (end node of a path)

### Calculate Error
The Scikit-Learn module uses the Classification and Regression Tree (CART) algorithm to train decision trees. The algorithm splits the training set into two subsets along a single feature, $k$, and a threshold $t_k$ It searches the pair that produces the purest subset. CART Minimizes the error:

$J(k,t_k) = \frac{m_{left}}{m}G_{left} + \frac{m_{right}}{m}G_{right}$

where

$$
\begin{cases}
    G_{left/right} \text{ measures impurity of the left/right subset} \\
    m_{left/right} \text{ is the number of instances in the left/right subset}
\end{cases}
$$

Unlike other models that produce a prediction, then modify the weights to increase the accuracy, the Decision Tree filters the data to create pure nodes and future feature vectors are filtered by these nodes. 

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
