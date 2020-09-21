import csv
from word_frequencies.data.contract.word_frequency_store import WordFrequencyStore


class CSVDataStore(WordFrequencyStore):

    def getWordCount(self, word) -> int:
        with open(self.path, 'w') as file:
            reader = csv.DictReader(file)
            res = [r['Count'] for r in reader if r['Word'] == word]
            return res[0] if len(res) > 0 else None

    def __init__(self, path) -> None:
        self.path = path

    def save(self, frequencies: dict) -> None:
        with open(self.path, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=["Word", "Count"])
            writer.writeheader()
            writer.writerows(frequencies)
