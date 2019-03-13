import pickle
import datetime
import pandas as pd
import paho.mqtt.client as mqtt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# The callback for when the client receives a CONNACK response from the server.
print("###### Welcome to wifi person detector ######")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("entc/wifipd")

# The callback for when a PUBLISH message is received from the server.


def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    txt = str(msg.payload)
    txt=txt[2:-1]
    p=list(map(int,txt.strip().split(",")))
    #print(p)
    # Making Predictions
    y_pred = model.predict([p])
    person = 0
    if y_pred[0] == 1:
        person = 1
    elif y_pred[0] == 2:
        person = 5
    
    print(datetime.datetime.now())
    print(str(person) + " person/s detected.")

# load the model from disk
filename = 'finalized_model.pkl'
file = open(filename, 'rb')
model = pickle.load(file)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect('localhost', 1883, 60)
client.loop_forever()
