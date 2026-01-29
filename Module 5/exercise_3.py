# Write a program that asks the user for an integer and tells if the number is a prime number. Prime numbers are number that are only divisible by one or the number itself.
#
# For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
# On the other hand, 21 is not a prime number as it is divisible by 3 and 7.

user_input = int(input("Enter a number: "))

for i in range(2,user_input):
    test = user_input % i
    print(test)
    if user_input == 1 or user_input == 2:
        print("It is a prime number.")
    elif test == 0:
        print("It is a prime number.")
        break
else:
    print("It is not a prime number.")

