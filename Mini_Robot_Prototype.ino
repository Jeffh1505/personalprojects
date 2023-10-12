#include <Servo.h>

#define trigPin 9
#define echoPin 10
#define motorPin1 3
#define motorPin2 4
#define motorEnablePin 5
#define servoPin 12
#define joyPinX A0
#define joyPinY A1

const int motorSpeed = 200;  // Adjust the motor speed as needed

Servo servoMotor;

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(motorEnablePin, OUTPUT);
  servoMotor.attach(servoPin);
}

void loop() {
  long duration, distance;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = (duration / 2) / 29.1;

  if (distance < 20) {  // Adjust the threshold distance as needed
    // Rotate the motor in the clockwise direction
    digitalWrite(motorPin1, HIGH);
    digitalWrite(motorPin2, LOW);
    analogWrite(motorEnablePin, motorSpeed);
  } else if (distance > 50) {  // Adjust the threshold distance as needed
    // Rotate the motor in the counterclockwise direction
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, HIGH);
    analogWrite(motorEnablePin, motorSpeed);
  } else {
    // Stop the motor
    digitalWrite(motorPin1, LOW);
    digitalWrite(motorPin2, LOW);
    analogWrite(motorEnablePin, 0);
  }

  int joyX = analogRead(joyPinX);
  int joyY = analogRead(joyPinY);

  int servoAngle = map(joyX, 0, 1023, 0, 180);
  servoMotor.write(servoAngle);

  delay(10);
}
