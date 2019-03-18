# 1. Importing libraries
import pickle 
import pandas as pd
from sklearn.model_selection import train_test_split  
from sklearn.metrics import classification_report, confusion_matrix 

# 2. Import unknoen data
wifidata = pd.read_csv("./test.csv")

# 3. load the model from disk
filename = 'finalized_model.sav'
model = pickle.load(open(filename, 'rb',encoding='utf-8'))

# 4. Making Predictions
y_pred = model.predict(wifidata)
print(y_pred)
