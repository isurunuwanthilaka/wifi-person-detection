# Person-Detection Using Wifi

## This project is to develop person detection inside a room with existing wifi router.

ESP8266 [Scan for SSID and RSSI] -----------> MQTT central server [iot.eclipse.org]
							|
							|
							|
							v
						Python MQTT client [Data Collection]
							|
							|
							|
							v
	Ardbuino Uno <------------------- Model Trainning [SVM] 
[Display Person Availability]
