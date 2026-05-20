import nltk
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

nltk.download("stopwords")
nltk.download("punkt_tab")

food_paragraph = """
Plants as a food source are divided into legumes, grains and nut.
Fruit Fruit and seed Fruit are important food items seed.
"""

cinema_paragraph = """
Hindi cinema included Sholay films Sholay Deewaar like Zanjeer, Deewaar and Sholay.
"""

food_keywords = ["fruit", "seed", "grain", "nut"]

cinema_keywords = ["zanjeer", "deewaar", "sholay"]

food_text = food_paragraph.lower()

# Tokenization
food_tokens = word_tokenize(food_text)

# Stopwords remove
stop_words = set(stopwords.words("english"))
food_filtered = []
for word in food_tokens:
    if word.isalpha() and word not in stop_words:
        food_filtered.append(word)

# Frequency Count
food_counter = Counter(food_filtered)

print(" FOOD ")
found_food = []
for word in food_keywords:
    count = food_counter[word]
    if count > 0:
        found_food.append((word, count))

print(found_food)
cinema_text = cinema_paragraph.lower()
cinema_tokens = word_tokenize(cinema_text)
cinema_filtered = []
for word in cinema_tokens:
    if word.isalpha() and word not in stop_words:
        cinema_filtered.append(word)
cinema_counter = Counter(cinema_filtered)

print(" Cinema ")
found_cinema = []
for word in cinema_keywords:
    count = cinema_counter[word]
    if count > 0:
        found_cinema.append((word, count))
print(found_cinema)

food_words = [word for word, count in found_food]
food_counts = [count for word, count in found_food]

cinema_words = [word for word, count in found_cinema]
cinema_counts = [count for word, count in found_cinema]

plt.bar(food_words, food_counts, alpha=0.7, label="Food")
plt.bar(cinema_words, cinema_counts, alpha=0.7, label="Cinema")
plt.xlabel("Keywords")
plt.ylabel("Counts")
plt.title("NLTK Food vs Cinema Analysis")
plt.legend()
plt.show()
