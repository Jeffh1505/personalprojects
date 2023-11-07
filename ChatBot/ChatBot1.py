import random
dictionary = []
with open(r"C:\Users\summe\OneDrive\Desktop\E1006\dictionary.txt", 'r') as file:
    for line in file:
        dictionary.append(line.strip())


class Chatbot:

    def __init__(self):
        self.greetings = ["Hi there!", "How can I help you?", "I'm not sure what you mean."]
        self.random_words = dictionary

    def respond(self, message):
        if message == "hello" or message == "hi" or message == "hello":
            return random.choice(self.greetings)
        elif message == "bye":
            return "Goodbye!"
        elif message == "Give me a random word" or message == "random":
            return random.choice(self.random_words)

chatbot = Chatbot()
exit = True
while exit:
    message = input("What would you like to say to the chatbot? ")
    response = chatbot.respond(message)
    if message == "bye":
        exit = False
    print(response)