from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


documentes = [
    "python is used for machine learning",
    "machine learning uses for algorithms",
    "python is used for ai ml"
]

query = [input("what do you want to learne: ").lower()]

count_vectorizer = CountVectorizer()

doc_matrix = count_vectorizer.fit_transform(documentes)
query_vector = count_vectorizer.transform(query)

similarity = cosine_similarity(query_vector, doc_matrix)

print("CountVectorizer Similarity:")
print(similarity)

# Method 2-- TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer()

doc_matrix = tfidf_vectorizer.fit_transform(documentes)
query_vector = tfidf_vectorizer.transform(query)

similarity = cosine_similarity(query_vector, doc_matrix)

print("TF-IDF Similarity:")
print(similarity)