from cryptography.fernet import Fernet
import PySimpleGUI as sg

def generate_key():
    # Generate a new encryption key
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    # Load the encryption key from the file
    with open("key.key", "rb") as key_file:
        return key_file.read()

def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message)
    return decrypted_message.decode()

# Check if the encryption key file exists, otherwise generate a new key
try:
    key = load_key()
except FileNotFoundError:
    generate_key()
    key = load_key()

layout = [
    [sg.Text("Enter the message to encrypt:")],
    [sg.Input(key="-MESSAGE-")],
    [sg.Button("Encrypt"), sg.Button("Decrypt")],
    [sg.Text("Result:"), sg.Input(key="-RESULT-", readonly=True)],
]

window = sg.Window("Encryptor", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "Encrypt":
        message = values["-MESSAGE-"]
        encrypted_message = encrypt_message(message, key)
        window["-RESULT-"].update(encrypted_message.decode())

    if event == "Decrypt":
        encrypted_message = values["-MESSAGE-"]
        decrypted_message = decrypt_message(encrypted_message.encode(), key)
        window["-RESULT-"].update(decrypted_message)

window.close()
