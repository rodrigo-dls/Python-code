# Exercise 4
print("\n------- Exercise 4: ------\n")

# Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year. A year is a leap year if it is divisible by four. However, years divisible by 100 are leap years only if they are also divisible by 400.

# Get data
year = int(input("Enter a year: "))

# Process data
if year % 400 == 0:
    print(f"The year {year} is a leap year.")
elif year % 100 == 0:
    print(f"The year {year} is not a leap year.")
elif year % 4 == 0:
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")