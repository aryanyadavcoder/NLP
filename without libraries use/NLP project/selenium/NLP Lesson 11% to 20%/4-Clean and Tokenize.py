import string

def clean_text(text):
    text = text.lower()

    result = ""

    for ch in text:
        if ch not in string.punctuation:
            result = result + ch

    result = " ".join(result.split())

    return result

message = "Champak Roy teaches Python, AI, ML, and NLP!"

cleaned = clean_text(message)
tokens = cleaned.split()

print("Cleaned text:", cleaned)
print("Tokens:", tokens)