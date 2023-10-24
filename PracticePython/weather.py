import requests
url = 'https://api.weather.gov/points/{40.8075},{-73.9625}'
response = requests.get(url)
print(response)