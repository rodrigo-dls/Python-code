# Exercise 5
print("\n------ Exercise 5: ------\n")

# Write a program that asks the user for a username and password. If either or both are incorrect, the program ask the user to enter the username and password again. This continues until the login information is correct or wrong credentials have been entered five times. If the information is correct, the program prints out Welcome. After five failed attempts the program prints out Access denied. The correct username is python and password rules.

attempts = 0
username = "python"
password = "rules"

while attempts < 5:
    username_input = input("Enter the username: ")
    password_input = input("Enter the password: ")
    if username == username_input and password == password_input:
        print("Welcome")
        break

    attempts += 1
    if attempts == 5:
        print("Access denied.")
    else:
        print("Try again.")
