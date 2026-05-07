from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sentences = [
    "Programmers Picnic AI ML",
    "AI ML class by Champak Roy"
]

vectorizer = CountVectorizer()

vectors = vectorizer.fit_transform(sentences)

similarity = cosine_similarity(vectors)

print(similarity)