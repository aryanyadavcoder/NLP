feedback = "The ai class was easy and the Python examples were easy to understand"
words = feedback.lower().split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] = word_count[word]+1
    else:
        word_count[word] = 1
print(word_count)            
