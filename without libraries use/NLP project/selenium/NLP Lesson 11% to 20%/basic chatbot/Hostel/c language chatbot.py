import pandas as pd

df = pd.read_csv("c_language_deep_notes.csv")
print(" C Language Chatbot ")
while True:

    question = input("\nAsk Question: ").lower()

    if question == "exit":
        print("Chatbot Closed")
        break

    words = question.split()
    found = False
    for i in range(len(df)):

        topic = str(df.loc[i, "Topic"]).lower()
        explanation = str(df.loc[i, "Explanation"])
        code = str(df.loc[i, "Example Code"])
        for word in words:
            if word in topic:
                print("\nTopic:", df.loc[i, "Topic"])
                print("\nExplanation:")
                print(explanation)
                print("\nExample Code:")
                print(code)

                found = True
                break
        if found:
            break

    if not found:
        print("No answer found")
