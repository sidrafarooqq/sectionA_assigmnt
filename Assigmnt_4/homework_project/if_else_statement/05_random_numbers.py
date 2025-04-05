import random

range_of_numbers = 10
min_value = 1
max_value = 100

def random_numbers():
    for i in range(range_of_numbers):
        value = random.randint(min_value, max_value)
        print(value, end=" ")

random_numbers()