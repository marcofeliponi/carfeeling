from transformers import pipeline
import re

irrelevant_phrases_to_remove = [
    "encontre um veículo", "últimos artigos", 
    "sobre este artigo", "vale a pena ler também", "comente", 
    "compre agora", "veja também", "artigo relacionado",
    "veja mais", "leia também", "compre com desconto",
]

positive_keywords = ['econômico', 'confortável', 'forte', 'bonito', 'excelente', 'silencioso', 'elegante', 'tecnologia']
negative_keywords = ['caro', 'raspa', 'alto', 'baixo', 'defeito', 'ruim', 'barulhento', 'feio', 'fraco', 'lento']

candidate_labels = ['relevant', 'not relevant']

def clean_text(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^\w\s]', '', text).lower()
    
    for phrase in irrelevant_phrases_to_remove:
        text = re.sub(rf'\b{re.escape(phrase)}\b', '', text)
    
    if len(text.split()) < 5:
        return ""
    
    return text.strip()

def process_texts(texts):
    processed_texts = []
    for text in texts:
        cleaned_text = clean_text(text)
        if cleaned_text:
            processed_texts.append(cleaned_text)
    return processed_texts

relevance_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_relevance(scrap_result):
    relevance_scores = {'scraped_sites': [], 'positives': [], 'negatives': []}
    
    for data in scrap_result:
        for text in data['cleaned_reviews']:
            result = relevance_classifier(text, candidate_labels)
            if result['labels'][0] == 'relevant' and result['scores'][0] > 0.8:
                if data['site'] not in relevance_scores['scraped_sites']:
                    relevance_scores['scraped_sites'].append(data['site'])
                if any(kw in text for kw in positive_keywords):
                    relevance_scores['positives'].append(text)
                elif any(kw in text for kw in negative_keywords):
                    relevance_scores['negatives'].append(text)
    
    relevance_scores['positives'] = relevance_scores['positives'][:10]
    relevance_scores['negatives'] = relevance_scores['negatives'][:10]
    
    return relevance_scores
