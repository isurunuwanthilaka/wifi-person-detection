/*
 *  This sketch demonstrates how to scan WiFi networks. 
 *  The API is almost the same as with the WiFi Shield library, 
 *  the most obvious difference being the different file you need to include:
 */
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// Update these with values suitable for your network.

String id="1";

const char* ssid = "IsuruAp";
const char* password = "Isuru1995";
const char* mqtt_server = "192.168.43.205";
const char* outTopic="entc/wifipd";

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[1024];
int value = 0;

void setup() {
   pinMode(BUILTIN_LED, OUTPUT);     // Initialize the BUILTIN_LED pin as an output
  Serial.begin(115200);
  //setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  Serial.println("Setup done");
}

void loop() {
  scanWifi();
  connectSend();
  delay(500);
}

void connectSend() {
  WiFi.mode(WIFI_STA);
  delay(100);
  setup_wifi();
  delay(100);
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("ESP8266Client")) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish(outTopic, msg);
      Serial.print("published");
      Serial.print(msg);
      // ... and resubscribe
     // client.subscribe("inTopic");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}
//{"id" : "1","UoM_Wireless1" : "-55","FaryLink_61AEB41" : "-52","UoM_Wireless1" : "-80","eduroam1" : "-54","FaryLink_4374501" : "-63","eduroam1" : "-79","iot1" : "-53","Jungle Book10" : "-71","HUAWEI nova 2i11" : "-85"}

void scanWifi(){
   // Set WiFi to station mode and disconnect from an AP if it was previously connected
   WiFi.mode(WIFI_STA);
   WiFi.disconnect();
   delay(100);
   Serial.println("scan start");
  /*clear the buffer and load data*/
  memset(msg,1024,0);
  String str="";
  str+='{';
  str+="\"id\" : \"";
  str+=id;
  str+="\",";



  // WiFi.scanNetworks will return the number of networks found
  int n = WiFi.scanNetworks();
  Serial.println("scan done");
  if (n == 0)
    Serial.println("no networks found");
  else
  {
    Serial.print(n);
    Serial.println(" networks found");
    for (int i = 0; i < n; ++i)
    {
      str+='\"';
      str+=WiFi.SSID(i)+WiFi.channel(i);
      str+="\" : \"";
      str+=WiFi.RSSI(i);
      str+="\"";

      if(i<n-1)
       str+=',';
      
      // Print SSID and RSSI for each network found
      Serial.print(i + 1);
      Serial.print(": ");
      Serial.print(WiFi.SSID(i));
      Serial.print(" (");
      Serial.print(WiFi.RSSI(i));
      Serial.print(")");
      Serial.println((WiFi.encryptionType(i) == ENC_TYPE_NONE)?" ":"*");
      delay(10);
    }
  }
  str+='}';
  
  Serial.println(str);
  str.toCharArray(msg,1024);
  // Wait a bit before scanning again
}



void setup_wifi() {

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
<<<<<<< HEAD:NodeMCU/Person_Detection.ino
}
=======
}
>>>>>>> 53d9f83403d41b9568b7f206d829c637a0d443aa:Person_Detection/Person_Detection.ino
