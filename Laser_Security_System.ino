int ldr = 0; //analog pin to which LDR is connected
int ldr_value = 0; //variable to store LDR values
const int LED = 9;

void setup() {
  Serial.begin(9600); //start the serial monitor
  pinMode(9, OUTPUT);
}

void loop() {
  ldr_value = analogRead(ldr); //reads the LDR values
  Serial.println(ldr_value); //prints the LDR values to serial monitor
  delay(100); //wait

  if (ldr_value < 600) {
    digitalWrite(9, HIGH);
  } else {
    digitalWrite(9, LOW);
  }

}