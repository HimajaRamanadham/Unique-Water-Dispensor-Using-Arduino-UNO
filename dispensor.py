#include <LiquidCrystal.h>

LiquidCrystal led(12, 11, 5, 4, 3, 2); // set the LCD address to 0x3F for a 16 chars and 2 line display

const int trigPin = 6; // Trigger pin of the ultrasonic sensor const int echoPin = 7; // Echo pin of the ultrasonic sensor

int buzzer = 9;

int motor = 8; char incomingByte;

void setup() {

Serial.begin(9600); // Initialize serial communication

lcd.begin(16, 2); // Initialize the LCD display

pinMode(trigPin, OUTPUT);

pinMode(buzzer, OUTPUT);

pinMode(motor, OUTPUT);

lcd.clear();

}

void loop() {

// Trigger the ultrasonic sensor

digitalWrite(trigPin, LOW);

delayMicroseconds(2);

digitalWrite(trigPin, HIGH);

delayMicroseconds(10);

digitalWrite(trigPin, LOW);

// Measure the duration of the echo pulse long duration = pulseln(echoPin, HIGH);

// Calculate the distance in centimeters float distance = duration 0.034/2;

if (distance > 10) {

lcd.clear();

lcd.setCursor(0, 0); lcd.print("PLACE YOUR GLASS"); delay(1000); lcd.clear();

}

if (distance < 10) {

lcd.setCursor(0, 0); lcd.print(" HOW MUCH WATER"); }

lcd.setCursor(0, 1);

lcd.print(" YOU WANT ");

 if (Serial.available() > 0) {
 incomingByte = Serial.read();
 if (incomingByte == '1') {
 if (distance < 10) {
 Serial.println("Received: 1");
 lcd.clear();
 lcd.setCursor(0, 0);
 lcd.print("Filling Water...");
 digitalWrite(motor, HIGH);
 delay(4580);
 digitalWrite(motor, LOW);
 delay(1000);
 }
 }
 else if (incomingByte == '2') {
 lcd.clear();
 lcd.setCursor(0, 0);
 lcd.print("Filling Water...");
 digitalWrite(motor, HIGH);
 delay(9000);
 digitalWrite(motor, LOW);
 Serial.println("Received: 2");
 }
 else if (incomingByte == '3') {
 lcd.clear();
 lcd.setCursor(0, 0);
 lcd.print("Filling Water...");
 digitalWrite(motor, HIGH);
 delay(13500);
 digitalWrite(motor, LOW);
 Serial.println("Received: 3");
 }
 else if (incomingByte == '4') {
 lcd.clear();
 lcd.setCursor(0, 0);
 lcd.print("Filling Water...");
 digitalWrite(motor, HIGH);
 delay(18000)
digitalWrite(motor, LOW);
 Serial.println("Received: 4");
 }
 else if (incomingByte == '5') {
 lcd.clear();
 lcd.setCursor(0, 0);
 lcd.print("Filling Water...");
 digitalWrite(motor, HIGH);
 delay(22500);
 digitalWrite(motor, LOW);
 Serial.println("Received: 5");
 }
 else if (incomingByte == '6') {
 lcd.clear();
 lcd.setCursor(0, 0);
 lcd.print("Filling Water...");
 digitalWrite(motor, HIGH);
 delay(22500);
 digitalWrite(motor, LOW);
 Serial.println("Received: 5");
 }
 }
}