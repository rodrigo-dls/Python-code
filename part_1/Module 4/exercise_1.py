# Exercise 1
print("\n------- Exercise 1: ------\n")

# Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.

n = 1

while n <= 1000:
    if n % 3 == 0:
        print(n)
    n += 1