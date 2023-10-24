import requests
from bs4 import BeautifulSoup

NYT_homepage = requests.get('https://www.nytimes.com/')
NYT_homepage_html = NYT_homepage.text
soup = BeautifulSoup(NYT_homepage_html, "html.parser")
title = soup.find('span', 'articletitle').string
print(title)