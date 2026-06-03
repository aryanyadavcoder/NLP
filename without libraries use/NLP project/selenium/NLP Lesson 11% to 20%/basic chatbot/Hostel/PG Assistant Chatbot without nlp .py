print(" Welcome To Aryan Hotel ")
while True:
    print("\n1. Room Booking")
    print("2. Food Order")
    print("3. Check Room Price")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter your name: ")
        print(" Room menu ")
        print("1. Budget-1500 per night ,2. 3-Star Room --3000 per night ,3. 5-Star Room -- 5000 per night ")
        n = input("Enter your choice: ")
        days = int(input("How many days you want to stay: "))
        if n == "1":
            print("Total Price: ",days*1500)
        elif n == "2":
            print("Total Price: ", days*3000)
        else :
            print("Total Price: ", days*5000)
        print("Room booked successfully")
        print("Customer Name:", name)  
        continue
    
    elif choice == "2":
        print(" Food Menu ")
        print("1. piza -- 200 ")
        print("2. Burger -- 50 ")
        print("3. Momo -- 60 ")
        print("4. Fruit -- 100 ") 
        l = input("Enter your choice: ")
        qut = int(input("Enter quantity: "))
        if l == "1":
            print("Total Food Price: ",qut*200)
        elif l == "2":
            print( "Total Food Price: ",qut*50)
        elif l == "3":
            print( "Total Food Price: ",qut*60)
        else :
            print( "Total Food Price: ",qut*100)
            
    elif choice == "3":
        print(" Room Price") 
        print("1. Budget-1500 per night")
        print("2. 3-Star Room --3000 per night ")
        print("3. 5-Star Room -- 5000 per night ")  
    else :
        exit()     
                        