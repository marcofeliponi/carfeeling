import aiohttp
import asyncio
from bs4 import BeautifulSoup
from .analyzer.relevance_classifier import process_texts, classify_relevance
from googlesearch import search
from services.services import get_cars_service, save_car_analysis
from time import sleep
import random

FAVORITES_SITES_TO_SCRAPE = [
        'https://quatrorodas.abril.com.br',
        'https://www.icarros.com.br',
        'https://flatout.com.br',
        'https://www.carrosnaweb.com.br',
        'https://autoentusiastas.com.br'
        'https://motor1.uol.com.br',
    ]

USER_AGENT_LIST = [    
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
    ] 

HEADERS = {
    'User-Agent': random.choice(USER_AGENT_LIST),
    'Accept-Language': 'pt-BR',
    'Connection': 'keep-alive',
}

async def scrape_site(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=HEADERS) as response:
            encoding = response.charset or 'utf-8'
            text = await response.read()
            text = text.decode(encoding, errors='replace')
            soup = BeautifulSoup(text, 'html.parser')

            reviews = soup.find_all(['p', 'div'], class_=lambda x: x and 'review' in x.lower())
            if not reviews:
                reviews = soup.find_all('p')
            
            return [review.get_text() for review in reviews]

async def run_scrape_process(query, num_results):
    sites = search(query, num_results=num_results, lang='pt-br', sleep_interval=5.0, safe='on')

    data = []
    for site in sites:
        sleep(10)
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
    relevant_reviews = {'scraped_sites': [], 'positives': [], 'negatives': [], 'neutral': []}

    for site in FAVORITES_SITES_TO_SCRAPE:
        query = f'{car} avaliação site:{site}'
        cleaned_reviews = await run_scrape_process(query, 1)
        
        if (len(cleaned_reviews) > 0):
            classified_data = classify_relevance(cleaned_reviews)

            relevant_reviews['scraped_sites'].extend(classified_data['scraped_sites'])
            relevant_reviews['positives'].extend(classified_data['positives'])
            relevant_reviews['negatives'].extend(classified_data['negatives'])
            relevant_reviews['neutral'].extend(classified_data['neutral'])

    not_enough_reviews_from_main_sites = (len(relevant_reviews['positives']) + len(relevant_reviews['negatives'])) < 5
    if (not_enough_reviews_from_main_sites):
        query = f'{car} vale a pena -site:{" -site:".join(FAVORITES_SITES_TO_SCRAPE)}'
        cleaned_reviews = await run_scrape_process(query, 5)

        if (len(cleaned_reviews) > 0):
            classified_data = classify_relevance(cleaned_reviews)

            relevant_reviews['scraped_sites'].extend(classified_data['scraped_sites'])
            relevant_reviews['positives'].extend(classified_data['positives'])
            relevant_reviews['negatives'].extend(classified_data['negatives'])
            relevant_reviews['neutral'].extend(classified_data['neutral'])
    
    if (len(relevant_reviews['positives']) > 0 or len(relevant_reviews['negatives']) > 0):
        score = calculate_score(relevant_reviews)
        # save_car_analysis(car, relevant_reviews, score)
        return {'car': car, 'score': score, **relevant_reviews}
    
async def run(car=None, year=None):
    response_to_api_calls = []

    if car:
        arguments = f'{car} {year}' if year else car
        response_to_api_calls = await process_car_reviews(arguments)
        return response_to_api_calls

    models = get_cars_service()['cars']
    for model in models:
        car = model['model']
        data = await process_car_reviews(car)
        response_to_api_calls.append(data)

    return response_to_api_calls

if __name__ == "__main__":
    asyncio.run(run())
