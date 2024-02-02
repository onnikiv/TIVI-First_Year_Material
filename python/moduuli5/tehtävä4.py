kaupungit = []

kaupunki = input("Anna kaupunki \n")
while kaupunki != "":
    kaupungit.append(kaupunki)
    kaupunki = input("Anna seuraava kaupunki tai lopeta painamalla Enter: ")

for kaupunki in kaupungit:
    print(kaupungit)