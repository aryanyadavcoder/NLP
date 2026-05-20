# ==============================
# NLP COMPLETE PRACTICE
# ==============================

# Libraries
import re
import nltk
import matplotlib.pyplot as plt

from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

from wordcloud import WordCloud

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# =====================================
# TEXT
# =====================================

text = """
Python is amazing for AI and Machine Learning.
Machine Learning is part of Artificial Intelligence.
Python is widely used in Data Science and NLP.
"""

# =====================================
# 1. LOWERCASING
# =====================================

lower_text = text.lower()

print("\n===== LOWERCASE =====")
print(lower_text)

# =====================================
# 2. TOKENIZATION
# =====================================

tokens = word_tokenize(lower_text)

print("\n===== TOKENS =====")
print(tokens)

# =====================================
# 3. REMOVE STOPWORDS
# =====================================

stop_words = set(stopwords.words('english'))

filtered_words = []

for word in tokens:
    if word.isalpha() and word not in stop_words:
        filtered_words.append(word)

print("\n===== STOPWORDS REMOVED =====")
print(filtered_words)

# =====================================
# 4. STEMMING
# =====================================

stemmer = PorterStemmer()

stemmed_words = []

for word in filtered_words:
    stemmed_words.append(stemmer.stem(word))

print("\n===== STEMMING =====")
print(stemmed_words)

# =====================================
# 5. LEMMATIZATION
# =====================================

lemmatizer = WordNetLemmatizer()

lemmatized_words = []

for word in filtered_words:
    lemmatized_words.append(lemmatizer.lemmatize(word))

print("\n===== LEMMATIZATION =====")
print(lemmatized_words)

# =====================================
# 6. REGEX CLEANING
# =====================================

clean_text = re.sub(r'[^a-zA-Z ]', '', lower_text)

print("\n===== REGEX CLEANING =====")
print(clean_text)

# =====================================
# 7. KEYWORD COUNTER
# =====================================

keywords = ["python", "machine", "learning", "ai", "nlp"]

print("\n===== KEYWORD COUNTER =====")

for word in keywords:
    count = lower_text.count(word)
    print(word, "=", count)

# =====================================
# 8. WORD FREQUENCY
# =====================================

word_counts = Counter(filtered_words)

print("\n===== WORD FREQUENCY =====")
print(word_counts)

# =====================================
# 9. BAR GRAPH
# =====================================

plt.figure(figsize=(8,5))

plt.bar(word_counts.keys(), word_counts.values())

plt.title("Word Frequency")
plt.xlabel("Words")
plt.ylabel("Count")

plt.show()

# =====================================
# 10. PIE CHART
# =====================================

plt.figure(figsize=(7,7))

plt.pie(
    word_counts.values(),
    labels=word_counts.keys(),
    autopct='%1.1f%%'
)

plt.title("Word Distribution")

plt.show()

# =====================================
# 11. WORD CLOUD
# =====================================

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white'
).generate(clean_text)

plt.figure(figsize=(10,5))

plt.imshow(wordcloud)

plt.axis("off")

plt.title("Word Cloud")

plt.show()

# =====================================
# 12. FREQUENCY DISTRIBUTION
# =====================================

freq_dist = nltk.FreqDist(filtered_words)

plt.figure(figsize=(8,5))

freq_dist.plot(10)

plt.show()