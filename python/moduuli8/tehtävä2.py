import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)


def query_for_all_airport_types():
    cursor = connection.cursor()
    cursor.execute(f"SELECT type FROM airport WHERE iso_country= '{user_input}' ORDER BY type")
    result = cursor.fetchall()
    
    for row in result:
        print(row)



query_for_all_airport_types()