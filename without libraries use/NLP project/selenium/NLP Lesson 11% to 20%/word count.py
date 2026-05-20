text = "python python nlp"

words = text.split()

count = {}

for w in words:
    count[w] = count.get(w, 0) + 1

print(count)