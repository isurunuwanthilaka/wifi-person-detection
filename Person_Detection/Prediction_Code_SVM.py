# 1. Importing libraries
import json
import csv
import os
import pandas as pd
import numpy as np  
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split  
from sklearn.metrics import classification_report, confusion_matrix 


# 2. Importing the dataset
#Download the dataset from database as a CSV file and store in the local directory. 
#To read data from CSV file, the simplest way is to use read_csv method of the pandas library. 
wifidata = pd.read_csv("wifi_dataggggg.csv")   #chnage your file name
unknowndata = pd.read_csv("unknownData.csv")


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

# 8. Predict Unknown Data
unknown_pred = svclassifier.predict(unknowndata)


# ---------- Remaining part is the Presentation of Data ---------------------#

# 9. Create a Text File
file = open("Result_Group3.txt", "w")
print("\nUnknown Data Labels")
for i in range(len(unknown_pred)):
    result= "Predicted room id for the respective row " + str(i+1) + " is " + str(unknown_pred[i])
    file.write(result)
    file.write("\n")
    print(result)
file.close()

# 10. Create a Csv File
val=0
def data_store_csv():

    result = {"UoM_Wireless1": -100, "UoM_Wireless6": -100, "UoM_Wireless11":-100, "eduroam1": -100, "eduroam6": -100, "eduroam11": -100, "Jungle Book10":-100, "PROLINK_H5004NK_8766E11": -100,"UNIC-wifi11":-100}
    ids=["UoM_Wireless1","UoM_Wireless6","UoM_Wireless11","eduroam1","eduroam6","eduroam11","Jungle Book10","PROLINK_H5004NK_8766E11","UNIC-wifi11"]

    filename = "Result_Group3.csv"
    count=0
    for y in row:
        result[ids[count]]=y
        count+=1
    result["id"] = unknown_pred[val]
    df = pd.Series(result).to_frame().T
    df.to_csv(filename,index=False,mode='a',header=(not os.path.exists(filename)))
    

with open('unknownData.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        try:
            tr=int(row[0])
            data_store_csv()
            val+=1
        except:
            continue



