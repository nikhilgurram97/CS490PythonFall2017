from sklearn import datasets, metrics
from sklearn import svm
from sklearn.cross_validation import train_test_split   #Importing necessary libraries

i=datasets.load_diabetes()      #Loading diabetes dataset
x=i.data
y=i.target                      #Assigning data and target variables

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)   #Implementing Training an Testing sets, with 20% testing set size of full dataset

m=svm.SVC(kernel="linear")      #Implementing SVM Classification with linear kernel
m.fit(x_train,y_train)          #Training the model
y_pred=m.predict(x_test)        #Predicting data with testing set
a=metrics.accuracy_score(y_test,y_pred)
print("Linear Accuracy: "+str(a))   #Printing Linear Model Accuracy score

m=svm.SVC(kernel="rbf")      #Implementing SVM Classification with RBF kernel
m.fit(x_train,y_train)          #Training the model
y_pred=m.predict(x_test)        #Predicting data with testing set
b=metrics.accuracy_score(y_test,y_pred)
print("RBF Accuracy: "+str(b))   #Printing Linear Model Accuracy score

if (a==b):
    print ("Changing Kernel doesn't change the Accuracy of the model")
else:
    print ("Changing Kernel changed the Accuracy of the model")