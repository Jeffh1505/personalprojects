import requests
latitude = input("Please input a latitude: ")
longitude = input("Please input a longitude: ")
url1 = f'https://api.weather.gov/points/{latitude},{longitude}'
response = requests.get(url1)
if response.status_code == 200:
    data = response.json()
    forecast_link = data['properties']['forecast']
else: 
    print("Invalid location")

response2 = requests.get(forecast_link)
if response2.status_code == 200:
    data2 = response2.json()
    forecast = data2['properties']['periods'][0]['detailedForecast']
print("Today's forecast: ", forecast)