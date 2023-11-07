import random
import csv
dictionary = []
number_list = []
countries = {}
with open(r"C:\Users\summe\OneDrive\Desktop\E1006\dictionary.txt", 'r') as file:
    for line in file:
        dictionary.append(line.strip())
for i in range(101):
    number_list.append(int(i))



with open(r"C:\Users\summe\Downloads\country-list.csv", 'r') as country_file:
    reader = csv.reader(country_file)
    for row in reader:
        country, capital, type = row
        countries.setdefault(country, capital)




#Create the ChatBot class

class Chatbot:

    def __init__(self):
        self.greetings = ["Hi there!", "How can I help you?", "Hows it going?", "Hello there!", "Hey!"]
        self.random_words = dictionary
        self.random_number = number_list
        self.country = countries

    def respond(self, message):
        if message == "hello" or message == "hi" or message == "hey":
            return random.choice(self.greetings)
        elif message == "bye":
            return "Goodbye!"
        elif message == "Give me a random word":
            return f"Your random word is {random.choice(self.random_words)}."
        elif message == "Give me a random number":
            return f"Your random number is {random.choice(self.random_number)}"
        elif message == "Give me a random country":
            return f"Your random country is {random.choice(self.country)}"
        elif message == "random":
            random_choice = random.choice([0, 1])
            if random_choice == 0:
                return f"Your random number is {random.choice(self.random_number)}"
            elif random_choice == 1:
                return f"Your random word is {random.choice(self.random_words)}."

chatbot = Chatbot()
exit = True
while exit:
    message = input("What would you like to say to the chatbot? ")
    response = chatbot.respond(message)
    if message == "bye":
        exit = False
    print(response)