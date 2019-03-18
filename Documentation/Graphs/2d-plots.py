import numpy as np
import pandas as pd
import operator
import random
import os
import matplotlib.pyplot as plt

# Loading data
filename="G:/CurrentWorkspace/Wifi-Person-Detection/Data_Collection/final-data-set.csv"
data = pd.read_csv(filename)

no_person = data[data.id==0]
one_person = data[data.id==1]
five_person = data[data.id==2]

len_no = no_person.shape[0]
len_one = one_person.shape[0]
len_five = five_person.shape[0] 

plt.xticks(range(-100,0,1))
plt.figure(1)

c=0
for name in data.columns:
    if name=='id':
        continue
    freq_no = no_person[name].value_counts().to_dict()
    freq_one = one_person[name].value_counts().to_dict()
    freq_five = five_person[name].value_counts().to_dict()

    plt.scatter(map(int,freq_no.keys()),np.ones(len(freq_no))-0.5+c*2,s=2*np.array(map(int,freq_no.values())),c='r',label='no')
    plt.scatter(map(int,freq_one.keys()),np.ones(len(freq_one))+c*2,s=2*np.array(map(int,freq_one.values())),c='g',label='one')
    plt.scatter(map(int,freq_five.keys()),np.ones(len(freq_five))+c*2+0.5,s=2*np.array(map(int,freq_five.values())),c='b',label='five')
    c+=2

plt.xlabel('RSSI values')
plt.title('IoT Data Visualization')
plt.grid(True)
plt.show()
