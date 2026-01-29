# Exercise 5
# Write a function that gets a list of integers as a parameter. The function returns a second list that is otherwise the same as the original list except that all uneven numbers have been removed. For testing, write a main program where you create a list, call the function, and then print out both the original as well as the cut-down list.

numbers_list = []

def remove_uneven(inner_list):
    new_list = []
    for i in inner_list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

while True:
    user_input = input("Enter a number to add in the list or leave empty to stop: ")
    if user_input == "":
        break
    value = int(user_input)
    numbers_list.append(value)

clean_list = remove_uneven(numbers_list)

print(f"Original list: {numbers_list}")
print(f"List without uneven numbers: {clean_list}")
