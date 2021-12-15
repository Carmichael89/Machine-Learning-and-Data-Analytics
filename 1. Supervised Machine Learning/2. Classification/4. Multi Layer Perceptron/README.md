# [Multi Layer Perceptron](https://scikit-learn.org/stable/modules/neural_networks_supervised.html#multi-layer-perceptron)
*Classification*

![MLP](multilayerperceptron_network.png)
---

## [Synopsis](https://en.wikipedia.org/wiki/Multilayer_perceptron)
The Multilayer Perceptron, or MLP, is an artificial neural network composed of at least three *perceptron* layers - an input layer, a hidden layer, and an output layer. While the inpnut and output layers are only one level deep, the hidden layer can contain any number of layers. A MLP containing a "deep" stack of hidden layers is called a Deep Neural Network. A deep stack is a succession of hidden layers where the output of one feeds the input of the next. MLPs can also have wide layers where the input layer, for example, feeds hidden layer 1 and the ouptut layer. This is a wide network because it connects all or part of the inputs directly to the output layer. This allows the network to learn both deep patterns and simple rules. 

The MLP works essentially the same as other machine learning models - it must be trained, tested, and reviewed. 

The benifits of an MLP are:
- It can be applied to complex/non-linear problems
- it works well with large input data
- it provides quick predictions after training

The issues with an MLP are:
- Training computations are difficult and time consuming
- Performance is heavily based on the quality of the training
- It is difficult to explain the internal workings of the model 

To train the MLP, a mini-batch of data is fed as an input to the model and fed foward to the output nodes to make a prediction. It then uses *backpropogation* to determine the error contributions from each layer, working backwards starting at the output node. Backpropogation applies the chain rule at the output of each layer and performs a gradient descent step to improve the weights at each node connection. 

It is important to note that during the initial development of the MLP, the crucial step to making it work was to change the activation function from a step function to a sigmoid function. The step activation function can only ever be a 0 or 1 and does not have a non-zero derivative, making gradient descent useless. The sigmoid is not the only functioning activation function, however. Any derivable activation function can be used - such as the hyperbolic tangent function (Tanh), the rectified linear unit function (ReLU), and the softmax function. 

The MLP can be used for both regression and classification tasks. For a regression implementation of the MLP, see the Regression folder in this repository. 

## Prediction
Like the perceptron, data is passed to a node, the inputs of the node are summed, and an activation function is applied to produce an output. Not every node needs to be connected to every other node. The activation function needs to be derivable (i.e. not the step function) for gradient descent to work. Each arc between nodes carries a weight. The data traversing the arcs are multiplied by the weights, then summed to get the output of the node. These weights are first randomly initialized, then trained using forward and back propogation. Below is a general example of the calculations.

### Predict
$$
a = \sigma(x^T\theta)
$$

### Calculate Error
$\frac{\partial C}{\partial W_i^L} = (a_i^L - y_i)\sigma^{\prime}(z_i^L)(a_{i}^{L-1})$

### Neuron Error Cost
$\delta^l = ((w^{l+1})\delta^{l+1}) \otimes \sigma^{\prime}(z^l)$

### Gradient Step
$\sigma^L = \nabla_a C \otimes\sigma^\prime(z^L)$

Once a prediction is made, the error is calculated and back propogated to yield the error at each node. This allows us to update the weights for each node specifically according to the error at that node.

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