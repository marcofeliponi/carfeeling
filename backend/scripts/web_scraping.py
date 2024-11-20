import aiohttp
import asyncio
from bs4 import BeautifulSoup
from .analyzer.relevance_classifier import process_texts, classify_relevance
from googlesearch import search
from services.services import get_cars_service, save_car_analysis, get_cars_without_reviews
from time import sleep
import random
import time


FAVORITES_SITES_TO_SCRAPE = [
    'https://www.icarros.com.br',
    'https://www.carrosnaweb.com.br',
    'https://flatout.com.br',
    'https://autoentusiastas.com.br'
    'https://motor1.uol.com.br',
    'https://quatrorodas.abril.com.br',
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

async def run_scrape_process(query, num_results, car_keyword):
    sites = search(query, num_results=num_results, lang='pt-br', sleep_interval=60.0, safe='on')

    data = []
    for site in sites:
        if car_keyword.lower() not in site.lower():
            continue

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

async def process_car_reviews(car, year=None):
    print(f'Scraping car = {car} || year = {year}')
    cleaned_reviews = []
    relevant_reviews = {'scraped_sites': [], 'positives': [], 'negatives': [], 'neutral': []}
    car_keyword = car.split()[0]

    for site in FAVORITES_SITES_TO_SCRAPE:
        query = f"{car} {year if year else ''} avaliação site:{site}"
        cleaned_reviews = await run_scrape_process(query, 1, car_keyword)
        
        if (len(cleaned_reviews) > 0):
            classified_data = classify_relevance(cleaned_reviews)

            relevant_reviews['scraped_sites'].extend(classified_data['scraped_sites'])
            relevant_reviews['positives'].extend(classified_data['positives'])
            relevant_reviews['negatives'].extend(classified_data['negatives'])
            relevant_reviews['neutral'].extend(classified_data['neutral'])

    not_enough_reviews_from_main_sites = (len(relevant_reviews['positives']) + len(relevant_reviews['negatives'])) < 5
    if (not_enough_reviews_from_main_sites):
        query = f"{car} {year if year else ''} vale a pena -site:{' -site:'.join(FAVORITES_SITES_TO_SCRAPE)}"
        cleaned_reviews = await run_scrape_process(query, 5, car_keyword)

        if (len(cleaned_reviews) > 0):
            classified_data = classify_relevance(cleaned_reviews)

            relevant_reviews['scraped_sites'].extend(classified_data['scraped_sites'])
            relevant_reviews['positives'].extend(classified_data['positives'])
            relevant_reviews['negatives'].extend(classified_data['negatives'])
            relevant_reviews['neutral'].extend(classified_data['neutral'])
    
    if (len(relevant_reviews['positives']) > 0 or len(relevant_reviews['negatives']) > 0):
        score = calculate_score(relevant_reviews)
        save_car_analysis(car, relevant_reviews, score, year)
        print(f'Dado salvo -> {car}')
        return {'car': car, 'score': score, 'year': year if year else 'not informed', **relevant_reviews}
    
async def run(car=None, year=None):
    response_to_api_calls = []

    if car:
        response_to_api_calls = await process_car_reviews(car, year)
        return response_to_api_calls

    models = get_cars_service()['cars']
    for model in models:
        car = model['model']
        year = model['year']

        start = time.perf_counter()

        data = await process_car_reviews(car, year)

        end = time.perf_counter()
        print(f'TEMPO -> {round(end-start, 2)} second(s)')

        response_to_api_calls.append(data)

    return response_to_api_calls

if __name__ == "__main__":
    asyncio.run(run())
