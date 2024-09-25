from analyzer.relevance_classifier import process_texts, classify_relevance
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import json

# TODO: Implement dynamic query (car options has to come from DB, or a JSON file)
query = 'onix bom site reviews'
sites = search(query, num_results=1)

def scrape_site(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    reviews = soup.find_all(['p', 'div'], class_=lambda x: x and 'review' in x.lower())
    if not reviews:
        reviews = soup.find_all('p')
    
    return [review.get_text() for review in reviews]

for site in sites:
    reviews = scrape_site(site)
    cleaned_reviews = process_texts(reviews)
    
    relevant_reviews = classify_relevance(cleaned_reviews)

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(relevant_reviews, f, ensure_ascii=False, indent=4)

