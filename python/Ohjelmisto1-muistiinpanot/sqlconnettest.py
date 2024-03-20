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

#Parempi tapa: kääritään yksittäiset toimimallisuudet uudelleenkäytettäviin funktioihin


def find_country_by_code(iso_code):
    sql = f"SELECT name, continent FROM country WHERE iso_country='{iso_code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    if cursor.rowcount == 1:
        return result
    return


def update_country_name_by_code(iso_code, name):
    sql = f"UPDATE country SET name='{name}' WHERE iso_country='{iso_code}'"
    #tarkista, että sql on oikein muodostettu
    #print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    if cursor.rowcount == 1:
        print(f"Tietue päivitetty ({iso_code}:{name}).")
        return True
    print("Pieleen meni.")


code_input = input("Anna Maakoodi: ")
country_input = input("Uusi nimi: ")
update_country_name_by_code(code_input, country_input)


user_input = input("Anna Maakoodi: ")
country = find_country_by_code(user_input)
# Jos country != None
if country:
    print(f"Löydetty maa: {country[0]}, {country[1]}")
else:
    print("Ei tuloksia.")

