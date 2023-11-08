import random
import csv
import cowsay
from weather_functionality import get_weather
dictionary = []
number_list = []
countries = {}

# Open files

with open(r"C:\Users\summe\OneDrive\Desktop\personalprojects\ChatBot\dictionary.txt", 'r') as file:
    for line in file:
        dictionary.append(line.strip())
for i in range(101):
    number_list.append(int(i))


with open(r"C:\Users\summe\OneDrive\Desktop\personalprojects\ChatBot\country-list.csv", 'r') as country_file:
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
        self.country = list(countries.keys())
        self.weather = get_weather()

    def respond(self, message):
        if message == "hello" or message == "hi" or message == "hey":
            return random.choice(self.greetings)
        elif message == "bye":
            return "Goodbye!"
        elif message == "give me a random word" or message == "random word":
            return f"Your random word is {random.choice(self.random_words)}."
        elif message == "give me a random number" or message == "random number":
            return f"Your random number is {random.choice(self.random_number)}."
        elif message == "give me a random country" or message == "random country":
            random_country = random.choice(self.country)
            return f"Your random country is {random_country} whose capital is {countries[random_country]}."
        elif message == "Get me the weather" or message == "weather" or message == "What's the weather?":
            return self.weather
        elif message == "random":
            random_choice = random.choice([0, 1, 2, 3])
            if random_choice == 0:
                return f"Your random number is {random.choice(self.random_number)}."
            elif random_choice == 1:
                return f"Your random word is {random.choice(self.random_words)}."
            elif random_choice == 2:
                random_country = random.choice(self.country)
                return f"Your random country is {random_country} whose capital is {countries[random_country]}."
            elif random_choice == 3:
                return self.weather

try:
    chatbot = Chatbot()
    exit = True
    print('beavis, cheese ,cow, daemon, dragon, fox, ghostbusters, kitty, meow, miki, milk, octopus, pig, stegosaurus, stimpy, trex, turkey, turtle, tux')
    chatbot_representation = input("Please pick which animal you would like your Chat bot to look like from the list: ")
    if chatbot_representation == "random":
        chatbot_representation = random.choice(['beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty',
    'meow', 'miki', 'milk', 'octopus', 'pig', 'stegosaurus', 'stimpy', 'trex', 
    'turkey', 'turtle', 'tux'])
    while exit:
        message = input("What would you like to say to the chatbot? ").lower()
        response = chatbot.respond(message)
        if message == "bye":
            exit = False
        if chatbot_representation == "cow":
            print(cowsay.get_output_string(chatbot_representation, f"Mooo! {response} Mooo!"))
        else:
            print(cowsay.get_output_string(chatbot_representation, response))
except TypeError:
    print("That is not a valid input.")