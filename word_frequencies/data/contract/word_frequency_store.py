from abc import ABC, abstractmethod


class WordFrequencyStore(ABC):
    @abstractmethod
    def save(self, frequencies: list) -> None:
        pass

    @abstractmethod
    def getWordCount(self, word) -> int:
        pass