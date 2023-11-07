import random
dictionary = []
with open(r"C:\Users\summe\OneDrive\Desktop\E1006\dictionary.txt", 'r') as file:
    for line in file:
        dictionary.append(line.strip())


class Chatbot:

    def __init__(self):
        self.responses = ["Hi there!", "How can I help you?", "I'm not sure what you mean."]

    def respond(self, message):
        if message == "hello":
            return "Hi there!"
        elif message == "bye":
            return "Goodbye!"
        else:
            return random.choice(self.responses)

chatbot = Chatbot()
exit = True
while exit:
    message = input("What would you like to say to the chatbot? ")
    response = chatbot.respond(message)
    if message == "bye":
        exit = False
    print(response)