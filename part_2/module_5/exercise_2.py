# Implement a backend service that gets the ICAO code of an airport and then returns the name and location of the airport in JSON format. The information is fetched from the airport database used on this course. For example, the GET request for EFHK would be: http://127.0.0.1:5000/airport/EFHK. The response must be in the format of: {"ICAO":"EFHK", "Name":"Helsinki-Vantaa Airport", "Location":"Helsinki"}.

from flask import Flask, Response
import mysql.connector
import json

# Database connection
def connect_db():
    return mysql.connector.connect(
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
        print(result)
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
    connection = connect_db()
    data  = get_name_and_location(connection, icao_code.upper() )

    if data == "db_error":
        # The db query failed
        response = {
            "message": "Server error.",
            "status": 500
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=500, mimetype="application/json")
        return http_response

    if data is None:
        # The db query worked but didn't match any airports.
        response = {
            "message": "Airport not found.",
            "status": 404
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response,
                                 status=404,
                                 mimetype='application/json')
        return http_response

    # The db query worked. Prepare data to be sent
    response = {
        "ICAO": icao_code,
        "Name": data[0],
        "Location": data[1]
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=200, mimetype="application/json")
    return http_response

@app.errorhandler(404)
def page_not_found(error):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype='application/json')
    return http_response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000 )