#implementation of a single layer perceptron

#the activation function
def activation(x):
    return 1 if (x>0.0) else 0
#predicts class based on trained weights and unseen X data

def predict(weights, x):
    sum = 0.0
    for w,x in zip(weights,x):
        sum += w*x
    return activation(sum)
    
#returns the accuracy of the model 
#based on trained weights and dataset (including labels)
def accuracy(weights, X):
    sum = 0.0
    for i in range(len(X)):
        X_row = X[i][:-1]
        prediction = predict(weights,X_row)
        if prediction == X[i][-1]:
            sum+=1.0
    return sum/float(len(X))
    
#function to train the model based on dataset with labels
def fit2 (weights, X, learning_rate = 0.01, epochs = 500):
    for epoch in range(epochs):
        print("Epoch: " + str(epoch))
        print("Accuracy: " + str(self.accuracy(weights, X))
        for i in range (len(X)):
            X_row = X[i][:-1]
            prediction = predict(weights,X_row)
            error = X[i][-1] - prediction
            for j in range(len(weights)):
                weights[j] = weights[j] + (error*learning_rate*X[i][j])
    return weights
