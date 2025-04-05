max_height = 50

def tall_enough_to_ride():
    height = float(input("How tall are you?"))

    if height >= max_height:
        print("You are tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")


tall_enough_to_ride()