#include <SparkFunESP8266WiFi.h>

const char mySSID[] = "n3tw3rk";
const char myPSK[] = "myn3tw3rkb3tw3rkin";

define STRING_BUFFER_SIZE 1024;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial1.begin(115200);
  Serial1.write("At\n\r");
  delay(200);
  Serial1.write("AT+CWMODE=3\n\r");
  delay(200)
  Serial1.write("AT+CWSAP=\"moarcoffee\",\"123\",5,0");
}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available()) { Serail1.write(Serial.read()); }
  while (Serial1.available()) { Serial.write(Serial1.read(); }
  }
}
