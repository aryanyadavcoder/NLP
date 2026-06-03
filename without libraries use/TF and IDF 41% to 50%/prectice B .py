from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

lessons = [
    {
        "title":"python basics",
        "description":"learne variables,loop,input,output,arithmatic oprators"
    },
    {
        "title":"Numpy for ai ml",
        "description":"learne array,matrix oprations,numrical computing"
    },
    {
        "title":"Machine learning with python",
        "description":"Supervised learning,Unsupervised learning,prediction and model evaluation"     
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
    },
    {
        "title":"Computer Vision in Autonomous Systems",
        "description": "A field enabling machines to interpret, process, and extract actionable information from visual inputs."
    },
    {
        "title":"Generative AI & Multimodal Models",
        "description":"AI systems that create new content—such as text, audio, images, or video—from simple text prompts. Modern multimodal models can process "
    },
    {
        "title":"MLOps and Production AI",
        "description":"The engineering discipline focused on bridging the gap between training a machine learning model and deploying it into live production"
    }
    
]


search_text = []

for lesson in lessons:
    combind_text = lesson["title"] + " "+ lesson["description"]
    search_text.append(combind_text)
    
query = input("What do you want to learn? ")

all_texts = [query] + search_text

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