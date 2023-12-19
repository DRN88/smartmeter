#include <ElegantOTA.h>

// ESP Specific START - Do not edit
#define ESP8266
#if defined(ESP8266)
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#elif defined(ESP32)
#include <WiFi.h>
#include <WiFiClient.h>
#include <WebServer.h>
#endif
#if defined(ESP8266)
ESP8266WebServer server(80);
#elif defined(ESP32)
WebServer server(80);
#endif
// ESP Specific END - Do not edit

//
// VARIABLES
//
// WIFI START
const char* ssid = "MySSID";
const char* password = "MyPassw0rd";
// WIFI END
String serialRawData;
unsigned long wifiPreviousMillis = 0;
unsigned long wifiInterval = 30000;
//

void setup(void)
{
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }
  server.on("/", []() {
    server.send(200, "text/plain", "List of endpoints: /meter, /update");
  });
  server.on("/meter", []() {
    server.send(200, "text/plain", serialRawData);
  });
  ElegantOTA.begin(&server);
  server.begin();
}

void loop(void)
{
  if (Serial.available() > 0) {
    serialRawData = Serial.readString();
  }
  server.handleClient();
  ElegantOTA.loop();
  reconnectWifi();
}

void reconnectWifi()
{
  unsigned long wifiCurrentMillis = millis();
  if ((WiFi.status() != WL_CONNECTED) && (wifiCurrentMillis - wifiPreviousMillis >= wifiInterval)) {
    WiFi.disconnect();
    WiFi.reconnect();
    wifiPreviousMillis = wifiCurrentMillis;
  }
}


