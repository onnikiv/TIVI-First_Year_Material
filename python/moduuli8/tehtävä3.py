import mysql.connector

connection = mysql.connector.connect( #Yhteys tietokantaan.
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)
