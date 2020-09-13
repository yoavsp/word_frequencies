from word_frequencies.csv_data_store import CSVDataStore
from word_frequencies.sqlite_data_store import SQLiteDataStore
from word_frequencies.word_count import main


main("http://www.gutenberg.org/files/11/11-0.txt", [CSVDataStore("/tmp/alice.csv"), SQLiteDataStore("/tmp/alice.db")])