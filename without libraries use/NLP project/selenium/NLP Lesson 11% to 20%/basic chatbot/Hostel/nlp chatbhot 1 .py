import pandas as pd

print("===== Welcome to Aryan Hotel =====")

# CSV Files Read
room_words_df = pd.read_csv("words.csv")
rooms = pd.read_csv("rooms.csv")
food_df = pd.read_csv("food.csv")

# NLP Keywords
room_words = room_words_df["Words"].tolist()

food_words = ["food", "menu", "eat", "dinner", "lunch", "breakfast"]

Hii = ["hii","hi","hello"]

contact_words = ["contact", "number", "phone", "mobile"]

location_words = ["location", "address", "place"]

hotel_number = "9876543210"
hotel_location = "Varanasi, Uttar Pradesh"


# ---------- FUNCTIONS ---------- #
def show_Hi():
    print("\n Hi sir how can help you today")
    

def room_booking():

    print("\n===== Rooms Available =====")

    for i in range(len(rooms)):
        print(i + 1, ".", rooms.iloc[i]["Room Name"], "-", rooms.iloc[i]["Price"])

    name = input("\nEnter your name: ")
    number = input("Enter phone number: ")

    days = int(input("How many days: "))

    choice = int(input("Choose room number: "))

    # Validation
    if choice < 1 or choice > len(rooms):
        print("Invalid Room Number")
        return

    room_name = rooms.iloc[choice - 1]["Room Name"]
    room_price = rooms.iloc[choice - 1]["Price"]

    room_total = room_price * days

    food_total = 0

    food_choice = input("\nDo you want food? (yes/no): ").lower()

    if "yes" in food_choice:

        print("\n===== Food Menu =====")

        for i in range(len(food_df)):
            print(
                i + 1, ".", food_df.iloc[i]["food_name"], "-", food_df.iloc[i]["price"]
            )

        food_number = int(input("\nChoose food number: "))
        quantity = int(input("Enter quantity: "))

        if food_number < 1 or food_number > len(food_df):
            print("Invalid Food Choice")
            return

        food_name = food_df.iloc[food_number - 1]["food_name"]
        food_price = food_df.iloc[food_number - 1]["price"]

        food_total = food_price * quantity

        print("\nFood Ordered:", food_name)

    gst = (room_total + food_total) * 0.18

    grand_total = room_total + food_total + gst

    print("\n===== Booking Successful =====")

    print("Customer Name:", name)
    print("Phone Number:", number)
    print("Room Type:", room_name)
    print("Days:", days)

    print("Room Bill:", room_total)
    print("Food Bill:", food_total)

    print("GST (18%):", gst)

    print("Grand Total:", grand_total)


def show_food():

    print("\n===== Food Menu =====")

    for i in range(len(food_df)):
        print(i + 1, ".", food_df.iloc[i]["food_name"], "-", food_df.iloc[i]["price"])


def show_contact():

    print("\nHotel Contact Number:", hotel_number)


def show_location():

    print("\nHotel Location:", hotel_location)


# ---------- MAIN LOOP ---------- #

while True:

    question = input("\nAsk your question: ").lower()

    # NLP Preprocessing
    words = question.split()
    if any(word in question for word in Hii):
        show_Hi()



    # Exit
    if "exit" in words:
        print("Thank you for visiting Aryan Hotel")
        break

    # Room Intent Detection
    elif any(word in words for word in room_words):

        room_booking()

    # Food Intent Detection
    elif any(word in words for word in food_words):

        show_food()

    # Contact Intent Detection
    elif any(word in words for word in contact_words):

        show_contact()

    # Location Intent Detection
    elif any(word in words for word in location_words):

        show_location()

    else:
        print("Sorry, I did not understand.")
