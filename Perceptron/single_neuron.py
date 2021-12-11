import numpy as np

class Perceptron():
        # Sigmoid activation function
    def sigmoid(z):
        z = np.array(z, dtype = np.float32)
        return 1.0/(1.0+np.exp(-z))

    # Sign activation function
    def sign(z):
        for i in range(z.shape[0]):
            # if positive, set to 1
            if(z[i] >= 0):
                z[i] = 1
            else:
                # Otherwise set to 0
                z[i] = 0
        return z
        
    def __init__(self, n_features, activation = sign, alpha = .005):
        self.n_features = n_features
        self.W = np.random.randn(self.n_features)*np.sqrt(2)
        self.activation = activation
        self.alpha = alpha

    # Function to predict an output
    def predict (self, A):
        z = np.array(A @ self.W)
        return self.activation(z)

    # Function returns the MSE over the whole set
    def total_mse(y_hat, labels):
        error = labels - y_hat
        return (sum((error**2))/y_hat.shape[0])**(0.5)

    # Function returns the MSE of each element
    def mse(y_hat, labels):
        error = labels - y_hat
        return (error**2)**(1/2)
    
    def train_weights(self, A = [], labels = [], epochs = 1000, hist = False):
        hist_error = []
        hist_W = []
        
        # Start with randomly initiated weights
        self.W = np.random.randn(A.shape[1], 1)*np.sqrt(2)
        hist_W.append(self.W)

        # Calculate initial total error
        print(f"Initial Cost using {self.activation.__name__} activation function: {sum(abs(labels - self.predict(A)))}")

        # Refine weight values epoch-many times
        for i in range(epochs):
            # Step 1: Predict an outcome
            y_hat = self.predict(A)

            # Step 2: Find error
            error = y_hat - labels
            hist_error.append(sum(abs(error[:,0])))
            
            # Step 3: Use error to update weights
            self.W = self.W - self.alpha*(A.T @ error)
            hist_W.append(self.W)
            
        # Take best error and store weights
        hist_error = np.array(hist_error)
        i = np.argwhere(hist_error == np.min(hist_error))

        r = i[0]

        hist_W = np.array(hist_W)
        
        # Assign self weights at the index of lowest error
        self.W = hist_W[r,:,0].T

        # Double check error at weight 
        y_hat = self.predict(A)
        error = y_hat - labels
        
        # Show improvement
        print(f"Minimal Cost using {self.activation.__name__} activation function: {sum(abs(error))}")
        
        # Pass our calculated weight values back to parent
        if hist:
            return hist_error



