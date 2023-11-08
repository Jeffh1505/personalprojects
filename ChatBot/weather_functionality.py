def get_weather():
    import requests
    user_location = input("Please input your address or a city: ")
    cities = {"New York": "20 W 34th St., New York, NY 10001", "Los Angeles": "1111 S Figueroa St, Los Angeles, CA 90015"
              , "Chicago": "233 S Wacker Dr, Chicago, IL 60606", "San Francisco": "600 Montgomery St, San Francisco, CA 94111",
              "Houston": "2800 Post Oak Blvd, Houston, TX 77056", "Miami":" 1 Washington Ave, Miami Beach, FL 33139", 
              "Philadelphia": "520 Chestnut St, Philadelphia, PA 19106", "Seattle": "400 Broad St, Seattle, WA 98109", 
              "Boston": ""}
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
        return f"Today's forecast: {forecast}"
    else:
        return "Forecast not found"