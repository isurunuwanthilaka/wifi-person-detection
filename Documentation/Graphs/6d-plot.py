import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import numpy as np
import seaborn as sns

# Visualizing 3-D mix data using scatter charts
# leveraging the concepts of hue, size, depth and shape
fig = plt.figure(figsize=(-100,-100))
t = fig.suptitle('Chamidi - NipunaM - IsuruAp - UoM_wireless - UNIC-wifi', fontsize=14)
ax = fig.add_subplot(111, projection='3d')

# Loading data
filename="G:/CurrentWorkspace/Wifi-Person-Detection/Data_Collection/final-data-set.csv"
data = pd.read_csv(filename)

xs = list(data['Chamidi1'])
ys = list(data['NipunaM6'])
zs = list(data['IsuruAp6'])
data_points = [(x, y, z) for x, y, z in zip(xs, ys, zs)]

ss = list(map(int,-data['UoM_Wireless11']))
colors = list(map(int,-data['UNIC-wifi11']))
markers = [',' if q == 0 else 'x' if q == 1 else 'o' for q in list(data['id'])]

for data, color, size, mark in zip(data_points, colors, ss, markers):
    x, y, z = data
    ax.scatter(x,y,z,alpha=0.4, c= '0.'+str(130-color), edgecolors='none', s=(size**1.2), marker=mark)

ax.set_xlabel('Chamidi1')
ax.set_ylabel('NipunaM6')
ax.set_zlabel('IsuruAp6')

plt.show()
