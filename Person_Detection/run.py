import pickle
import datetime
import pandas as pd
import paho.mqtt.client as mqtt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import ast

# Starting.
print("###### Welcome to wifi person detector ######")

# callback for connecting to the server
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("entc/wifipd")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    try:
        print("-----------------------------")
        print(msg.topic+" "+str(msg.payload))
        data1=msg.payload
        dic = ast.literal_eval(data1.decode("utf-8"))
        #print(dic)
        p = [dic.setdefault("Chamidi1",-100),dic.setdefault("NipunaM1",-100),dic.setdefault("IsuruAp6",-100),dic.setdefault("UoM_Wireless1",-100),dic.setdefault("UNIC-wifi11",-100)]
        p=list(map(int,p))
        print("p",p)
        # Making Predictions
        y_pred = model.predict([p])
        person = 0
        if y_pred[0] == 1:
            person = 1
        elif y_pred[0] == 2:
            person = 5
        
        print(datetime.datetime.now())
        print(str(person) + " person/s detected.")
    except Exception as e:
        print(e)

# Load the model from disk
filename = 'finalized_model.pkl'
file = open(filename, 'rb')
model = pickle.load(file)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("iot.eclipse.org", 1883, 120)
client.loop_forever()
