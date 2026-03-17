# Exercise 2

# Write a program that asks the user to enter numbers until they input an empty string to quit. At the end, the program prints out the five greatest numbers sorted in descending order. Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.

raw_list = []

while True:
    user_input = input("Enter a number (or quit with 'Enter'): ")
    if user_input == "":
        break
    if int(user_input) not in raw_list:
        raw_list.append(int(user_input))

raw_list.sort(reverse=True)
print(raw_list[:5])