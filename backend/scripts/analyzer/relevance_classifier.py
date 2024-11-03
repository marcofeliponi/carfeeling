from transformers import pipeline
import re
from .sentiment_analyzer import sentiment_analysis

relevance_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", clean_up_tokenization_spaces=True)

IRRELEVANT_PHRASES = [
    "encontre um veículo", "últimos artigos", 
    "sobre este artigo", "vale a pena ler também", "comente", 
    "compre agora", "veja também", "artigo relacionado",
    "veja mais", "leia também", "compre com desconto",
    "assinar", "limite", "matérias restritas", "assinante",
    "assinatura", "conteúdo exclusivo", "conteúdo restrito",
    "financiamento", "financie", "financiamento de veículo",
    "vendedor", 
]
CANDIDATE_LABELS = ['relevant', 'not relevant', 'irrelevant', 'subscription-only', 'not applicable']

def clean_text(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^\w\s]', '', text).lower()
    
    if len(text.split()) < 5:
        return ""
    
    return text.strip()

def process_texts(texts):
    processed_texts = []
    for text in texts:
        if any(keyword in text.lower() for keyword in IRRELEVANT_PHRASES):
            continue

        original_text = text
        cleaned_text = clean_text(text)
        if cleaned_text:
            processed_texts.append({ 'cleaned_text': cleaned_text, 'original_text': original_text })

    return processed_texts

def classify_relevance(scrap_result):
    relevance_scores = {'scraped_sites': [], 'positives': [], 'negatives': [], 'neutral': []}
    
    for data in scrap_result:
        for text in data['cleaned_reviews']:
            relevance_result = relevance_classifier(text['cleaned_text'], CANDIDATE_LABELS)

            if relevance_result['scores'][0] > 0.8:
                label = relevance_result['labels'][0]

                if label in ['not relevant', 'irrelevant', 'subscription-only', 'not applicable']:
                    continue
                
                if label == 'relevant':
                    if data['site'] not in relevance_scores['scraped_sites']:
                        relevance_scores['scraped_sites'].append(data['site'])
                
                    sentiment_result = sentiment_analysis(text['cleaned_text'])

                    sentiment_label = sentiment_result[0]['label']

                    if sentiment_label in ['4 stars', '5 stars']:
                        relevance_scores['positives'].append(text['original_text'])
                    elif sentiment_label in ['1 star', '2 stars']:
                        relevance_scores['negatives'].append(text['original_text'])
                    else:
                        relevance_scores['neutral'].append(text['original_text'])
    
    relevance_scores['positives'] = relevance_scores['positives'][:10]
    relevance_scores['negatives'] = relevance_scores['negatives'][:10]
    relevance_scores['neutral'] = relevance_scores['neutral'][:10]
    
    return relevance_scores
