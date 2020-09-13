import csv

from word_frequencies.word_count import WordFrequencyStore


class CSVDataStore(WordFrequencyStore):

    def __init__(self, path) -> None:
        self.path = path

    def save(self, frequencies: dict) -> None:
        with open(self.path, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=["Word", "Count"])
            writer.writeheader()
            writer.writerows(frequencies)

