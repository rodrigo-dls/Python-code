# Exercise 6
# Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza in euros. The function calculates and returns the unit price of the pizza per square meter. The main program asks the user to enter the diameter and price of two pizzas and tells the user which pizza provides better value for money (which of them has a lower unit price). You must use the function you wrote for calculating the unit prices.

import math

def price_by_size(diameter, price):
    radius_m = diameter * 10e-2 / 2     # convert cm -> m
    area = math.pi * (radius_m ** 2)
    return price / area

pizza1_size = float(input("What's the diameter of the first pizza in cm? "))
pizza1_price =  float(input("What's the price of the first pizza? "))

pizza2_size = float(input("What's the diameter of the second pizza in cm? "))
pizza2_price =  float(input("What's the price of the second pizza? "))

pizza1_score = price_by_size(pizza1_size, pizza1_price)
pizza2_score = price_by_size(pizza2_size, pizza2_price)

if pizza1_score < pizza2_score:
    print("The first pizza provides better value for money.")
elif pizza1_score > pizza2_score:
    print("The second pizza provides better value for money.")
else:
    print("Both pizza provide the same value for money. Feel free to chose!")