from flask import Flask, request, Response
import json
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)

app = Flask(__name__)

@app.route('/kenttä/<string:ICAO>', methods=['GET'])
def kenttä_haku(ICAO):
    cursor = connection.cursor()
    cursor.execute(f"SELECT name, municipality FROM airport WHERE ident='{ICAO.upper()}'")
    result = cursor.fetchone()
    
    if result:
        icao, name, municipality = ICAO.upper(), result[0], result[1]
        response_data = {"ICAO": icao, "Name": name, "Municipality": municipality}
        return json.dumps(response_data)
    else:
        response_data = {'error': 'Airport not found.', 'status': 404}
        return json.dumps(response_data)

@app.errorhandler(404)
def page_not_found(error):
    response_data = {'error': error.name, 'description': error.description, 'status': error.code}
    return Response(
        response=json.dumps(response_data),
        status=404,
        mimetype='application/json'
    )

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
