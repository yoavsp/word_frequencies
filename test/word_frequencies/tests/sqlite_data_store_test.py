import unittest
from word_frequencies.data.concrete.sqlite_data_store import SQLiteDataStore
import os

class SQLiteDataStoreTests(unittest.TestCase):

    def setUp(self) -> None:
        os.remove("/tmp/test.db")
        super().setUp()

    def test_upsert(self):
        ds = SQLiteDataStore("/tmp/test.db")
        ds.save([{"Word": 'a', 'Count': 3}, {"Word": 'b', 'Count': 4}])
        ds.save([{"Word": 'a', 'Count': 6}, {"Word": 'b', 'Count': 7}])
        count = ds.getWordCount("a")
        self.assertEqual(count, 6)