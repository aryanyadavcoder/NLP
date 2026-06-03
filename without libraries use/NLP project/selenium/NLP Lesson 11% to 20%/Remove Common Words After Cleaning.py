import string
common_word = ["is","am","are","the","a","an","and","to"]
def clean_text(text):
    text = text.lower()
    result = ""
    for ch in text:
        if ch not in string.punctuation:
            result = result+ch
    result = " ".join(result.split())
    return result
Sentence = "Champak Roy is teaching AI and ML in the class."
cleaned = clean_text(Sentence)
word = cleaned.split()
important_word = []
