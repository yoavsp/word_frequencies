from abc import ABC, abstractmethod
import logging
import re
from itertools import groupby
from typing import List

import requests
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

# had a problem with nltk at first so copied the list
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
logger = logging.getLogger(__name__)

def download_text(url:str) -> str:
    try:
        return requests.get(url).content.decode()
    except Exception as e:
        logger.exception(e)
        raise

def extract_words(text: str) -> list:
    return [lemmatizer.lemmatize(w) for w in re.findall(r'\w+', text) if w not in stop_words]

def extract_word_frequencies(words:list) -> dict:
    frequencies = dict()
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return dict(sorted(frequencies.items(), key= lambda item: item[1], reverse=True))


class WordFrequencyStore(ABC):
    @abstractmethod
    def save(self, frequencies: list) -> None:
        pass

def main(url: str, data_store_providers: List[WordFrequencyStore] = [], top_k: int = 100):

    frequencies = extract_word_frequencies(extract_words(download_text(url)))
    for ds in data_store_providers:
        try:
            ds.save([{"Word": k, "Count":v} for k,v in frequencies.items()][:top_k])
        except Exception as e:
            logger.exception(e)
