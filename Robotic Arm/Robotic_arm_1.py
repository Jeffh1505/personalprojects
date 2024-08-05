import tkinter as tk
from pca9685 import PCA9685
from machine import I2C, Pin
from servo import Servos

class ServoControlApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Servo Control")

        # Set up the I2C and PCA9685
        sda = Pin(0)
        scl = Pin(1)
        id = 0
        self.i2c = I2C(id=id, sda=sda, scl=scl)
        self.pca = PCA9685(i2c=self.i2c)
        self.servo = Servos(i2c=self.i2c)

        # Create sliders for each servo
        self.create_slider("Claw Servo", 0)
        self.create_slider("Hand Servo", 1)
        self.create_slider("Arm 1 Servo", 2)
        self.create_slider("Arm 2 Servo", 3)

    def create_slider(self, label_text, servo_index):
        frame = tk.Frame(self.master)
        frame.pack()

        label = tk.Label(frame, text=label_text)
        label.pack(side=tk.LEFT)

        slider = tk.Scale(frame, from_=0, to=180, orient=tk.HORIZONTAL, command=lambda pos, idx=servo_index: self.update_servo(idx, pos))
        slider.pack(side=tk.LEFT)

    def update_servo(self, servo_index, position):
        degrees = int(position)
        self.servo.position(index=servo_index, degrees=degrees)

if __name__ == "__main__":
    root = tk.Tk()
    app = ServoControlApp(master=root)
    root.mainloop()
