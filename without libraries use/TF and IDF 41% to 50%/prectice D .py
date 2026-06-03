from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
lessons = [
    "Python Basics for Beginners",
    "Python for AI and Machine Learning",
    "Web Design with HTML and CSS",
    "JavaScript Fundamentals",
    "Data Science with Python",
    "Introduction to Artificial Intelligence"
]
queries = [
    "Python AI beginner",
    "web design CSS"
]
vectorizer = TfidfVectorizer()
lesson_vectors = vectorizer.fit_transform(lessons)
for query in queries:
    print("\n" + "=" * 50)
    print("Query:", query)
    print("=" * 50)

    query_vector = vectorizer.transform([query])

    similarity = cosine_similarity(query_vector, lesson_vectors)

    scores = similarity[0]
    ranked_results = sorted(
        zip(lessons, scores),
        key=lambda x: x[1],
        reverse=True
    )

    print("\nRanked Results:\n")

    for rank, (lesson, score) in enumerate(ranked_results, start=1):
        print(f"{rank}. {lesson}")
        print(f"   Similarity Score: {score:.4f}")

    print("\nBest Match:")
    print(ranked_results[0][0])