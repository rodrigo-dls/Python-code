from random import randrange

# Exercise 1
print("\n------- Exercise 1: ------\n")

# Write a program that asks your name and then greets you by your name: Examples:
#
# If you enter Viivi as your name, the program will greet you with Hello, Viivi!.
# If you enter Ahmed as your name, the program will greet you with Hello, Ahmed!.

name = input("What's your name: ")

print(f"Hello, {name}!")

# Exercise 2
print("\n------- Exercise 2: ------\n")

# Write a program that asks the user for the radius of a circle and the prints out the area of the circle.

pi = 3.14
circle_radius = float(input("What's the radius of the circle: "))

circle_area = pi * circle_radius * circle_radius

print(f"The area of the circle is {circle_area:4.6}")

# Exercise 3
print("\n------- Exercise 3: ------\n")

# Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter and area of the rectangle. The perimeter of a rectangle is the sum of the lengths of each four sides.

length = float(input("What's the length of the rectangle: "))
width = float(input("And the width: "))

rect_perimeter = 2 * (length + width)
rect_area = length * width

print(f"That rectangle perimeter is {rect_perimeter:4.6} and its area is {rect_area:4.6}")

# Exercise 4
print("\n------- Exercise 4: ------\n")

# Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers.

num_1 = int(input("What's the first integer number: "))
num_2 = int(input("What's the second integer number: "))
num_3 = int(input("And the third integer number: "))

sum = num_1 + num_2 + num_3
product = num_1 * num_2 * num_3
average = float(sum / 3)

print(f"The sum is: {sum}")
print(f"The product is: {product}")
print(f"The average is: {average:4.6}")


# Exercise 5
print("\n------- Exercise 5: ------\n")

# Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti).
# The program converts the input to full kilograms and grams and outputs the result to the user:

talents =   float(input("Enter talents: \n"))
pounds =    float(input("\nEnter pounds: \n"))
lots =      float(input("\nEnter lots: \n"))

lot_gr =    13.3
pound_gr =  32 * lot_gr
talent_gr = 20 * pound_gr

# total weight in grams
weight_gr = talents * talent_gr + pounds * pound_gr + lots * lot_gr

# kilograms of the total weight
kg = int(weight_gr // 1000)

# grams of the total weight
gr = weight_gr % 1000

print("\nThe weight in modern units: ")
print(f'{kg} kilograms and {gr:4.6} grams.')

# Exercise 6
print("\n------- Exercise 6: ------\n")

# Write a program that draws two random combinations of numbers for a combination lock:
# a 3-digit code where each number is between 0 and 9.
# a 4-digit code where each number is between 1 and 6.

dig1_3d = str(randrange(0,10))  # digit 1 of 3-digit code
dig2_3d = str(randrange(0,10))  # digit 2 of 3-digit code
dig3_3d = str(randrange(0,10))  # digit 3 of 3-digit code

three_dig_code = dig1_3d + dig2_3d + dig3_3d    # build 3-digit code

dig1_4d = str(randrange(1,7))   # digit 1 of 4-digit code
dig2_4d = str(randrange(1,7))   # digit 2 of 4-digit code
dig3_4d = str(randrange(1,7))   # digit 3 of 4-digit code
dig4_4d = str(randrange(1,7))   # digit 4 of 4-digit code

four_dig_code = dig1_4d + dig2_4d +dig3_4d + dig4_4d # build 4-digit code

# Print the generated codes
print("3-digit code:", three_dig_code)
print("4-digit code:", four_dig_code)
