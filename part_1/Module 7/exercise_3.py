# Write a program for fetching and storing airport data. The program asks the user if they want to enter a new airport, fetch the information of an existing airport or quit. If the user chooses to enter a new airport, the program asks the user to enter the ICAO code and name of the airport. If the user chooses to fetch airport information instead, the program asks for the ICAO code of the airport and prints out the corresponding name. If the user chooses to quit, the program execution ends. The user can choose a new option as many times they want until they choose to quit. (The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of Helsinki-Vantaa Airport is EFHK. You can easily find the ICAO codes of different airports online.)

# enter new airport, (enter ICAO and name)
# fetch info (ask for ICAO and print the name)
# quit

# Variables

airports = {}

# Functions

def add_new_airport(airports_dict):
    airport_code = input("Enter ICAO code of the airport: ")
    airport_name = input("Enter the name of the airport: ")
    airports_dict[airport_code] = airport_name

def fetch_airport_info(airports_dict, airport_code):
    if airport_code in airports_dict:
        print(
            f"The airport's name is {airports_dict[airport_code]}")
    else:
        print("The ICAO code does not exist.")

# Program

print("Welcome to the airports program.")
while True:
    user_input = int(input(
            "Actions:\n"
            "1. Enter a new airport.\n"
            "2. Fetch information of an airport.\n"
            "3. Quit\n"))

    if user_input == 1:
        print("1. Enter a new airport.")
        add_new_airport(airports)
    elif user_input == 2:
        print("2. Fetch information of an airport.")
        airport_code = input("Enter the ICAO code of the airport: ")
        fetch_airport_info(airports, airport_code)
    elif user_input == 3:
        print("Bye.")
        break
    else:
        print("Invalid input.")





