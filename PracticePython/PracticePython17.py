import requests
from bs4 import BeautifulSoup

NYT_homepage = requests.get('https://www.nytimes.com/')
NYT_homepage_html = NYT_homepage.text