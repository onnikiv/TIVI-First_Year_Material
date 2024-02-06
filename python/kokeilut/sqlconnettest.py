import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)
cursor = connection.cursor()
cursor.execute("SELECT iso_country, name FROM country WHERE name='FINLAND'")
# fetchone hakee yhden rivin tulosjoukoista
# result_row = cursor.fetchall()

result_row = cursor.fetchall()
print(f"Ensimmäinen rivi: {result_row[0]}, jossa maakoodi: {result_row[0][0]}")
print(f"Maakoodeja löytyi {cursor.rowcount} kappaletta.")

if cursor.rowcount > 0:
    for row in result_row:
        print(f"Maakoodi: {row[0]}, nimi: {row[1]}")

else:
    print("Ei tuloksia")