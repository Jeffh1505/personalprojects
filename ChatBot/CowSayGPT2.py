from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
import cowsay
import math
import sympy as sym
class ChatBot:
    def __init__(self):
        self.model_type = 'gpt2-xl'
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = GPT2LMHeadModel.from_pretrained(self.model_type)
        self.model.config.pad_token_id = self.model.config.eos_token_id  # suppress a warning

    #This is the generative portion of the chatbot using the GPT2 model
    def generate(self, prompt='', num_samples=10, steps=40, do_sample=True):
        tokenizer = GPT2Tokenizer.from_pretrained(self.model_type)
        encoded_input = tokenizer(prompt, return_tensors='pt').to(self.device)
        x = encoded_input['input_ids'].expand(num_samples, -1) if prompt else None

        # Forward the model `steps` times to get samples, in a batch
        y = self.model.generate(x, max_length=steps, do_sample=do_sample, top_k=40)

        for i in range(num_samples):
            out = tokenizer.decode(y[i].cpu().squeeze())
        return print(cowsay.get_output_string("cow", out))
    
    #Gets the weather for a specified place (Be it a specific address or a city)
    def get_weather(self, user_location):
        import requests
        
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
    #Performs mathematical operations     
    def basic_calculator(self, user_input):
        if "**" in user_input:
            x, z = user_input.split("**")
            x = float(x)
            z = float(z)
            return print(cowsay.get_output_string("cow", f"{x} raised to {z} = {x ** z}"))

        elif "sqrt" in user_input or "square root" in user_input:
            if "sqrt" in user_input:
                x = float(user_input.split("sqrt")[1])
            else:
                x = float(user_input.split("square root")[1])

            return print(cowsay.get_output_string("cow", f"Square root of {x} = {math.sqrt(x)}"))

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


    # Inside the ChatBot class
    # ... (other methods unchanged)
    
    def calculus_calculator(self, method, function):
        x = sym.symbols('x')
        
        if method.lower() == "derivative":
            derivative = sym.diff(function, x)
            return print(cowsay.get_output_string("cow", f"The derivative of {function} with respect to x is {derivative}"))

        elif method.lower() == "integration":
            check_for_limits = input("Would you like to add limits? (y/n): ").lower()
            if check_for_limits == 'y':
                upper_limit = float(input("What is the upper limit?: "))
                lower_limit = float(input("What is the lower limit?: "))
                definite_integral = sym.integrate(function, (x, lower_limit, upper_limit))
                return print(cowsay.get_output_string("cow", f"The integral of {function} over the interval {lower_limit} to {upper_limit} is {definite_integral}"))
            
            elif check_for_limits == 'n':
                indefinite_integral = sym.integrate(function, x)
                return print(cowsay.get_output_string("cow", f"The indefinite integral of {function} is {indefinite_integral}"))

            else:
                return print(cowsay.get_output_string("cow", "Invalid choice for limits. Please enter 'y' or 'n'."))

        elif method.lower() == "limit":
            approaching = float(input("What is x approaching?: "))
            limit = sym.limit(function, x, approaching)
            return print(cowsay.get_output_string("cow", f"The limit of {function} as x approaches {approaching} is {limit}"))

        else:
            return print(cowsay.get_output_string("cow", "Invalid method choice. Please choose 'Derivative', 'Integration', or 'Limit'."))


def main():
    chatbot = ChatBot()
    while True:
        user_input = input("What would you like to say to the chatbot?: ").lower()
        if user_input.lower() in ['exit', 'quit']:
            print(cowsay.get_output_string("cow", "Goodbye!"))
            break
        elif user_input == "Get me the weather" or user_input == "weather" or user_input == "What's the weather?":
            user_location = input("Where would you like the weather?: ")
            chatbot.get_weather(user_location)
        elif "+" in user_input or "-" in user_input or "*" in user_input or "/" in user_input or "**" in user_input or ("sqrt" or "square root") in user_input:
            chatbot.basic_calculator(user_input)
        elif user_input == "calculus":
            function = input("What is the function?: ")
            method = input("What would you like to do to the function? (Derivative, Integration, Limit):")
            chatbot.calculus_calulator(method, function)
        
        else:
            chatbot.generate(user_input)


if __name__ == "__main__":
    main()
