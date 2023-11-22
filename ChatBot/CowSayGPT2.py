from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
import cowsay
class ChatBot:
    def __init__(self):
        self.model_type = 'gpt2-xl'
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = GPT2LMHeadModel.from_pretrained(self.model_type)
        self.model.config.pad_token_id = self.model.config.eos_token_id  # suppress a warning

    def generate(self, prompt='', num_samples=10, steps=20, do_sample=True):
        tokenizer = GPT2Tokenizer.from_pretrained(self.model_type)
        encoded_input = tokenizer(prompt, return_tensors='pt').to(self.device)
        x = encoded_input['input_ids'].expand(num_samples, -1) if prompt else None

        # Forward the model `steps` times to get samples, in a batch
        y = self.model.generate(x, max_length=None, do_sample=do_sample, top_k=40)

        for i in range(num_samples):
            out = tokenizer.decode(y[i].cpu().squeeze())
        return print(cowsay.get_output_string("cow", out))
    def get_weather(self, user_location):
        import requests
        
        cities = {"New York": "20 W 34th St., New York, NY 10001", "Los Angeles": "1111 S Figueroa St, Los Angeles, CA 90015"
                , "Chicago": "233 S Wacker Dr, Chicago, IL 60606", "San Francisco": "600 Montgomery St, San Francisco, CA 94111",
                "Houston": "2800 Post Oak Blvd, Houston, TX 77056", "Miami":" 1 Washington Ave, Miami Beach, FL 33139", 
                "Philadelphia": "520 Chestnut St, Philadelphia, PA 19106", "Seattle": "400 Broad St, Seattle, WA 98109", 
                "Boston": "206 Washington St, Boston, MA 02109", "Washington DC": "1600 Pennsylvania Avenue NW, Washington, DC 20500"}
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
        
    def math(self, user_input):
        x, y, z= user_input.split(" ")
        x = float(x)
        z = float(z)
        if y == "+":
            print(x + z)
        elif y == "-":
            print(x - z)
        elif y == "*":
            print(x*z)
        elif y == "/":
            print(x/z)


def main():
    chatbot = ChatBot()
    while True:
        user_input = input("What would you like to say to the chatbot?: ")
        if user_input.lower() in ['exit', 'quit']:
            print(cowsay.get_output_string("cow", "Goodbye!"))
            break
        elif user_input == "Get me the weather" or user_input == "weather" or user_input == "What's the weather?":
            user_location = input("Where would you like the weather?: ")
            chatbot.get_weather(user_location)
        else:
            chatbot.generate(user_input)


if __name__ == "__main__":
    main()
