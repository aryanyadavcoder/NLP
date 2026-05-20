import string
text = "Do you teach AI, ML and NLP?"
clean_text = ""
for character in text :
    if character not in string.punctuation:
        clean_text = clean_text + character
print(clean_text)        
        