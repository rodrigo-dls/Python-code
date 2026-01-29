# Exercise 1
import random

# Write a program that asks the user how many dice to roll. The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.

n_dice = int(input("Enter the number of dice to roll: "))
sum_of_dice = 0

for i in range(n_dice):
    die_result = random.randint(1,6)
    sum_of_dice += die_result

print(f"The sum of the numbers: {sum_of_dice}")