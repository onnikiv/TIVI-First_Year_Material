import mysql.connector

connection = mysql.connector.connect( #Yhteys tietokantaan.
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)


def query_landcode(user_input): #Kysely maakoodista, mikä tsekkaa onko siinä tietyssä maassa mitäkin lentokenttätyyppejä.
    cursor = connection.cursor()
    cursor.execute(f"SELECT type FROM airport WHERE iso_country='{user_input}' ORDER BY type")
    results = cursor.fetchall()
    airport_types = {
        "closed": 0,
        "heliport": 0,
        "small_airport": 0,
        "medium_airport": 0,
        "large_airport": 0,
        "seaplane_base": 0,
        "balloonport": 0
    }

    for result in results: #Käydään läpi tulokset ja lisätään ne airport_types dictionaryyn.
        a_type = result[0]
        
        if a_type in airport_types:
            airport_types[a_type] += 1

    return airport_types

while True: #Kysytään käyttäjältä maakoodia ja tarkistetaan onko se olemassa.
    user_input = input("Anna maakoodi:\n ").upper()
    field_types = query_landcode(user_input)

    if field_types:  
        print(f"Maassa {user_input} on seuraavat lentokenttätyypit: {field_types}.")
        break
    else:
        print("Virheellinen maakoodi.")