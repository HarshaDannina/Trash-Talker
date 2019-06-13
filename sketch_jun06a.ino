#include <BoltDeviceCredentials.h>
#include <BoltIoT-Arduino-Helper.h>


#include <Ultrasonic.h>

Ultrasonic ultrasonic(12, 13);

void setup() {
  Serial.begin(9600);
  boltiot.begin(Serial);
  }

void loop() {
  float senData = ultrasonic.read();
  int sensor = int(senData);
  //Serial.println(sensor);
  boltiot.processPushDataCommand(sensor);
  delay(500);
  
}
