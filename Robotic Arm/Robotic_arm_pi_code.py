from machine import I2C, Pin, ADC
from pca9685 import PCA9685
from servo import Servos
import time

# Initialize I2C for PCA9685
sda = Pin(0)
scl = Pin(1)
i2c = I2C(0, sda=sda, scl=scl)

# Initialize PCA9685 and Servos
pca = PCA9685(i2c=i2c)
servo = Servos(i2c=i2c)

# Define the joystick pins
joystick_x = ADC(Pin(26))  # Analog pin for X-axis
joystick_y = ADC(Pin(27))  # Analog pin for Y-axis
button = Pin(15, Pin.IN, Pin.PULL_UP)  # Button pin

# Define the potentiometer pin
potentiometer = ADC(Pin(28))  # Analog pin for potentiometer

# Servo positions
SERVO_1_UP = 90
SERVO_1_DOWN = 0
SERVO_2_UP = 90
SERVO_2_DOWN = 0
SERVO_3_MIN = 0    # Minimum position for the third servo
SERVO_3_MAX = 180  # Maximum position for the third servo
CLAW_OPEN = 0
CLAW_CLOSED = 90

# Define servo position
def set_servo_position(index, position):
    servo.position(index=index, degrees=position)

# Function to read joystick values
def read_joystick():
    x_value = joystick_x.read_u16()  # Read X-axis value (0 to 65535)
    y_value = joystick_y.read_u16()  # Read Y-axis value (0 to 65535)
    return x_value, y_value

# Function to read potentiometer value
def read_potentiometer():
    pot_value = potentiometer.read_u16()  # Read potentiometer value (0 to 65535)
    # Map potentiometer value to servo position
    mapped_position = int((pot_value / 65535) * (SERVO_3_MAX - SERVO_3_MIN) + SERVO_3_MIN)
    return mapped_position

# Main control loop
while True:
    try:
        x_value, y_value = read_joystick()
        pot_position = read_potentiometer()

        # Map joystick values to servo positions
        if y_value < 32768:  # Joystick moved up
            set_servo_position(3, SERVO_1_UP)  # Move link 1 up
        else:
            set_servo_position(3, SERVO_1_DOWN)  # Move link 1 down

        if x_value < 32768:  # Joystick moved left
            set_servo_position(2, SERVO_2_UP)  # Move link 2 up
        else:
            set_servo_position(2, SERVO_2_DOWN)  # Move link 2 down

        # Control the third servo with the potentiometer
        set_servo_position(1, pot_position)

        # Control the claw mechanism
        if not button.value():  # Button pressed
            set_servo_position(0, CLAW_CLOSED)  # Close claw
        else:
            set_servo_position(0, CLAW_OPEN)  # Open claw

        time.sleep(0.1)  # Small delay to avoid overwhelming the system

    except KeyboardInterrupt:
        print("Program interrupted")
        break
    except Exception as e:
        print(f"Error: {e}")
