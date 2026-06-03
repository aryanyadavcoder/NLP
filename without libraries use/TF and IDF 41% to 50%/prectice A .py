from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
sentence = [
    "python is a basics language",
    "Python is used for machine learning.",
    "The AI model is trained on a large dataset.",
    "A search engine helps users find information.",
    "Machine learning is a part of artificial intelligence.",
    "The NLP system is used to analyze text."
]
vectorizer = TfidfVectorizer(stop_words="english")
vectorizer.fit(sentence)
remaining_words = set(vectorizer.get_feature_names_out())

all_words = set()
for s in sentence:
    all_words.update(s.lower().replace(".", "").split())
removed_words = all_words - remaining_words

print("Remaining Words:", remaining_words)
print("Removed Stop Words:", removed_words)



