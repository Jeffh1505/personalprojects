from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
import cowsay
import math
import sympy as sym
import random
from openai import OpenAI
class ChatBot:
    def __init__(self):
        self.model_type = 'gpt2-xl'
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = GPT2LMHeadModel.from_pretrained(self.model_type)
        self.model.config.pad_token_id = self.model.config.eos_token_id  # suppress a warning

    #This is the generative portion of the chatbot using the GPT2 model
    def generate(self, prompt='', num_samples=10, steps=40, temperature=0.7):
        import openai
        
        # OpenAI API key
        api_key = "YOUR_API_KEY"  # Replace with your actual OpenAI API key
        
        # Set up the OpenAI API client
        openai.api_key = api_key

        # Prepare the request payload
        prompt_text = f"{prompt}\nChatbot:"

        response = openai.ChatCompletion.create(
            model="text-davinci-003",
            messages=[
                {"role": "user", "content": prompt_text},
                {"role": "assistant"}
            ],
            max_tokens=steps,
            temperature=temperature,
            n=num_samples
        )
        
        # Collect generated responses
        outputs = [message['content'] for message in response['messages'][1:]]

        for output in outputs:
            print(cowsay.get_output_string("cow", output))

    #Gets the weather for a specified place (Be it a specific address or a city)
    def get_weather(self, user_location):
        import requests
        
        #Dictionary of famous landmarks in each city to get the cooridnates to pass into the weather api 
        # (i.e. New York has the Empire State Building, Washington DC has the White House)
        cities = {"New York": "20 W 34th St., New York, NY 10001", "Los Angeles": "1111 S Figueroa St, Los Angeles, CA 90015"
                , "Chicago": "233 S Wacker Dr, Chicago, IL 60606", "San Francisco": "600 Montgomery St, San Francisco, CA 94111",
                "Houston": "2800 Post Oak Blvd, Houston, TX 77056", "Miami":" 1 Washington Ave, Miami Beach, FL 33139", 
                "Philadelphia": "520 Chestnut St, Philadelphia, PA 19106", "Seattle": "400 Broad St, Seattle, WA 98109", 
                "Boston": "206 Washington St, Boston, MA 02109", "Washington DC": "1600 Pennsylvania Avenue NW, Washington, DC 20500", 
                "Columbia University": "116th and Broadway, New York, NY 10027"}
        if user_location in cities.keys():
            user_location = cities[user_location]
        address_url = f'https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address={user_location}&benchmark=2020&format=json'
        response1 = requests.get(address_url)
        if response1.status_code == 200:
            data1 = response1.json()

        else:
            return "Invalid Location."
        latitude = str(data1['result']['addressMatches'][0]['coordinates']['y'])[:-10]
        longitude = str(data1['result']['addressMatches'][0]['coordinates']['x'])[:-10]

        url1 = f'https://api.weather.gov/points/{latitude},{longitude}'
        response2 = requests.get(url1)
        if response2.status_code == 200:
            data = response2.json()
            forecast_link = data['properties']['forecast']
        else: 
            return "Invalid location"

        response3 = requests.get(forecast_link)
        if response3.status_code == 200:
            data2 = response3.json()
            forecast = data2['properties']['periods'][0]['detailedForecast']
            return print(cowsay.get_output_string("cow",f"Today's forecast: {forecast}"))
        else:
            return print(cowsay.get_output_string("cow","Forecast not found"))
        
    #Performs basic mathematical operations     
    def basic_calculator(self, user_input):

        #Implements raising a number to a power
        if "**" in user_input:
            x, z = user_input.split("**")
            x = float(x)
            z = float(z)
            return print(cowsay.get_output_string("cow", f"{x} raised to {z} = {x ** z}"))
        
        #Implements the square root of a number
        elif "sqrt" in user_input or "square root" in user_input:
            if "sqrt" in user_input:
                x = float(user_input.split("sqrt")[1])
            else:
                x = float(user_input.split("square root")[1])

            return print(cowsay.get_output_string("cow", f"Square root of {x} = {math.sqrt(x)}"))
        
        #Implements all other mathematical operations
        else:
            x, y, z = user_input.split(" ")
            x = float(x)
            z = float(z)
            if y == "+":
                return print(cowsay.get_output_string("cow", f"{x} + {z} = {x + z}"))
            elif y == "-":
                return print(cowsay.get_output_string("cow", f"{x} - {z} = {x - z}"))
            elif y == "*":
                return print(cowsay.get_output_string("cow", f"{x} * {z} = {x * z}"))
            elif y == "/":
                return print(cowsay.get_output_string("cow", f"{x} / {z} = {x / z}"))

    #Performs calculus operations
    def calculus_calculator(self, method, function):
        x = sym.symbols('x')

        #Takes the derivative of a function
        if method.lower() == "derivative":
            derivative = sym.diff(function, x)
            return print(cowsay.get_output_string("cow", f"The derivative of {function} with respect to x is {derivative}"))
        
        #Takes the integral of a function
        elif method.lower() == "integration":
            check_for_limits = input("Would you like to add limits? (y/n): ").lower()
            if check_for_limits == 'y':
                upper_limit = input("What is the upper limit (or 'inf' for infinity)?: ").lower()
                lower_limit = input("What is the lower limit (or '-inf' for negative infinity)?: ").lower()
                
                if upper_limit == 'inf':
                    upper_limit = sym.oo
                else:
                    upper_limit = float(upper_limit)
                
                if lower_limit == '-inf':
                    lower_limit = -sym.oo
                else:
                    lower_limit = float(lower_limit)
                
                definite_integral = sym.integrate(function, (x, lower_limit, upper_limit))
                return print(cowsay.get_output_string("cow", f"The integral of {function} over the interval {lower_limit} to {upper_limit} is {definite_integral}"))
            
            elif check_for_limits == 'n':
                indefinite_integral = sym.integrate(function, x)
                return print(cowsay.get_output_string("cow", f"The indefinite integral of {function} is {indefinite_integral}"))

            else:
                return print(cowsay.get_output_string("cow", "Invalid choice for limits. Please enter 'y' or 'n'."))
        
        #Takes the limit of a function
        elif method.lower() == "limit":
            approaching = input("What is x approaching (or 'inf' for infinity)?: ").lower()
            
            if approaching == 'inf':
                approaching = sym.oo
            else:
                approaching = float(approaching)
            
            limit = sym.limit(function, x, approaching)
            return print(cowsay.get_output_string("cow", f"The limit of {function} as x approaches {approaching} is {limit}"))

        else:
            return print(cowsay.get_output_string("cow", "Invalid method choice. Please choose 'Derivative', 'Integration', or 'Limit'."))
        
    #Gets an image from NASA API
    def space_image(self):
        import requests
        import json
        import webbrowser
        
        params = {"api_key": "auVKThbI6c5rw8C9CXubfHaK2lOiV631jbocLL0F", "hd": True, "count" : 1}    
        f = r"https://api.nasa.gov/planetary/apod?"
        data = requests.get(f, params = params)
        tt = json.loads(data.text)
    
        print(cowsay.get_output_string("cow",tt[0]["title"]))
        webbrowser.open(tt[0]["url"])

    #Creates a code guessing game
    def code_guessing_game(self):
        import random

        code = str(random.randint(1000, 9999))
        
        guessed_codes = []
        correct_numbers = []
        tries = 0

        #Creates game loop
        while True:
            user_input = str(input("Guess the code: ")) #Takes user input

            if user_input in code:
                correct_numbers.append(user_input)
                print(cowsay.get_output_string("cow","Correct guess"))
                if set(correct_numbers) == set(code):
                    print(cowsay.get_output_string("cow",f"You got it, {code} was the code!"))
                    break    
            else: 
                tries += 1
                if tries == 5:
                    print(cowsay.get_output_string("cow",f"You lost, {code} was the code."))
                    break
            part_of_code_to_display = ""
            for number in code:
                if number in correct_numbers:
                    part_of_code_to_display += number
                else: 
                    part_of_code_to_display += "_"
            print(cowsay.get_output_string("cow",part_of_code_to_display))

    #Creates a word guessing game
    def word_guessing_game(self):
        import random
        with open(r"C:\Users\summe\OneDrive\Desktop\E1006\dictionary.txt", 'r') as f:
            words = [line.strip().lower() for line in f]

        word_to_guess = random.choice(words)
        print(word_to_guess)

        guessed_letters = []
        correct_letters = []
        tries = 0

        while True:
            guesser_letter = input("Guess letter: ")

            if guesser_letter not in guessed_letters:
                guessed_letters.append(guesser_letter)
                

            if guesser_letter in word_to_guess:
                correct_letters.append(guesser_letter)
            elif guesser_letter not in word_to_guess:
                tries += 1

            if set(correct_letters) == set(word_to_guess):
                print(cowsay.get_output_string("cow", f"{word_to_guess} is the word!"))
                break

            if tries == 5:
                print(cowsay.get_output_string("cow", f"You lost, {word_to_guess} was the word."))
                break

            word_to_display = ""
            for letter in word_to_guess:
                if letter in correct_letters:
                    word_to_display += letter
                else:
                    word_to_display += "_"
            
            print(cowsay.get_output_string("cow",word_to_display))

    #Gets the headlines from the front page of the New York Times
    def news(self):
        import requests
        from bs4 import BeautifulSoup

        url = 'https://www.nytimes.com/section/todayspaper?redirect_uri=https%3A%2F%2Fwww.nytimes.com%2F'
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            headline_elements = soup.find_all('h3', class_='css-miszbp e1hr934v2')
            
            if headline_elements:
                headlines = []
                for headline_element in headline_elements:
                    headline = headline_element.get_text()
                    headlines.append(headline)
                all_headlines = '\n'.join(headlines)
                print(cowsay.get_output_string("cow",f"Today's headlines:\n {all_headlines} \nSource: The New York Times"))
            else:
                print(cowsay.get_output_string("cow",'Headlines not found on the page.'))
        else:
            print(cowsay.get_output_string("cow",'Failed to fetch the webpage.'))

    


#Main function implements the functionalities of the chatbot class
def main():
    chatbot = ChatBot()
    while True:
        user_input = input("What would you like to say to the chatbot?: ").lower()

        #Checks if user wants to exit
        if user_input.lower() in ['exit', 'quit']:
            print(cowsay.get_output_string("cow", "Goodbye!"))
            break

        #Activates weather functionality
        elif user_input == "get me the weather" or user_input == "weather" or user_input == "what's the weather?":
            user_location = input("Where would you like the weather?: ")
            chatbot.get_weather(user_location)
        
        #Implements calculator functionality
        elif "+" in user_input or "-" in user_input or "*" in user_input or "/" in user_input or "**" in user_input or ("sqrt" or "square root") in user_input:
            chatbot.basic_calculator(user_input)

        #Implements calculus functionality
        elif user_input == "calculus":
            function = input("What is the function?: ")
            method = input("What would you like to do to the function? (Derivative, Integration, Limit): ")
            chatbot.calculus_calculator(method, function)
        
        #Implements functionality to get an image from NASA's website
        elif user_input == "space":
            chatbot.space_image()

        #Implements the functionality for the games associated with the bot, it chooses at random between the two games in the chatbot 
        #class and then begins the game methods
        elif user_input == "game":
            game_to_play = random.randint(1,2)
            if game_to_play == 1:
                chatbot.code_guessing_game()
            elif game_to_play == 2:
                chatbot.word_guessing_game()

        #Implements the news functionality 
        elif user_input == "news" or user_input == "headlines":
            chatbot.news()

        elif user_input == "translate":
            text_to_translate = input("Please input some text to translate: ")
            chatbot.translation(text_to_translate)
        #Implements the generative portion of the chatbot
        else:
            chatbot.generate(user_input)


if __name__ == "__main__":
    main()