import string

def clean_text(text):
    text = text.lower()

    result = ""

    for ch in text:
        if ch not in string.punctuation:
            result = result + ch

    result = " ".join(result.split())

    return result

message = "Hello!!! I want to Learn AI & ML..."

print(clean_text(message))