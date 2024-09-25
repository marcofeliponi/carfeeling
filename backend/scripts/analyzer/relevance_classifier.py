from transformers import pipeline
import re

candidate_labels = ['relevant', 'not relevant']

def clean_text(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower()

def process_texts(texts):
    processed_texts = []
    for text in texts:
        cleaned_text = clean_text(text)
        processed_texts.append(cleaned_text)
    return processed_texts

relevance_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_relevance(texts):
    relevant_texts = []
    for text in texts:
        result = relevance_classifier(text, candidate_labels)

        if result['labels'][0] == 'relevant' and result['scores'][0] > 0.8:
            relevant_texts.append(text)
    return relevant_texts