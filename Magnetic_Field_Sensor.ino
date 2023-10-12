#include <Adafruit_SSD1306.h>
#include <Adafruit_GFX.h>

#define ANALOG_PIN A0

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

void setup() {
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.display();
  delay(2000);
  display.clearDisplay();

  pinMode(ANALOG_PIN, INPUT);
}

void loop() {
  int sensorValue = analogRead(ANALOG_PIN);
  float magneticField = map(sensorValue, 0, 1023, -2000, 2000);  // Map analog value to magnetic field range (-2000 to 2000)

  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.print("Magnetic Field: ");
  display.print(magneticField);
  display.println(" Gauss");
  display.display();

  delay(1000);
}
