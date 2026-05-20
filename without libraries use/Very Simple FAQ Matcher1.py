faqs = {
    "admission":"Admissions are open from June to August ",
    "fees":"the annual fees is around 50,000.",
    "course":"we offer BCA,B.tech and Diploma courses",
    "hostel": "Hostel facility is available for both boys and girls."
}

question = input("Ask your question :")
question = question.lower()
answer_found = False
for keyword in faqs:
    if keyword in question:
        print(faqs[keyword])
        answer_found = True
        break
if answer_found == False:
    print("Please contact Champak Roy for detail.")    