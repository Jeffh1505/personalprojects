import tkinter as tk

window = tk.Tk()
window.title("My Window")
window.geometry("300x300")

label = tk.Label(window, text="Hello, world!")
label.pack()

entry = tk.Entry(window)
entry.pack()

def on_click():
    print(entry.get())

button = tk.Button(window, text="Click me!", command=on_click)
button.pack()

window.mainloop()