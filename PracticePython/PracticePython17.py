import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    title_element = soup.find('h1', {'data-testid': 'headline'})
    
    if title_element:
        title = title_element.get_text()
        print(title)
    else:
        print('Title not found on the page.')
else:
    print('Failed to fetch the webpage.')
