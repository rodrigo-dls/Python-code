# Write a program that asks the user to enter the ICAO codes of two airports. The program prints out the distance between the two airports in kilometers. The calculation is based on the airport coordinates fetched from the database. Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/. Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE, write geopy into the search field and finish the installation.

import mysql.connector
from geopy.distance import geodesic

#  Function: runs queries
def run_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

# def
# Database connection
connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'rodrigod',
    password = '',
    autocommit=True
)

# Program
# Gets user data
airports = []  # collects airport data in tuples (ICAO code, airport name, latitude, longitude)
user_inputs = [] # collects the ICAO codes from the user

# Requests user data, queries DB and store data in a dictionary
for i in range(2):
    user_inputs.append(input(f"Enter the ICAO code of airport {i}: "))

    query = f"SELECT name, airport.latitude_deg, airport.longitude_deg FROM airport WHERE ident LIKE '{user_inputs[i]}'"
    result = run_query(connection, query)

    for row in result:
        airports.append((user_inputs[i], row[0], float(row[1]), float(row[2]))) # ('ICAO code','airport name','latitude','longitude')

# Calculate distance
loc_1 = (airports[0][2], airports[0][3]) # (latitude, longitude)
loc_2 = (airports[1][2], airports[1][3]) # (latitude, longitude)
distance_km = geodesic(loc_1, loc_2).kilometers

print(f"The distance between {airports[0][1]} and {airports[1][1]} is {distance_km:.2f}km.")
