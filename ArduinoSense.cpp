#include <arduino.h>

const int flamePin = A0;
const int flameRange = 75;

const int buzzerPin = 11;

int mainFlame;


void setup() 
{
     Serial.begin(9600);
     pinMode(buzzerPin, OUTPUT);
}

void loop() 
{
   mainFlame = analogRead(flamePin);

   if (mainFlame > flameRange)
   {
       digitalWrite(buzzerPin, LOW);
       Serial.println("0");
       delay(1000);
   }else if (mainFlame < flameRange)
   {
       digitalWrite(buzzerPin, HIGH);
       Serial.println("1");
       delay(1000);
   }
}
