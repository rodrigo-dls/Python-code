# Write a program that asks the user to enter the ICAO code of an airport. The program fetches and prints out the corresponding airport name and location (town) from the airport database used on this course. The ICAO codes are stored in the ident column of the airport table.
import mysql.connector

def run_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

# Create connection con flight_game database
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='rodrigod',
    password='',
    autocommit=True
)

# program: ask user icao code for the SQL query
user_input = input("Enter the ICAO code of an airport: ")
query = f"SELECT name, municipality FROM airport WHERE ident = '{user_input}'"

# program: query the db
result = run_query(connection, query)

# program: prints name and location
for row in result:
    print(f"Airport name: {row[0]}")
    print(f"Airport location: {row[1]}")