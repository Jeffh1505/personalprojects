from pyfirmata import Arduino, util
import time

# Establish a serial connection to the Arduino Uno
board = Arduino('COM3')  # Change '/dev/ttyUSB0' to the port your Arduino is connected to

# Define the pin mode as OUTPUT
board.digital[13].mode = pyfirmata.OUTPUT

# Blink the LED 5 times
for i in range(5):
    board.digital[13].write(1)  # Turn ON the LED
    time.sleep(1)  # Wait for 1 second
    board.digital[13].write(0)  # Turn OFF the LED
    time.sleep(1)  # Wait for 1 second

# Close the serial connection
board.exit()
