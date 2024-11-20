"""
This module contains the sentiment analysis function.
It uses the Hugging Face transformers library to analyze the sentiment of the text.
"""

from transformers import pipeline

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

def sentiment_analysis(text):
    """Analyze the sentiment of the text."""
    results = sentiment_pipeline(text)
    return results
