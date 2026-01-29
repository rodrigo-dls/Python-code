# Exercise 3
# Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres. Write a main program that asks for a volume in gallons from the user and converts the value to liters. The conversion must be done by using the function. Conversions continue until the user inputs a negative value.

def gal_to_lit(vol):
    return vol * 3.79

while True:
    vol_gal = float(input("Enter the quantity of gasoline in gallons: "))
    if vol_gal < 0:
        print("That was a negative value. Bye.")
        break
    vol_lit = gal_to_lit(vol_gal)
    print(f"{vol_gal} of gasoline equals to {vol_lit} liters of gasoline.")
