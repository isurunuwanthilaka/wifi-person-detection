import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import numpy as np
import seaborn as sns

# Visualizing 6-D mix data using scatter charts
# leveraging the concepts of hue, size, depth and shape
fig = plt.figure(figsize=(50,50))
t = fig.suptitle('Chamidi - NipunaM - IsuruAp - Sandali - UoM_wireless - UNIC-wifi', fontsize=14)
ax = fig.add_subplot(111, projection='3d')

# Loading data
filename="G:/CurrentWorkspace/Wifi-Person-Detection/Data_Collection/final-data-set.csv"
data = pd.read_csv(filename)

xs = list(data['Chamidi1'])
ys = list(data['NipunaM6'])
zs = list(data['IsuruAp6'])

ss = np.array([int(abs(q)) for q in list(data['UoM_Wireless11'])])
colors = np.array([ 'red' if q==0 else 'green' if q==1 else 'blue' for q in list(data['id'])])

ax.scatter(xs, ys, zs, c=colors, s=ss)

ax.set_xlabel('Chamidi1')
ax.set_ylabel('NipunaM6')
ax.set_zlabel('IsuruAp6')

plt.show()


