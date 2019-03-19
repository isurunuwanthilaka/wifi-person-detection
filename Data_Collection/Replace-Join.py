import pandas as pd
import operator
import random
import os

# 1.preparing 
files=[x for x in os.listdir('.') if 'wifi_data' in x]
for filename in files:
        df=pd.read_csv(filename)
        print(filename)

        for i in df.columns:
                if i=='id':
                        continue
                
                temp=df[i].value_counts().to_dict()
                sorted_x = sorted(temp.items(), key=operator.itemgetter(1))
                arr=[]
                for j in sorted_x[-4:]:
                        if j[0]!=-100:
                                arr.append(int(j[0]))
                if len(arr)==3:
                        df=df.replace({i:-100},random.choice(arr[-3:]))
                elif len(arr)==2:
                        df=df.replace({i:-100},random.choice(arr[-2:]))
                elif len(arr)==1:
                        df=df.replace({i:-100},random.choice(arr))       

        df.to_csv("cleaned_"+filename)

# 2.joining cleaned data sets 
filename="final-data-set.csv"

data0 = pd.read_csv("cleaned_wifi_data0.csv")[['Chamidi1','NipunaM6','IsuruAp6','UoM_Wireless11','UNIC-wifi11','id']]
data1 = pd.read_csv("cleaned_wifi_data01.csv")[['Chamidi1','NipunaM6','IsuruAp6','UoM_Wireless11','UNIC-wifi11','id']]
data2 = pd.read_csv("cleaned_wifi_data02.csv")[['Chamidi1','NipunaM6','IsuruAp6','UoM_Wireless11','UNIC-wifi11','id']]
data3 = pd.read_csv("cleaned_wifi_data10.csv")[['Chamidi1','NipunaM6','IsuruAp6','UoM_Wireless11','UNIC-wifi11','id']]
data4 = pd.read_csv("cleaned_wifi_data11.csv")[['Chamidi1','NipunaM6','IsuruAp6','UoM_Wireless11','UNIC-wifi11','id']]
data5 = pd.read_csv("cleaned_wifi_data21.csv")[['Chamidi1','NipunaM6','IsuruAp6','UoM_Wireless11','UNIC-wifi11','id']]
data6 = pd.read_csv("cleaned_wifi_data22.csv")[['Chamidi11','NipunaM6','IsuruAp6','UoM_Wireless1','UNIC-wifi11','id']]
data6.columns=['Chamidi1','NipunaM6','IsuruAp6','UoM_Wireless11','UNIC-wifi11','id']

data0 = data0.append(data1)
data0 = data0.append(data2)
data0 = data0.append(data3)
data0 = data0.append(data4)
data0 = data0.append(data5)
df = data0.append(data6)

df = df.sample(frac=1).reset_index(drop=True)

df.to_csv(filename,index=False,mode='a',line_terminator="",header=(not os.path.exists(filename)))
