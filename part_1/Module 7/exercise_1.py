# Write a program that asks the user for a number of a month and then prints out the corresponding season (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program. We can define each season to last three months, December being the first month of winter.

seasons = (
    'winter','winter',
    'spring', 'spring', 'spring',
    'summer', 'summer', 'summer',
    'autumn', 'autumn', 'autumn',
    'winter')

while True:
    user_input = int(input("Enter the number of a month to know the corresponding season: "))
    if 1 <= user_input <= 12:
        break
    else:
        print("The number has to be between 1 and 12.")

season = seasons[user_input-1]
print(f"That month corresponds to the {season}")
