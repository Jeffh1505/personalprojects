import requests
import tkinter as tk

def get_lat_long(address):
    address_url = f'https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address={address}&benchmark=2020&format=json'
    response1 = requests.get(address_url)
    
    if response1.status_code == 200:
        data1 = response1.json()
        latitude = str(data1['result']['addressMatches'][0]['coordinates']['y'])[:-10]
        longitude = str(data1['result']['addressMatches'][0]['coordinates']['x'])[:-10]
        return latitude, longitude
    else:
        print("Invalid Location.")
        return None, None

def get_weather(latitude, longitude):
    url1 = f'https://api.weather.gov/points/{latitude},{longitude}'
    response2 = requests.get(url1)
    
    if response2.status_code == 200:
        data = response2.json()
        forecast_link = data['properties']['forecast']
        
        response3 = requests.get(forecast_link)
        if response3.status_code == 200:
            data2 = response3.json()
            forecast = data2['properties']['periods'][0]['detailedForecast']
            return forecast
        else:
            print("Forecast not found")
            return None
    else:
        print("Invalid location")
        return None

def weather_app():
    window = tk.Tk()
    window.title("Weather App")
    window.geometry("300x300")

    label = tk.Label(window, text="Enter address:")
    label.pack()

    entry = tk.Entry(window)
    entry.pack()

    def show_weather():
        user_address = entry.get()
        latitude, longitude = get_lat_long(user_address)
        
        if latitude is not None and longitude is not None:
            weather = get_weather(latitude, longitude)
            
            if weather is not None:
                output_text.delete(1.0, tk.END)  # Clear previous output
                output_text.insert(tk.END, "The forecast is:\n" + weather)
            else:
                output_text.delete(1.0, tk.END)
                output_text.insert(tk.END, "Forecast not found.")
        
    button = tk.Button(window, text="Get Weather", command=show_weather)
    button.pack()

    output_text = tk.Text(window, height=6, width=40)
    output_text.pack()

    window.mainloop()

weather_app()
