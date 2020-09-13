from os import path
from typing import List

from word_frequencies.data.concrete.csv_data_store import CSVDataStore
from word_frequencies.data.concrete.sqlite_data_store import SQLiteDataStore
from word_frequencies.data.contract.word_frequency_store import WordFrequencyStore
from word_frequencies.word_frequency_services import extract_word_frequencies, extract_words, download_text
import logging

# TODO: logger config doesn't apply - need to fix
from logging.config import fileConfig

log_setting_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
fileConfig(log_setting_file_path)

logger = logging.getLogger(__name__)

def main(url: str, data_store_providers: List[WordFrequencyStore] = [], top_k: int = 100):
    frequencies = extract_word_frequencies(extract_words(download_text(url)))
    for ds in data_store_providers:
        try:
            ds.save([{"Word": k, "Count": v} for k, v in frequencies.items()][:top_k])
        except Exception as e:
            logger.exception(e)

main("http://www.gutenberg.org/files/11/11-0.txt", [CSVDataStore("/tmp/alice.csv"), SQLiteDataStore("/tmp/alice.db")])