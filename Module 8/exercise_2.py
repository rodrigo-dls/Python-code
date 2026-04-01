# Write a program that asks the user to enter the area code (for example FI) and prints out the airports located in that country ordered by airport type. For example, Finland has 65 small airports, 15 helicopter airports and so on.

import mysql.connector

# Function: Queries the DB
def run_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

# Database connection
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='rodrigod',
    password='',
    autocommit=True
)

# Program
user_input = input('Enter the area code of the airport: ')

query = f"SELECT country.name, COUNT(airport.type) AS count_type, airport.type FROM airport, country WHERE airport.iso_country = country.iso_country AND airport.iso_country LIKE '{user_input}' GROUP BY airport.type ORDER BY count_type DESC;"

result = run_query(connection, query)

print(result[0][0])
for row in result:
    str = row[2]
    print(row[1], str.replace("_"," "))
