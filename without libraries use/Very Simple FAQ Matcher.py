faqs = {
    "fees": "Please visit learnwithchampak.live for course fee details.",
    "timing": "Classes are usually held according to the announced schedule.",
    "python": "Yes, Python is used in our AI-ML classes.",
    "certificate": "Certificate details will be shared by the teacher."
}

question = "Do you teach python in this course?"
question = question.lower()

answer_found = False

for keyword in faqs:
    if keyword in question:
        print(faqs[keyword])
        answer_found = True
        break

if answer_found == False:
    print("Please contact Champak Roy for details.")
    
  