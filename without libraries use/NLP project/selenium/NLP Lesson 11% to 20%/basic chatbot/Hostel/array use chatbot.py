import pandas as pd

print("Welcome to Aryan Hotel")
room_words_df = pd.read_csv("words.csv")
rooms = pd.read_csv("rooms.csv")
room_words = room_words_df["Words"].tolist()

while True:
    question = input("\nAsk your question: ").lower()
    if question == "exit":
        print("Thank you for visiting Aryan Hotel")
        break
    question_words = question.split()
    found = False
    for word in room_words:
        if word in question_words:
            found = True
            print("\nRooms Available")
            for i in range(len(rooms)):
                print(i + 1,".",rooms.iloc[i]["Room Name"],"-",rooms.iloc[i]["Price"])
            name = input("Enter your name: ")
            days = int(input("How many days: "))
            choice = int(input("Choose room number: "))
            room_name = rooms.iloc[choice - 1]["Room Name"]
            price = rooms.iloc[choice - 1]["Price"]
            total = price * days

            print("\nRoom Booked Successfully")
            print("Customer Name:", name)
            print("Room Type:", room_name)
            print("Days:", days)
            print("Total Bill:", total)

            break

    if found == False:
        print("Sorry, I did not understand.")