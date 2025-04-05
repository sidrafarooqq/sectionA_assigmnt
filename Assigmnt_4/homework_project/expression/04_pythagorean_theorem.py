import math


def pythagrean_theory():
    ab = float(input("enter the length of ab : "))
    ac = float(input("enter the length of ac:"))

    bc = math.sqrt(ab ** 2 + ac ** 2)

    print("The length of BC (the hypotenuse) is: " + str(bc))

pythagrean_theory()   