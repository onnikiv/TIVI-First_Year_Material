yritysten_maara = 0

while yritysten_maara < 5:
    tunnus = input("Syötä käyttäjätunnus: \n").lower()
    salasana = input("Syötä salasana: \n").lower()

    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa!")
        break

    else:
        print(f"Väärä käyttäjätunnus tai salasana. {5 - yritysten_maara} yritystä jäljellä")
        yritysten_maara += 1

    if yritysten_maara == 5:
        print("Pääsy evätty")
