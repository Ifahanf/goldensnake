# goldensnake

#include <Arduino.h>
#include <ESP8266WiFi.h>
#include<Firebase_ESP_Client.h>

//Provide the token generation process info.
#include "addons/TokenHelper.h"
//Provide the RTDB payload printing info and other helper functions.
#include "addons/RTDBHelper.h"

// Insert your network credentials
#define WIFI_SSID "Hematech Nusantara"
#define WIFI_PASSWORD "hematech123"

// Insert Firebase project API Key
#define API_KEY "AIzaSyD85-ebAiMu5duQC1TCwMYcO-ntL58FzzY"

// Insert RTDB URLefine the RTDB URL */
#define DATABASE_URL "control-led-1511-default-rtdb.firebaseio.com"

FirebaseData fbdo;
FirebaseAuth auth;
FirebaseConfig config;

unsigned long sendDataPrevMillis =0;
int intValue;
bool signupOK= false;
bool boolValue;

#define LED1 D1
#define LED2 D2
#define LED3 D3
#define LED4 D4
#define LED5 D5

void initLED(){ //setup LED
  pinMode(D1, OUTPUT);
  pinMode(D2, OUTPUT);
  pinMode(D3, OUTPUT);
  pinMode(D4, OUTPUT);
  pinMode(D5, OUTPUT);
}

void setup() {

  initLED();

  Serial.begin(9600);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED){
    Serial.print(".");
  }
  Serial.println();
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
  Serial.println();

  /* Assign the api key (required) */
  config.api_key = API_KEY;

  /* Assign the RTDB URL (required) */
  config.database_url = DATABASE_URL;

  /* Sign up */
  if (Firebase.signUp(&config, &auth, "", "")){
    Serial.println("ok");
    signupOK = true;
  }
  else{
    Serial.printf("%s\n",config.signer.signupError.message.c_str());
  }

  /* Assign the callback function for the long running token generation task */
  config.token_status_callback = tokenStatusCallback; //see addons/TokenHelper.h
  
  Firebase.begin(&config, &auth);
  Firebase.reconnectWiFi(true);
}

void loop() {
   if (Firebase.ready() && signupOK ) {
    sendDataPrevMillis = millis();
    
    if (Firebase.RTDB.getInt(&fbdo, "test/int")) {
      if (fbdo.dataType() == "int") {
        intValue = fbdo.intData();
        Serial.println(intValue);

        if (intValue==true)
        {
          digitalWrite(D10, HIGH);
        }
        else
        {
          digitalWrite(D10, LOW);
        }
      }
      Firebase.RTDB.setString(&fbdo, "test/status", "berhasil");
    }
    else {}

    //for LED1
    if (Firebase.RTDB.getInt(&fbdo, "LED/led1")) {
      if (fbdo.dataType() == "int") {
        intValue = fbdo.intData();
        Serial.println(intValue);

        if (intValue==true)
        {
          digitalWrite(D1, HIGH);
        }
        else
        {
          digitalWrite(D1, LOW);
        }
      }
    }
    else {}
    
    //for LED 2
     if (Firebase.RTDB.getInt(&fbdo, "LED/led2")) {
      if (fbdo.dataType() == "int") {
        intValue = fbdo.intData();
        Serial.println(intValue);

        if (intValue==true)
        {
          digitalWrite(D2, HIGH);
        }
        else
        {
          digitalWrite(D2, LOW);
        }
      }
    }
    else {}

    //for LED 3
     if (Firebase.RTDB.getInt(&fbdo, "LED/led3")) {
      if (fbdo.dataType() == "int") {
        intValue = fbdo.intData();
        Serial.println(intValue);

        if (intValue==true)
        {
          digitalWrite(D3, HIGH);
        }
        else
        {
          digitalWrite(D3, LOW);
        }
      }
    }
    else {}

    //for LED 4

     if (Firebase.RTDB.getInt(&fbdo, "LED/led4")) {
      if (fbdo.dataType() == "int") {
        intValue = fbdo.intData();
        Serial.println(intValue);

        if (intValue==true)
        {
          digitalWrite(D4, HIGH);
        }
        else
        {
          digitalWrite(D4, LOW);
        }
      }
    }
    else {}

    //for LED 5

     if (Firebase.RTDB.getInt(&fbdo, "LED/led5")) {
      if (fbdo.dataType() == "int") {
        intValue = fbdo.intData();
        Serial.println(intValue);

        if (intValue==true)
        {
          digitalWrite(D5, HIGH);
        }
        else
        {
          digitalWrite(D5, LOW);
        }
      }
    }
    else {}
  }
}
