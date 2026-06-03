import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("without libraries use/NLP project/selenium/NLP Lesson 11% to 20%/basic chatbot/Hostel/data_science_deep_notes.csv")
print(df)

question =df["Question"].tolist()
user_question = input("Any Question: ")
                                                                                                                     