#include <arduino.h>

//The pin the flame sensor is connected
const int flamePin = A3;

//The range within the fire should be detected
const int flameRange = 75;

//The pin the buzzer is connected to
const int buzzerPin = 11;

int mainFlame;


void setup() 
{
     // Starts up the Arduino and establishes the buzzer as Output
     Serial.begin(9600);
     pinMode(buzzerPin, OUTPUT);
}

void loop() 
{
   // The variable reads from the pin the flame sensor is connected to
   mainFlame = analogRead(flamePin);

   if (mainFlame > flameRange)
   {
       // If the flame is outside the custom set range; 
        
       //The buzzer does not ring
       digitalWrite(buzzerPin, LOW);
        
       //The Variable needed for the messaging system to function is set to 0
       Serial.println("0");
        
       delay(1000);
   }
   else if (mainFlame < flameRange)
   {
       // If the flame is inside the custom set range; 
        
       //The buzzer does start to ring
       digitalWrite(buzzerPin, HIGH);
        
       // The Variable needed for the messaging system to function is set to 1
       Serial.println("1");
        
       delay(1000);
   }
}
