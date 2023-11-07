import random
dictionary = []
with open(r"C:\Users\summe\OneDrive\Desktop\E1006\dictionary.txt", 'r') as file:
    for line in file:
        dictionary.append(line.strip())


class Chatbot:
    def __init__(self, responses, random word):
        self.responses = random.choice(["Hello!", "Hi!", "Hows it going?"])