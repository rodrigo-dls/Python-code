# Exercise 1
print("\n------- Exercise 1: ------\n")

# Write a program that asks a fisher the length of a zander in centimeters. If the zander does not fulfill the size limit, the program instructs to release the fish back into the lake and notifies the user of how many centimeters below the size limit the caught fish was. A zander must be 42 centimeters or longer to meet the size limit.

# Get data
fish_length = float(input("Enter the size of the fish (in centimeters): "))
MINIMUM_LENGTH = 42

# Process data
if fish_length < MINIMUM_LENGTH:
    difference_length = MINIMUM_LENGTH - fish_length
    print(f"The fish size does not fulfill the size limit, it is {difference_length:.2f} under the size limit. Please release the fish back into the lake.")
else:
    print("Well done. The fish size is acceptable.")
