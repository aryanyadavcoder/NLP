lessons = [
    "Python variables and arithmetic operators",
    "Beginning NLP with text similarity",
    "Machine learning with simple datasets",
    "Google Search Console for Blogger",
    "Sorting trace and algorithm detection"
]

search = "text similarity NLP"
search_words = search.lower().split()

scores = []

for lesson in lessons:
    lesson_words = lesson.lower().split()
    score = 0

    for word in search_words:
        if word in lesson_words:
            score = score + 1

    scores.append([score, lesson])

scores.sort(reverse=True)

print("Best matching lessons:")
for score, lesson in scores:
    print(score, "-", lesson)