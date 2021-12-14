---
# Linear Regression

## Overview

[Linear Regression](https://en.wikipedia.org/wiki/Linear_regression) is an algorithm borrowed from statistical inference and used to determine a linear equation that best represents the collected data. This can then be used to predict the ouptut of future data.

Linear regression is a linear approach for representing the relationship between an output and input variables. Linear regression estimates parameters from input data that minimize the squared-error of predicted and actual results. This approach leverages a conditional probability distribution given the values of the predictors. 

Linear Regression assumes input vectors are "fixed" observations, or constants, that are affected by some random error $\large \epsilon$ with some probability distribution. The equation $\large Y= \theta_{0} + x^i\theta_1 + \epsilon$. Because $\large\epsilon$ is a random variable, Y inherits its radomness. If we assume $\large\epsilon$ is normally distributed, we can model Y will also be normally distributed with the PDF of:

$
\Large f(y^i|x^i,\theta) = \frac{1}{\sqrt{2\pi}}e^{\frac{-(y^i - \theta^tx^i)^2}{2\sigma^2}}
$

We then use the [Log Likelyhood Estimator](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation) to find an estimate of $\theta$ which maximizes the probability of observing our observations. Refering to the equation above, we can see if we take the natural logarithm, we will get:

$
\Large \ell(\theta) = \ln L(\theta) = \ln{\frac{1}{\sqrt{2\pi}}\sum_{i = 1}^m(e^{\frac{-(y^i - \theta^tx^i)^2}{2\sigma^2}})}
$

$
\Large = m\ln({\frac{1}{\sqrt{2\pi}}})-\frac{1}{\sqrt{2\pi\sigma^2}}\sum_{i=1}^m(y^i - \theta^Tx^i)^2
$

The objective is to maximize the the probability $\theta$ describes what we observe. Therefore, all other components of the equation descrived above are considered "constant" with $\theta$ as the variable to be adjusted. $\theta$ Only appears inside the summation and the convex function $(y^i - \theta^Tx^i)^2$. A convex function has one local minimum, which is also the global minimum, so the value of theta that maximizes the probabiliity of describing the observations minimizes the error function $(y^i - \theta^Tx^i)^2$ and can be solved for directly using partial derivatives.

The equation for the optimal theta, $\hat{\theta}$, is:

$
\Large \hat{\theta} = (X^TX)^{-1}X^T
$

Using this equation, we can calculate the optimal $\theta$ directly, without needing the multiple iterations required by gradient descent.

## Strengths
Linear regression algorithms are extremly fast and computationaly cheap. They can provide great baselines for data with linearly corilated data and benefit from the ability to directly calculate $\theta$. As number of features grow, the computational strain increases for iterative algorithms exponentially. Adjusting the significance of each feature can also help determine which features should or should not be included in each dataset. 

## Weaknesses
Linear regession finds the optimal values of $\theta$ that minimizes the total squared error across all feature vectors. This makes it extremely susceptable to outliers, non-linear data, and data with large variance. Various linear regression algorithms, like lasso regression, elastic net, and ridge regression attempt to account and adjust for these deficiencies by adjusting the significance of the significance of features on prediction, the algorithms are still susceptible to large spreads in the data.

## Variations
Linear regression encompases a large family of algorithms that attempt to overcome the limitations of "simple" linear regression. 

### LASSO Regression
[LASSO](https://www.statisticshowto.com/lasso-regression/) - or Least Absolute Shrinkage and Selection Operator - regression uses "shrinkage" where data values are shrunk towards the mean. This algorithm is useful in feature selection and applies a "penalty" to features that do not benefit the prediction

### Ridge Regression
[Ridge](https://www.mygreatlearning.com/blog/what-is-ridge-regression/) regression compensates for large variation in the input data. Ridge regression includes a "penalty" term $\lambda$ that shrinks weight of $\theta$

### Elastic Net
[Elastic Net](https://en.wikipedia.org/wiki/Elastic_net_regularization) Regression is a combination of LASSO and Ridge Regression that adjusts both the weight of features and the weight of the updated $\theta$.
