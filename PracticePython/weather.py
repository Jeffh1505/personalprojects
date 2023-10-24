import requests
url1 = 'https://api.weather.gov/points/40.8075,-73.9625'
response = requests.get(url1)
if response.status_code == 200:
    data = response.json()
    forecast_link = data['forecast']
print(forecast_link)