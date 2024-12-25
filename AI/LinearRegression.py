import numpy as np
# <-------------------------------Code for Linear Regression------------------------------->
class LinearRegression:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None
        self.history = {'loss': []}

    def fit(self, X, y):
        """
        Train the linear regression model using gradient descent.
        
        Parameters:
        X (array-like): Training features of shape (n_samples, n_features)
        y (array-like): Target values of shape (n_samples,)
        """
        # Initialize parameters
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # Gradient descent
        for _ in range(self.n_iterations):
            # Forward pass
            y_predicted = self._predict(X)
            
            # Calculate gradients
            dw = (1/n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1/n_samples) * np.sum(y_predicted - y)
            
            # Update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
            
            # Calculate and store loss
            loss = self._mean_squared_error(y, y_predicted)
            self.history['loss'].append(loss)

    def predict(self, X):
        """
        Make predictions for new data.
        
        Parameters:
        X (array-like): Features of shape (n_samples, n_features)
        
        Returns:
        array-like: Predicted values
        """
        return self._predict(X)
    
    def _predict(self, X):
        """Internal prediction method"""
        return np.dot(X, self.weights) + self.bias
    
    def _mean_squared_error(self, y_true, y_pred):
        """Calculate mean squared error loss"""
        return np.mean((y_true - y_pred) ** 2)
    
    def score(self, X, y):
        """
        Calculate R-squared score.
        
        Parameters:
        X (array-like): Features
        y (array-like): True values
        
        Returns:
        float: R-squared score
        """
        y_pred = self.predict(X)
        ss_total = np.sum((y - np.mean(y)) ** 2)
        ss_residual = np.sum((y - y_pred) ** 2)
        return 1 - (ss_residual / ss_total)
    
# <-------------------------------Code for Linear Regression Implementation------------------------------->
# Generate sample data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1).flatten()

# Create and train the model
model = LinearRegression(learning_rate=0.01, n_iterations=1000)
model.fit(X, y)

# Make predictions
X_test = np.array([[1.5]])
prediction = model.predict(X_test)

# Calculate R-squared score
r2_score = model.score(X, y)