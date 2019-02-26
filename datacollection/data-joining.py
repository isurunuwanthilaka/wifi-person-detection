import pandas as pd
import os

filename="cleaned-data-set.csv"

data0 = pd.read_csv("wifi_data0.csv")[['Chamidi1','NipunaM6','IsuruAp6','Sandali11','Becon_Wireless11','UoM_Wireless11','UNIC-wifi11','id']]
data1 = pd.read_csv("wifi_data01.csv")[['Chamidi1','NipunaM6','IsuruAp6','Sandali11','Becon_Wireless11','UoM_Wireless11','UNIC-wifi11','id']]
data2 = pd.read_csv("wifi_data02.csv")[['Chamidi1','NipunaM6','IsuruAp6','Sandali11','Becon_Wireless11','UoM_Wireless11','UNIC-wifi11','id']]
data3 = pd.read_csv("wifi_data10.csv")[['Chamidi1','NipunaM6','IsuruAp6','Sandali11','Becon_Wireless11','UoM_Wireless11','UNIC-wifi11','id']]
data4 = pd.read_csv("wifi_data11.csv")[['Chamidi1','NipunaM6','IsuruAp6','Sandali11','Becon_Wireless11','UoM_Wireless11','UNIC-wifi11','id']]
data5 = pd.read_csv("wifi_data21.csv")[['Chamidi1','NipunaM6','IsuruAp6','Sandali11','Becon_Wireless11','UoM_Wireless11','UNIC-wifi11','id']]

data0 = data0.append(data1)
data0 = data0.append(data2)
data0 = data0.append(data3)
data0 = data0.append(data4)
df = data0.append(data5)

df = df.sample(frac=1).reset_index(drop=True)

df.to_csv(filename,index=False,mode='a',line_terminator="",header=(not os.path.exists(filename)))



