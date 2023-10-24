import requests
from bs4 import BeautifulSoup

NYT_homepage = requests.get('https://www.nytimes.com/')
