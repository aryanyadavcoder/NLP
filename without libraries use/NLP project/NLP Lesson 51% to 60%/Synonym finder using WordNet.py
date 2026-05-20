from nltk.corpus import wordnet as wn

def get_synonyms(word):
    synonyms = set()

    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            name = lemma.name().replace("_", " ")
            if name.lower() != word.lower():
                synonyms.add(name)

    return sorted(synonyms)

word = input("Enter a word: ")

print("\nSynonyms:")
for item in get_synonyms(word):
    print("-", item)