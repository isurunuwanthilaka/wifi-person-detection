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
    print(msg.topic+" "+str(msg.payload))
    txt = msg.payload

    # Making Predictions
    y_pred = model.predict(map(int, txt.strip().split(",")))
    person = 0
    if y_pred == 1:
        person = 1
    elif y_pred == 2:
        person = 5
    
    print(datetime.datetime.now())
    print(person + " person/s detected.")


# load the model from disk
filename = 'finalized_model.sav'
model = pickle.load(open(filename, 'rb'))

client = mqtt.Client()
client.connect("iot.eclipse.org", 1883, 60)
client.on_connect = on_connect
client.on_message = on_message
