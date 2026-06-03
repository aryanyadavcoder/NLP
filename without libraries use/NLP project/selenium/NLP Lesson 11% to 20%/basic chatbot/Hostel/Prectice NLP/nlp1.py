sentence = "Comedy Works is a stand-up comedy club with two locations in the Denver, Colorado metropolitan area. The downtown club opened in September 1981 and is located in Larimer Square in Denver. The south club, which opened September 2008, is part of The Landmark development in Greenwood Village."
coomon_words = ["is","am","are","the","and","a","not","this","that","those","i","to","if","for","with","two","which","in"]
words = sentence.lower().split()
important_words = []
word_count = {}
for word in words:
    if word not in coomon_words:
        important_words.append(word)
        if word in word_count:
            word_count[word] = word_count[word]+1
        else:
            word_count[word] = 1    
print("Important word: ",important_words)  
print("\nWord Count:")
print(word_count)
      