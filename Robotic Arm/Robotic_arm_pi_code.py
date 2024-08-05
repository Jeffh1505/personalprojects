from machine import I2C, Pin
from pca9685 import PCA9685
from servo import Servos
import sys

sda = Pin(0)
scl = Pin(1)
id = 0
i2c = I2C(id=id, sda=sda, scl=scl)

pca = PCA9685(i2c=i2c)
servo = Servos(i2c=i2c)

def set_servo_position(index, position):
    servo.position(index=index, degrees=position)

while True:
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        line = sys.stdin.readline().strip()
        if line:
            parts = line.split(',')
            if len(parts) == 2:
                index, position = int(parts[0]), int(parts[1])
                set_servo_position(index, position)
