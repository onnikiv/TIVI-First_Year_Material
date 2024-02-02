kaupungit = []  # Tyhjä lista

for i in range(5): # Kysytään viiden kaupungin nimet
    kaupunki = input("Syötä kaupungin nimi: ")
    kaupungit.append(kaupunki)  # Kaupunki listaan

print("Syötetyt kaupungit:") #Tulostetaan kaupungit
for kaupunki in kaupungit:
    print(kaupunki)
