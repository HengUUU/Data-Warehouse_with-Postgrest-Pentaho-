import numpy as np
from sklearn.preprocessing import MinMaxScaler


class Linear_Regression:
    def __init__(self,learning_rate = 0.063, n_iteration = 3000 ):
        self.weight = None
        self.bias = None
        self.learning_rate = learning_rate
        self.n_itera = n_iteration
        self.scaler = MinMaxScaler()
        
    def hypothesis(self,x):
        return np.dot(x,self.weight) + self.bias
    
    def cost_function(self,y_hat,y):
        return np.mean((y_hat-y)**2)
    
    def gradient_descend(self,X,y_hat,y):
        grad_we = np.dot(X.T,(y_hat - y))
        grad_bi =  np.mean(y_hat - y)
        return grad_we,grad_bi
    
    def fit(self,X,Y):
        # intial wieght and biase
        self.weight = [np.ones(X.shape[1])]
        self.bias = 0
        costList = []
        # normalize x
        X = self.scaler.fit_transform(X)
        # iteration
        for i in range(self.n_itera):
            # hypo
            hypo = self.hypothesis(X)
            # cost
            cost = self.cost_function(hypo,Y)
            costList.append(cost)
            # gradient
            grad_w,grad_b = self.gradient_descend(X,hypo,Y)
            # update
            self.weight -= self.learning_rate*grad_w
            self.bias -= self.learning_rate*grad_b
        return costList, self.weight,self.bias
            
    def predict(self,X):
        X = self.scaler.fit_transform(X)
        return np.dot(X,self.weight) + self.bias
    
            
            
        
        
        
        