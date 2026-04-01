# Exercise 2
print("\n------- Exercise 2: ------\n")

# Write a program that asks the user to enter the cabin class of a cruise ship and then prints out a written description according to the list below. You must use an if/elif/else structure in your solution.
#
#     LUX: upper-deck cabin with a balcony.
#     A: above the car deck, equipped with a window.
#     B: windowless cabin above the car deck.
#     C: windowless cabin below the car deck.
#
# If the user enters an invalid cabin class, the program outputs an error message Invalid cabin class.

# Get data
cabin_class = input("What's your cabin class?: ")

# Process data
if cabin_class == "LUX":
    print("LUX: upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("A: above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("B: windowless cabin above the car deck.")
elif cabin_class == "C":
    print("C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")