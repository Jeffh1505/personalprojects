import pyfirmata2
board = pyfirmata2.Arduino('COM3')
ledpin = board.get_pin('d:13:p')

for i in range(5):
    ledpin.write(1.0)