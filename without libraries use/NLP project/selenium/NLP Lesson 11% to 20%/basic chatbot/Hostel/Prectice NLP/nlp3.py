import string
text = "Do you teach , ai,ml and nlp? without python!"
clean_text = ""
for charecter in text:
    if charecter not in string.punctuation:
        clean_text = clean_text + charecter
print(clean_text)        