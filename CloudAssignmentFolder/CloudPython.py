import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('stopwords')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))
file = open('paragraphs.txt', 'r')
text_data = file.read()
words = word_tokenize(text_data)
filtered_words = [word for word in words if word.lower() not in stop_words]
word_count = Counter(filtered_words).most_common()

for word, freq in word_count:
    print(f'"{word}": {freq}.')
