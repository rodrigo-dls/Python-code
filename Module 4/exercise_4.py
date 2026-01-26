# Exercise 4
print("\n------ Exercise 4: ------\n")

import random

# Write a game where the computer draws a random integer between 1 and 10. The user tries to guess the number until they guess the right number. After each guess the program prints out a text: Too high, Too low or Correct. Notice that the computer must not change the number between guesses.

answer = random.randint(1,10)

while True:
    user_input = int(input("Guess an integer number between 1 and 10: "))
    if answer < user_input:
        print("Too high")
    elif answer > user_input:
        print("Too low")
    else:
        print("Correct")
        break
