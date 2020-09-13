import logging
import os
import re
import ssl

import nltk
import requests
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
        getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

nltk.download('wordnet')
nltk.download('stopwords')
lemmatizer = WordNetLemmatizer()

logger = logging.getLogger(__name__)
stop_words = stopwords.words('english')

def download_text(url: str) -> str:
    try:
        return requests.get(url).content.decode()
    except Exception as e:
        logger.exception(e)
        raise

def extract_words(text: str) -> list:
    return [lemmatizer.lemmatize(w) for w in re.findall(r'\w+', text.lower()) if w not in stop_words]

def extract_word_frequencies(words: list) -> dict:
    frequencies = dict()
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return dict(sorted(frequencies.items(), key=lambda item: item[1], reverse=True))


