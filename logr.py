import numpy as np
from sklearn import linear_model
#X is independent, continuous variable
X = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
#y is discrete binomial classifier
y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

log_reg = linear_model.LogisticRegression()
log_reg.fit(X,y)
print(log_reg.coef_)
print(log_reg.intercept_)
#now we've fit a logistic regression equation to the data, it will be able to predict classification based on input X
predicted = log_reg.predict(np.array([3.66]).reshape(-1,1))
#reshape doesn't change data, only reshapes data structure for processing
print(np.array([3.46]).reshape(-1,1))

print(predicted)

def log2prob(log_reg,x):
    log_odds = log_reg.coef_*x + log_reg.intercept_
    #print(log_odds)
    odds = np.exp(log_odds)
    prob = odds/(1+odds)
    return(prob)

print(log2prob(log_reg,2))

#Logistic Regression is good for predicting categorical data based off of independent variables and patterns in data
#Linear Regression is good for prediciting numerical data given independent numerical variable and patterns in data
#Multiple regression is good for predicting numerical output given multiple numerical independent variables as input 
#Clustering is good for predicting label given other data points by euclidean evaluation
#Decision Tree is good at predicting categorical data given other data points by generating boolean thresholds, can take many input indpendent variables into account
#-Must be converted to numerical beforehand
