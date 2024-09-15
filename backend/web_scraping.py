from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re

# TODO: Implement dynamic query
query = 'onix bom'
sites = search(query, num_results=1)

def scrape_site(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

def clean_text(text):
    text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuations
    return text.lower()

for site in sites:
    text = scrape_site(site)
    text = clean_text(text)
    print(text)

