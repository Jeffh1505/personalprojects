import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/section/todayspaper?redirect_uri=https%3A%2F%2Fwww.nytimes.com%2F'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    headline_elements = soup.find_all('h3', {'data-testid': 'css-miszbp e1hr934v2'})
    
    if headline_elements:
        for headline_element in headline_elements:
            headline = headline_element.get_text()
            print(headline)
    else:
        print('Headlines not found on the page.')
else:
    print('Failed to fetch the webpage.')
