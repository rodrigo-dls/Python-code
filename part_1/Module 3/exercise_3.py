# Exercise 3
print("\n------- Exercise 3: ------\n")

# Write a program that asks for the biological gender and hemoglobin value (g/l). The program the notifies the user if the hemoglobin value is low, normal or high.
#
#     A normal hemoglobin value for adult females is between 117-155 g/l.
#     A normal hemoglobin value for adult males is between 134-167 g/l.
#

#  Get data
gender = input("Enter your gender: ")
hemoglobin = float(input("Enter hemoglobin value (g/l): "))

# Process data
if gender == "male":
    if hemoglobin < 134:
        print("Hemoglobin value is low.")
    elif hemoglobin <= 167:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")
elif gender == "female":
    if hemoglobin < 117:
        print("Hemoglobin value is low.")
    elif hemoglobin <= 155:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")
else:
    print("Invalid gender.")
