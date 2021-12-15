# [Ensemble Learning](https://scikit-learn.org/stable/modules/ensemble.html)
*Regression*

![EL](EL.png)
---

## [Synopsis](https://en.wikipedia.org/wiki/Ensemble_learning)
Ensemble learning is the combination of multiple models to determine the final value of a prediction. Each model developed to model data has benefits and issues. Ensemble learning seeks to maintain the benefits of a model and mediate the issues. Ensemble learning can be used for regression and classification tasks, and can consist of mulitple isntances of the same model, or any combination of task-specific models (i.e. classification or regression). In this repository, we will investigate the voting regressor and the random forests models. In classification, ensemble learning models will "vote" on a classification, with the highest vote determining the predicted label. 

### Random Forests
A random forest is a collection of decision trees. Random forests build decision trees from drawing samples (without replacement) from the dataset. This tactic decreases the variance of the forest estimator and mitigate the risk of overfitting. The average of the decision trees is taken, averaging out some errors, to produce a prediction. Reducing the variance in this manner can risk increasing the bias, however the variance reduction is often significant enough to produce a better model. For information on how a decision tree makes its predictions, see the decision tree project in the regression or classification folder of this repository.

### Voting Regressor
The Voting Regressor combines different models and averages the predicted result, following the same logic as the random forests model. Weights can be assigned to each individual model, or they can all have equal weight, to skew the prediction towards a model that may describe the data better. Combining the outputs of multiple models can strengthen the predictive power and increase accuracy. For more information on how each model makes a prediction, please reference that model's folder in this repository.

While we will focus our efforts on these two models, ensemble learning has many variants for both classification and regression. For more information, reference the scikit-learn website linked at the top of this page.

## Prediction
An ensemble model makes a prediction based on the collective output of the models it is composed from. In regression, the predicted output is the weighted average value of all models. A model may be assigned a higher or lower weight if the model type is suited or detrimental to the specific dataset. 

## Error Analysis
After training the model, we will test the model by predicting the test set feature vectors and comparing it to the actual labels. The measurements we will use to calculate the error of each model is the Mean Squared Error and the Mean Absolute Error. These metrics provide complimentary error analysis for each model and will allow us to compare how well they do relative to each other. 

Mean Squared Error:
$
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y_i})^2
$

Mean Average Error:
$
MAE = \frac{1}{n}\sum_{i=1}^{n}(|y_i-\hat{y}_i|)
$

We will then compare the results with each model to determine the best model for our dataset. 