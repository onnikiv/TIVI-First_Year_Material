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

# 127.0.0.1:3000/kenttä/EFHK
@app.route(f'/kenttä/<string:ICAO>', methods=['GET'])
def kenttä_haku(ICAO):
    cursor = connection.cursor()
    cursor.execute(f"SELECT name, municipality FROM airport WHERE ident='{ICAO.upper()}'")
    result = cursor.fetchall()
    Name = result[0][1]
    Municipality = result[0][0]

    if result:
        return {'ICAO': ICAO.upper(),'Name': Name, 'Municipality': Municipality,}
    else:
        return {'error': 'Airport not found.', 'status': 404}


@app.errorhandler(404)
def page_not_found(error):
    response_body = json.dumps(
        {'error': error.name, 'description': error.description, 'status': error.code}
    )
    return Response(
        response=response_body,
        status=404,
        mimetype='application/json'
    )


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

