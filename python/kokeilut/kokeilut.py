age = 5
print(age)
age = 6
print(age + 2)
# merkkijono
age_string = "seitsemän"

# kokonaisluku
age_int = 6
# ei toimi: print(age_string + age_int)

# plus-lasku
print(age_int +4 )
# merkkijonojen liittäminen (concatenation)
print(age_string + " vuotta")

# liukuluvut (float) (ei ihan sama(tarkka) kuin desimaaliluku)
depth = 10.0
width = 70
area = depth * width
print(area)

# boolean: totta vai tarua (pythonissa myös 1 tai 0)
is_it_true = True
print(is_it_true)

# tyyppimuunnokset
age_input = input("Kuinka vanha olet?")
# print(type(ageInput)) #"13"
age_int = int(age_input) # esim "13" -> 13
new_age = age_int + 1

print("Vuoden päästä olet " + str(new_age) + " vuotta.")
# tai "f-stringillä (huom aaltosulkeet ja f-alkuun"
print(f"Vuoden päästä olet {new_age} vuotta.")
print("testi")
