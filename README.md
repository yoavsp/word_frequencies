 This app gets the top k frequent words in given story(in this case the story is 
 [Alice’s Adventures in Wonderland](http://www.gutenberg.org/files/11/11-0.txt)   

The app collects The top k frequent words and saves them into a csv file and a SQLite DB:
In each line the first element is the word (string) and the second is the count.  for example (for k=3):

| Word  | Count       | 
|-------|-------------|
| word1 | word1_count |
| word2 | word2_count |
| word3 | word3_count | 

 In order to run this project, please install dependencies using (pip install -r requirements.txt).
 Then run: python -m word_frequencies.app
 