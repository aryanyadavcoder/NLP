from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

lessons = [
    {
        "title": "Python Basics",
        "description": "Learn variables, input, output, arithmetic operators and beginner programming."
    },
    {
        "title": "NumPy for AI and ML",
        "description": "Learn arrays, matrix operations, numerical computing and AI data handling."
    },
    {
        "title": "Machine Learning with Python",
        "description": "Learn supervised learning, training data, prediction and model evaluation."
    },
    {
        "title": "NLP Text Similarity",
        "description": "Learn CountVectorizer, cosine similarity and sentence comparison."
    },
    {
        "title": "TF-IDF Search Ranking",
        "description": "Learn stop words, term frequency, inverse document frequency and better text search."
    },
    {
        "title": "HTML and CSS Web Design",
        "description": "Learn how to create beautiful web pages using HTML and CSS."
    },
    {
        "title": "Angular GitHub Pages Deployment",
        "description": "Learn how to build and deploy Angular apps on GitHub Pages."
    }
]

search_texts = []

for lesson in lessons:
    combined_text = lesson["title"] + " " + lesson["description"]
    search_texts.append(combined_text)

query = input("What do you want to learn? ")

all_texts = [query] + search_texts

vectorizer = TfidfVectorizer(stop_words="english")
vectors = vectorizer.fit_transform(all_texts)

scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

ranked_results = sorted(
    zip(lessons, scores),
    key=lambda item: item[1],
    reverse=True
)

print("\nSearch query:")
print(query)

print("\nBest lessons:")

for lesson, score in ranked_results:
    if score > 0:
        print("\nTitle:", lesson["title"])
        print("Description:", lesson["description"])
        print("Score:", round(score, 3))    