print("Welcome to Aryan Hotel")

while True:
    question = input("\nAsk your question: ").lower()

    if "room price" in question:
        print("Room Price")
        print("1. Budget Room - 1500 per night")
        print("2. 3-Star Room - 3000 per night")
        print("3. 5-Star Room - 5000 per night")

    elif "book" in question or "room booking" in question:

        name = input("Enter your name: ")
        days = int(input("How many days: "))

        print("Choose Room Type")
        print("1. Budget Room")
        print("2. 3-Star Room")
        print("3. 5-Star Room")

        room = input("Enter room type number: ")

        if room == "1":
            price = 1500
            room_name = "Budget Room"

        elif room == "2":
            price = 3000
            room_name = "3-Star Room"

        elif room == "3":
            price = 5000
            room_name = "5-Star Room"

        else:
            print("Invalid room choice")
            continue

        total = price * days

        print("\nRoom booked successfully")
        print("Customer Name:", name)
        print("Room Type:", room_name)
        print("Days:", days)
        print("Total Bill:", total)

    elif "room" in question or "booking" in question:
        print("Yes, rooms are available today.")

    elif "food" in question or "menu" in question:
        print("Food Menu")
        print("1. Pizza - 250")
        print("2. Tea - 40")
        print("3. Coffee - 60")
        

    elif "location" in question or "address" in question:
        print("Aryan Hotel, Pandeypur, Varanasi")

    elif "number" in question or "contact" in question:
        print("Contact us at: 9250435696")

    elif "time" in question or "timing" in question:
        print("Check-in time is 12 PM")
        print("Check-out time is 11 AM")

    elif "exit" in question:
        print("Thank you for visiting Aryan Hotel")
        break

    else:
        print("Sorry, please contact: 01125532553")