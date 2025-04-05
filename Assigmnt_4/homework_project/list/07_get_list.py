my_list = []

def get_list():
    while True:
        value = input("Enter a value (press Enter to stop): ")

        if value == "":
            break

        my_list.append(value)

    print("Final list: ", my_list)

get_list()