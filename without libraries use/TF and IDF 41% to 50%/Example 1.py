from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

lesson_titles = [
    "Python basics for beginners",
    "HTML and CSS introduction",
    "Machine Learning with Python",
    "Angular deployment on GitHub Pages",
    "NLP text similarity using cosine similarity",
    "TF IDF search ranking in natural language processing",
    "Sorting algorithms in Python",
    "NumPy arrays for AI and ML"
]

query = input("Search for a lesson: ")

all_texts = [query] + lesson_titles

vectorizer = TfidfVectorizer(stop_words="english")
vectors = vectorizer.fit_transform(all_texts)

scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

best_index = scores.argmax()
best_lesson = lesson_titles[best_index]
best_score = scores[best_index]

print("\nYour search:")
print(query)

print("\nBest matching lesson:")
print(best_lesson)

print("\nSimilarity score:")
print(round(best_score, 3))

print("\nRanked results:")

ranked = sorted(
    zip(lesson_titles, scores),
    key=lambda item: item[1],
    reverse=True
)

for title, score in ranked:
    print(round(score, 3), "->", title)