# Exercise 2
print("\n------- Exercise 2: ------\n")

# Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.

INCH_TO_CM = 2.54  # 1 inch = 2.54 cm
value = float(input("Enter the value in inches: "))

while value >= 0:
    print(f"Value in cm: {value * INCH_TO_CM:.2f}")
    value = float(input("Enter the value in inches: "))
print("That is a negative value. Program ends.")
