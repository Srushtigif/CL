const int pirPin = 2; // PIR sensor output pin
const int ledPin = 9; // LED pin
const int buzPin = 3;
int motionState = LOW; // Initial state of motion
void setup() {
Serial.begin(9600); // Start serial communication
pinMode(pirPin, INPUT); // Set PIR sensor pin as input
pinMode(ledPin, OUTPUT); // Set LED pin as output
pinMode(buzPin, OUTPUT);
}
void loop() {
motionState = digitalRead(pirPin); // Read PIR sensor state
if (motionState == HIGH) {
digitalWrite(ledPin, LOW); // Turn on LED
digitalWrite(buzPin, LOW);

delay(100); // Delay to prevent flooding Serial Monitor
} else {
digitalWrite(ledPin, HIGH); // Turn off LED
digitalWrite(buzPin, HIGH);
}
delay(100); // Small delay to improve responsiveness
}