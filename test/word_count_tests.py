import unittest
from unittest.mock import Mock

import nltk
from nltk.corpus import stopwords

from word_frequencies.word_frequency_services import extract_words, extract_word_frequencies
from word_frequencies.app import main


class WordFrequencyServiceTests(unittest.TestCase):

    def test_stop_words_are_filtered(self):
        words = extract_words(", ".join(stopwords.words('english')))
        self.assertTrue(len(words) == 0)

    def test_extract_word_frequencies(self):
        word_input = ['it', 'was', 'the', 'best', 'of', 'times', 'it', 'was',
                   'the', 'worst', 'of', 'times', 'it', 'was', 'the', 'age',
                   'of', 'wisdom', 'it', 'was', 'the', 'age', 'of',
                   'foolishness']

        word_output = extract_word_frequencies(word_input)

        self.assertEqual(sorted(word_output.items(), key= lambda x: x[0]),  [('age', 2), ('best', 1), ('foolishness', 1), ('it', 4), ('of', 4), ('the', 4), ('times', 2), ('was', 4), ('wisdom', 1), ('worst', 1)])

    def test_main_calls_data_store(self):
        mock_store: Mock = Mock()
        main("http://www.gutenberg.org/files/11/11-0.txt", data_store_providers = [mock_store])
        mock_store.save.assert_called()