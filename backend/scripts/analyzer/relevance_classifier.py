"""
This module is responsible for classifying the relevance of the reviews.
It uses the Facebook BART model to classify the reviews as relevant or not relevant.
The module also uses the sentiment analysis to classify the reviews as positive, negative or neutral.
"""

import re
from transformers import pipeline
from .sentiment_analyzer import sentiment_analysis

relevance_classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli",
    clean_up_tokenization_spaces=True
)

IRRELEVANT_PHRASES = [
    "encontre um veículo", "últimos artigos", 
    "sobre este artigo", "vale a pena ler também", "comente", 
    "veja também", "artigo", "veja mais", "leia também", "compre com desconto",
    "assinar", "limite", "matérias", "assinante",
    "assinatura", "conteúdo exclusivo", "restrito",
    "financiamento", "financie", "financiamento",
    "vendedor", "clique", "assine", "cnpj", "cpf",
    "reservados", "conteudo", "acesso", "cadastro",
    "login", "?"
]
CANDIDATE_LABELS = ['relevant', 'not relevant']

def clean_text(text):
    """Clean the text to remove irrelevant phrases and special characters."""
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^\w\s]', '', text).lower()

    if len(text.split()) < 5:
        return ""

    return text.strip()

def process_texts(texts):
    """Process the texts to remove irrelevant phrases."""
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
    """Classify the relevance of the reviews."""
    relevance_scores = {'scraped_sites': [], 'positives': [], 'negatives': [], 'neutral': []}

    for data in scrap_result:
        for text in data['cleaned_reviews']:
            relevance_result = relevance_classifier(text['cleaned_text'], candidate_labels=CANDIDATE_LABELS)

            is_relevant_score = relevance_result['scores'][0]

            if is_relevant_score > 0.985:
                relevant_label = relevance_result['labels'][0]

                if relevant_label == 'not relevant':
                    continue

                if relevant_label == 'relevant':
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
