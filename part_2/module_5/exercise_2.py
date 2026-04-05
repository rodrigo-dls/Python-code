# Implement a backend service that gets the ICAO code of an airport and then returns the name and location of the airport in JSON format. The information is fetched from the airport database used on this course. For example, the GET request for EFHK would be: http://127.0.0.1:5000/airport/EFHK. The response must be in the format of: {"ICAO":"EFHK", "Name":"Helsinki-Vantaa Airport", "Location":"Helsinki"}.

from flask import Flask, Response
import mysql.connector
import json

# Database connection
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='rodrigod',
    password='',
    autocommit=True
)

# Query the database, retrieves airport name and location by passing the icao code of the airport
def get_name_and_location(conn, icao_code):
    try:
        query = "SELECT name, municipality FROM airport WHERE ident = %s"
        cursor = conn.cursor()
        cursor.execute(query, (icao_code,))
        result = cursor.fetchone() # returns (name, municipality)
        cursor.close()

        if result:
            print(result)
        else:
            print("Airport not found.")

        return result
    except:
        print("Error consulting the database.")
        return "db_error"
    finally:
        if conn.is_connected():
            conn.close()


app = Flask(__name__)
@app.route('/airport/<icao_code>')
def get_country(icao_code):
    # Retrieve data from database
    print(icao_code)
    data  = get_name_and_location(connection, icao_code.upper() )
    print(data)

    if data == "db_error":
        json_response = json.dumps(data)
        http_response = Response(response=json_response, status=500, mimetype="application/json")
        return http_response

    # Prepare data to be sent
    response = {
        "ICAO": icao_code,
        "Name": data[0],
        "Location": data[1]
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=200, mimetype="application/json")
    return http_response

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000 )