import requests
user_address = input("Please input your address: ")
address_url = f'https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address={user_address}&benchmark=2020&format=json'
response1 = requests.get(address_url)
if response1.status_code == 200:
    data1 = response1.json()

else:
    print("Invalid Location.")
latitude = str(data1['result']['addressMatches'][0]['coordinates']['y'])[:-10]
longitude = str(data1['result']['addressMatches'][0]['coordinates']['x'])[:-10]
print(latitude, longitude)
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
    print("Today's forecast: ", forecast)
else:
    print("Forecast not found")