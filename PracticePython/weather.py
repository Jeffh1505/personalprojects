import requests
url = 'https://api.weather.gov/points/40.8075,-73.9625'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
print(data)