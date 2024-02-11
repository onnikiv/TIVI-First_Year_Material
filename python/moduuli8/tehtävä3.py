import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect( #Yhteys tietokantaan.
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)


def coordinate_search(ICAO):
    cursor = connection.cursor()
    cursor.execute(f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{ICAO}'")
    result = cursor.fetchall()
    return result

Icao_1_coordinate = coordinate_search(input("Anna ensimmäinen ICAO-koodi:\n "))
Icao_2_coordinate = coordinate_search(input("Anna toinen ICAO-koodi:\n "))

distance = geodesic(Icao_1_coordinate, Icao_2_coordinate).kilometers

print(f"Etäisyys kahden lentokentän välillä on {distance:.2f} km.")