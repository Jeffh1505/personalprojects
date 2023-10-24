import requests
url1 = 'https://api.weather.gov/points/40.8075,-73.9625'
response = requests.get(url1)
if response.status_code == 200:
    data = response.json()
    forecast_link = data['properties']['forecast']

response2 = requests.get(forecast_link)
if response2.status_code == 200:
    data2 = response2.json()
    forecast = data2['']
print(data2)