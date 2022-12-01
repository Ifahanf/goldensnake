# GOLDEN SNAKES
FITRA HANIFAH (MATRIC) <br />
AUDREY SHINE ELYSIA (A19EE0454) <br />
MUHAMMAD RAFIZARD ACHWAN (A18KE0322) <br />
MUHAMMAD HIRO SAKA NEGARA (A18KE0320) <br />


# Stage 2
<ol type="1">
  <li><a href = "https://github.com/Ifahanf/goldensnake/blob/master/README.md/##10-Problem-Statement">Problem Statement</a></li>
  <li><a href = "https://github.com/Ifahanf/goldensnake/blob/master/README.md/##20-System-Architecture">System Architecture</a></li>
  <li><a href = "https://www.google.com">Sensor</a></li>
  <li><a href = "https://www.google.com">Cloud Platform</a></li>
  <li><a href = "https://www.google.com">Dashboard</a></li>
</ol>

## 1.0 Problem Statement

There are several working environments that typically have high heat and humidity. 
The cause of the situation is usually due to appliances used in the working process which have a heat source. 
Some of the examples of the appliances are furnace, stove and oven where it is typically used in bakeries, kitchen, paper production, to iron mills. 
Other than that, the weather and sunlight also could contribute to rising temperatures in the working environment. 
Surely, a long exposure of heat will risk workers’ health. 
Then, this matter became one of a focus for occupational safety and health administration as it causes issues towards many workers across fields. 
To solve the problem, the air flow should be increased in order to reduce the temperature and humidity. 
Afterwards, to conserve energy, the control of the air flow should be adjusted based on the current temperature.

## 2.0 System Architecture

![alt text](https://github.com/Ifahanf/goldensnake/blob/master/Swimlane%20Diagram.jpg?raw=true)

<br> Sensor: DHT 22/11 <br>
Microcontroller: ESP8266 for HTTP client library<br>
Data transmission protocol: HTTP<br>
Ingest data: Flask<br>
Storage: Google Cloud<br>



## 3.0 Sensor

Proposed Device: DHT22 and ESP32 <br />
Data Transmission: HTTP <br />
![alt text](https://github.com/Ifahanf/goldensnake/blob/master/DHT22%20and%20ESP32.jpg?raw=true)<br />

## 4.0 Cloud Platform

Link Video: https://youtu.be/l2CTqgiERM4

## 5.0 Dashboard

![alt text](https://github.com/Ifahanf/goldensnake/blob/master/Screen%20Shot%202022-11-27%20at%2018.19.04.png?raw=true)




Library for http by using ESP8266 Nodemcu 

#include <Arduino.h> <br />
#include <ESP8266HTTPClient.h> <br />
#include <ESP8266HTTPUpdateServer.h> <br />
#include <ESP8266HTTPUpdateServer-impl.h> <br />
