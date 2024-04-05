# Käytännössä tehdään funktio, jota voidaan käyttää myöhemmin. Eikä tarvitse aina kirjoittaa uudelleen.

# Yksinkertainen funktio
# def do_something():
#     print("Teen jotain")
#     print("ja jotain muuta")
# do_something()
# print("Jotain muuta koodia")
# do_something()

# Parametrisoitu funktio
def calculate_numbers(calc_type, num1, num2):
    #print(f"{num1 + num2}")
    if calc_type == "add":
        return num1 + num2
    elif calc_type == "multiply":
        return num1 * num2
    return "No such calculation type."

sum_of_nums = calculate_numbers("add",2,3)
print(f"Summa: {sum_of_nums}")
print(f"Tulo: {calculate_numbers('multiply',2,3)}")


#Lista parametreinä
def calculate_numbers_list(calc_type, numbers):
    if calc_type == "add":
        numbers_sum = 0
        for num in numbers:
            numbers_sum += num
        return numbers_sum
    elif calc_type == "multiply":
        result = 1
        for num in numbers:
            result = result * num
        return result
    return "No such calculation type."


sum_of_nums = calculate_numbers_list("add", [1, 2, 3, 4])
print(f"Summa: {sum_of_nums}")
print(f"Tulo: {calculate_numbers_list('multiply',[1, 2, 3, 4])}")

# Lista parametreinä
inventory = ["kynä", "kumi"]
def add_stuff(item, new_inventory):
    new_inventory.append(item)
    print("Reppuun lisättiin " + item)
    return new_inventory


updated_inventory = add_stuff("tietokone", inventory)

inventory.append("hiiri")

print(inventory)
print(updated_inventory)
updated_inventory.append("kuulakynä")
print(inventory)

# Materiaali primitiiviarvoilla
def vaihda(kaupunki):
    kaupunki = "Vantaa"
    print("Funktiossa lopuksi: " + kaupunki)
    return

kaupunki = "Helsinki"
print("Pääohjelmassa aluksi: " + kaupunki)
vaihda(kaupunki)
# Alkuperäisen muuttujan arvo ei muuttunut
print("Pääohjelmassa lopuksi: " + kaupunki)

# nimetyt parametrit
def calc_v2(num1, num2, calc_type = "add"):
    if calc_type == "add":
        return num1 + num2
    elif calc_type == "multiply":
        return num1 * num2

# käytetään laskutavalle oletusarvoa
result = calc_v2(2,4)
print(result)
# Syötetään parametrit vapaa järjestyksellä nimeämällä ne
result = calc_v2(num2=2, num1=4, calc_type="multiply")
print(result)

# Satunnainen määrä parametreja


def list_numbers(*parameters):
    # parameters sisältää kaikki annetut parametrien arvot yhtenä monikkkona
    # ("kiinteä" lista)
    return parameters


print(list_numbers(2, 5, 7, "kutonen"))
