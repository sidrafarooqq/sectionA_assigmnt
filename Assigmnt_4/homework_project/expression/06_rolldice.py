import random
def rollerdice():
    die1 = random.randint(1 , 6)
    die2 = random.randint(1 , 6)
    total = die1 + die2

    print(f"first die is, {die1} ")
    print(f"second die is, {die2}")
    print(total)

rollerdice()   