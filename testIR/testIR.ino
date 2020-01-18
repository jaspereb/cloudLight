/* dump.ino Example sketch for IRLib2
   Illustrates how to receive an IR signal, decode it and print
   information about it to the serial monitor.
*/
//This includes everything. Not generally recommended.
//It's better to include only the parts of library you really need.
//But for this example it's quick and easy. See "comboDump" example
//for a more efficient way.
#include "IRLibAll.h"
#define IR_PWR 7
#define IR_PIN 4

IRrecv myReceiver(IR_PIN);
IRdecode myDecoder;   

void setup() {
  pinMode(IR_PWR, OUTPUT);
  digitalWrite(IR_PWR, HIGH);

  
  Serial.begin(9600);
  myReceiver.enableIRIn(); // Start the receiver
  Serial.println(F("Ready to receive IR signals"));
}

void loop() {
  //Continue looping until you get a complete signal received
  if (myReceiver.getResults()) {
    myDecoder.decode();           //Decode it
    //myDecoder.dumpResults(false);  //Now print results. Use false for less detail
    myReceiver.enableIRIn();      //Restart receiver
    Serial.println(myDecoder.value, HEX);
    
  }
  //delay(1000);
}
