from sklearn import linear_model
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as p     #Importing necessary libraries

bost=datasets.load_boston()        #Loading boston dataset
b=bost.data[:,np.newaxis,2]         #Creating new dimension so that sklearn library accepts as input without error

xtr=b[:-25]                     #Training x with a small part of the dataset
xts=b[-25:]                     #Testing x with a small part of the dataset

ytr=bost.target[:-25]           #training y with a small part of dataset
yts=bost.target[-25:]           #testing y with a small part of dataset

model=linear_model.LinearRegression()   #initializing linear regression
model.fit(xtr,ytr)                      #Training data with training set
ypred=model.predict(xts)                #predicting data with testing set

p.scatter(xts,yts, color='red')
p.plot(xts,ypred)
p.show()                            #Plotting the line and points