# Person-Detection Using Wifi

## This project is to develop person detection inside a room with existing wifi routers.

This simple application includes following components.

* ESP8266 - Scan for SSID and RSSI [Data Collection]

* MQTT central server [iot.eclipse.org] or Docker Mosquito MQTT server

* Python MQTT client - Subscribe to the relevant topic for data 

* Model Training [SVM or Appropriate ML model]

* Arduino Uno - Display Person Availability