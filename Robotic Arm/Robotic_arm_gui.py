import tkinter as tk
import serial

class ServoControlApp:
    def __init__(self, master, serial_port):
        self.master = master
        self.master.title("Servo Control")

        self.serial_port = serial.Serial(serial_port, 115200, timeout=1)

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
        command = f"{servo_index},{position}\n"
        self.serial_port.write(command.encode())

if __name__ == "__main__":
    serial_port = "COM3"  # Update this to the correct port for your setup
    root = tk.Tk()
    app = ServoControlApp(master=root, serial_port=serial_port)
    root.mainloop()
