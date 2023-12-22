import requests
import tkinter as tk
def get_lat_long(address):
    user_address = address
    address_url = f'https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address={user_address}&benchmark=2020&format=json'
    response1 = requests.get(address_url)
    if response1.status_code == 200:
        data1 = response1.json()

    else:
        print("Invalid Location.")
    latitude = str(data1['result']['addressMatches'][0]['coordinates']['y'])[:-10]
    longitude = str(data1['result']['addressMatches'][0]['coordinates']['x'])[:-10]
    return latitude, longitude

def get_weather(latitude, longitude):
    url1 = f'https://api.weather.gov/points/{latitude},{longitude}'
    response2 = requests.get(url1)
    if response2.status_code == 200:
        data = response2.json()
        forecast_link = data['properties']['forecast']
    else: 
        print("Invalid location")

    response3 = requests.get(forecast_link)
    if response3.status_code == 200:
        data2 = response3.json()
        forecast = data2['properties']['periods'][0]['detailedForecast']
        return forecast
    else:
        print("Forecast not found")

def weather_app():
    window = tk.Tk()
    window.title("My Window")
    window.geometry("300x300")

    label = tk.Label(window, text="Hello, world!")
    label.pack()

    entry = tk.Entry(window)
    entry.pack()
    user_address = entry.get()
    latitude, longitude = get_lat_long(user_address)
    weather = get_weather(latitude, longitude)
    output_text = tk.Text(window, height=4, width=40)
    output_text.pack()
    output_text.delete(1.0, tk.END)  # Clear previous output
    output_text.insert(tk.END, "The forecast is" + weather)
   

    window.mainloop()
    