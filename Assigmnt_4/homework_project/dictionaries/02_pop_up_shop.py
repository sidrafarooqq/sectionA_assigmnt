def pop_up_shop():
    fruits ={"Apple": 2,     
    "Banana": 1,     
    "Orange": 1.5,   
    "Mango": 3,      
    "Grapes": 2.5 }

    print("Welcome to the fruits shop")
    print(f"Here is rate chart: \n {fruits}")

    cost = 0

    for fruit in fruits:
        while True:
            quantity = input(f"How much {fruit} do you want to buy? (Enter 0 if none)")
            if quantity.isdigit():
                quantity = int(quantity)
                price = fruits[fruit]
                cost += (price * quantity)
                break
            else:
                print("❌ Please enter a valid digit!")
        
    print(f"Here is your total bill: {cost}")
