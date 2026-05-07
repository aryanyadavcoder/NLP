sentence = "Champak Roy is teaching AI in the online class"
common_words = ["is","an","the","in","to","of"]
words = sentence.lower().split()
importent_words = []
for word in words:
    if word not in common_words:
        importent_words.append(word)
print("All words :",word)
print("Important word :",importent_words)