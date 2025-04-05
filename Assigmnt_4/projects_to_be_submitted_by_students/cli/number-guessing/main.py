import random

print ("Welcome to Number Guessing Game!\n You got 5 attempts to guess the number between 50 and 100, \n Lets start the Game")

number_to_guess = random.randrange(50, 100)
chances:int = 5
guesss_counter= 0

while guesss_counter < chances:
    guesss_counter+=1
    #guesss_counter= guesss_counter + 1
    my_guess=int(input("Enter your guess: "))

    if my_guess == number_to_guess:
        print(f"The number is {number_to_guess} and you found it right in the {guesss_counter} attempt!!")
        break
    elif guesss_counter >= chances and my_guess != number_to_guess:
        print(f"Oops sorry, the number is {number_to_guess} Better Luck Next Time")
    elif my_guess < number_to_guess:
        print("Your Guess is very Low, Try Again!")

    elif my_guess > number_to_guess:
        print("Your Guess is very High, Try Again!")