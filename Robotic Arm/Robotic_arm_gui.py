import tkinter as tk
from tkinter import messagebox, simpledialog
import serial
import serial.tools.list_ports

class ServoControlApp:
    def __init__(self, master, serial_port):
        self.master = master
        self.master.title("Servo Control")

        try:
            self.serial_port = serial.Serial(serial_port, 115200, timeout=1)
        except serial.SerialException as e:
            messagebox.showerror("Error", f"Could not open serial port {serial_port}: {e}")
            self.master.destroy()
            return

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
    # List available COM ports and ask user to select one
    ports = list(serial.tools.list_ports.comports())
    if not ports:
        print("No COM ports found")
        sys.exit()

    port_list = [p.device for p in ports]
    print("Available COM ports:")
    for i, port in enumerate(port_list):
        print(f"{i}: {port}")

    # Ask the user to select a COM port
    selected_port_index = simpledialog.askinteger("Select COM port", "Enter the index of the COM port:", minvalue=0, maxvalue=len(port_list) - 1)
    if selected_port_index is None:
        print("No COM port selected")
        sys.exit()

    serial_port = port_list[selected_port_index]

    root = tk.Tk()
    app = ServoControlApp(master=root, serial_port=serial_port)
    root.mainloop()
