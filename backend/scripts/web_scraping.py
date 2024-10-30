import aiohttp
import asyncio
from bs4 import BeautifulSoup
from .analyzer.relevance_classifier import process_texts, classify_relevance
from googlesearch import search
from services.services import get_cars_service, save_car_analysis

favorites_sites_to_scrape = [
        'https://quatrorodas.abril.com.br',
        'https://www.icarros.com.br',
        'https://flatout.com.br',
        'https://www.carrosnaweb.com.br',
        'https://autoentusiastas.com.br'
        'https://motor1.uol.com.br',
    ]

async def scrape_site(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            encoding = response.charset or 'utf-8'
            text = await response.read()
            text = text.decode(encoding, errors='replace')
            soup = BeautifulSoup(text, 'html.parser')

            reviews = soup.find_all(['p', 'div'], class_=lambda x: x and 'review' in x.lower())
            if not reviews:
                reviews = soup.find_all('p')
            
            return [review.get_text() for review in reviews]

async def run_scrape_process(query, num_results):
    sites = search(query, num_results=num_results)

    data = []
    for site in sites:
        reviews = await scrape_site(site)

        if (len(reviews) == 0):
            print(f'No reviews found for {query} on {site}')
            continue

        cleaned_reviews = process_texts(reviews)
        data.append({'cleaned_reviews': cleaned_reviews, 'site': site})
        
    return data

def calculate_score(data):
    positive_weight = 1
    negative_weight = -1
    
    num_positives = len(data['positives'])
    num_negatives = len(data['negatives'])
    
    score = (num_positives * positive_weight) + (num_negatives * negative_weight)

    min_score, max_score = -10, 10
    normalized_score = 1 + ((score - min_score) / (max_score - min_score)) * 4
    normalized_score = round(max(1, min(normalized_score, 5)), 2)

    return normalized_score

async def process_car_reviews(car):
    print(f'Scraping {car}')
    cleaned_reviews = []
    relevant_reviews = {'scraped_sites': [], 'positives': [], 'negatives': []}
    extra_relevant_reviews = {'scraped_sites': [], 'positives': [], 'negatives': []}
    
    for site in favorites_sites_to_scrape:
        query = f'{car} avaliação site:{site}'
        cleaned_reviews = await run_scrape_process(query, 1)
        
    relevant_reviews = classify_relevance(cleaned_reviews)

    not_enough_reviews_from_main_sites = (len(relevant_reviews['positives']) + len(relevant_reviews['negatives'])) < 5
    if (not_enough_reviews_from_main_sites):
        query = f'{car} avaliação -site:{" -site:".join(favorites_sites_to_scrape)}'
        cleaned_reviews = await run_scrape_process(query, 3)

        extra_relevant_reviews = classify_relevance(cleaned_reviews)
        relevant_reviews['scraped_sites'].extend(extra_relevant_reviews['scraped_sites'])
        relevant_reviews['positives'].extend(extra_relevant_reviews['positives'])
        relevant_reviews['negatives'].extend(extra_relevant_reviews['negatives'])
    
    if (len(relevant_reviews['positives']) > 0 or len(relevant_reviews['negatives']) > 0):
        score = calculate_score(relevant_reviews)
        save_car_analysis(car, relevant_reviews, score)
    
async def run():
    models = get_cars_service()['cars']

    for model in models:
        car = model['model']
        await process_car_reviews(car)

asyncio.run(run())
