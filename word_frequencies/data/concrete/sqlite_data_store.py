import logging
import sqlite3
from sqlite3 import Error
from word_frequencies.data.contract.word_frequency_store import WordFrequencyStore

logger = logging.getLogger(__name__)

CREATE_TABLE_SQL = """
    CREATE TABLE IF NOT EXISTS word_frequencies (
	word text PRIMARY KEY NOT NULL,
	count integer);"""

class SQLiteDataStore(WordFrequencyStore):

    def __init__(self, db_file: str) -> None:
        self.db_file = db_file
        try:
            connection = sqlite3.connect(self.db_file)
            connection.execute(CREATE_TABLE_SQL)
        except Error as e:
            logger.exception(e)


    def save(self, frequencies: list) -> None:
        try:
            connection = sqlite3.connect(self.db_file)
            sql = '''INSERT INTO word_frequencies VALUES(:word,:count) ON CONFLICT(word) DO UPDATE SET count=:count'''
            cursor = connection.cursor()

            cursor.executemany(sql, tuple([(frequency["Word"], int(frequency["Count"]), ) for frequency in frequencies]))
            connection.commit()
        except Error as e:
            logger.exception(e)

    def getWordCount(self, word) -> int:
        try:
            connection = sqlite3.connect(self.db_file)
            sql = '''SELECT * FROM word_frequencies where word=?'''
            cursor = connection.cursor()

            cursor.execute(sql, (word,))
            res = cursor.fetchone()
            assert not res or len(res) == 2
            return res[1] if res else None
        except Error as e:
            logger.exception(e)


