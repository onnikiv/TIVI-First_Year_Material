yritysten_määrä = 0

while yritysten_määrä < 5:
    tunnus = input("Syötä käyttäjätunnus: \n")
    salasana = input("Syötä salasana: \n")

    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa!")
        break

    else:
        print(f"Väärä käyttäjätunnus tai salasana. {4 - yritysten_määrä} yritystä jäljellä")
        yritysten_määrä += 1

    if yritysten_määrä == 5:
        print("Pääsy evätty")
