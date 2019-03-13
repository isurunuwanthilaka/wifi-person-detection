# 1. Importing libraries
import json
import csv
import os
import pandas as pd
import numpy as np 
import pickle 
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split  
from sklearn.metrics import classification_report, confusion_matrix 


# 2. Importing the dataset
#Download the dataset from database as a CSV file and store in the local directory. 
#To read data from CSV file, the simplest way is to use read_csv method of the pandas library. 
wifidata = pd.read_csv("./final-data-set.csv")   #change your file name

# 3. Exploratory Data Analysis
#check the dimensions of the data and see first few records
print("Dimensions of the data:")
print(wifidata.shape)
print("\nFirst few records:")
print(wifidata.head())

# 4. Data Preprocessing
# To divide the data into attributes and labels
X = wifidata.drop('id', axis=1)  #contains attributes
y = wifidata['id'] # contains coresponding labels

#divide data into training and test sets 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

# 5. Training the Algorithm
svclassifier = SVC(kernel='linear')  
svclassifier.fit(X_train, y_train) # train the algorithm on the training data

# 6. Making Predictions
y_pred = svclassifier.predict(X_test)

# 7. Evaluating the Algorithm
#Confusion matrix, precision, recall, and F1 measures are the most commonly used metrics for classification tasks.
print("\nConfusion Matrix:")
print(confusion_matrix(y_test,y_pred))
print("\nClassification Report:")
print(classification_report(y_test,y_pred))

# 8.save the model to disk
filename = 'finalized_model.pkl'
pickle.dump(svclassifier, open(filename, 'wb'))