# Exercise 4
# Write a function that gets a list of integers as a parameter. The function returns the sum of all the numbers in the list. For testing, write a main program where you create a list, call the function, and print out the value it returned.

def sum_numbers(numbers):
    total = 0
    for i in numbers:
        total += i
    return  total

numbers_list = []

while True:
    user_input = input("Enter a number to add in the list or leave empty to stop: ")
    if user_input == "":
        print(f"The list is : {numbers_list}")
        break
    value = int(user_input)
    numbers_list.append(value)

final_value = sum_numbers(numbers_list)

print(f"The sum of all the numbers in the list equals to: {final_value}")