import string
text = "Do you teach Python AI , ML and NLP?"
clean_text = ""
for char in text:
    if char not in string.punctuation:
        clean_text = clean_text + char
print(clean_text)        