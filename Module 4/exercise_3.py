# Exercise 3
print("\n------- Exercise 3: ------\n")

# Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program prints out the smallest and largest number from the numbers it received.

user_input = input("Enter a number: ")
if user_input != "":
    min_val = float(user_input)
    max_val = float(user_input)

    while user_input != "":
        value =  float(user_input)

        if min_val > value:
            min_val = value
        if max_val < value:
            max_val = value

        user_input = input("Enter a number: ")
    else:
        print(f"min_val: {min_val}")
        print(f"max_val: {max_val}")

print("Good bye!")