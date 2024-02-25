lentoasemat = {
"EFHK":"Helsinki-Vantaa",
"EHAM":"Amsterdam Schiphol Airport",
"LTCJ":"Batman Airport",
"EDDB":"Berlin Schönefeld Airport",
"EDDF":"Frankfurt Airport",
"LIME":"Milano Bergamo Airport",
"EKCH":"Copenhagen Airport",
"EGKK":"London Gatwick Airport",
"EDDM":"Munich Airport",
"LIRF":"Rome Fiumicino Airport",
"LEMD":"Madrid Barajas Airport",
"LEBL":"Barcelona Airport",
}


while True:
    print("---------------------------------")
    print("1. Uusi lentoasema")
    print("2. Hae lentoasema")
    print("3. Lopeta")

    valinta = input("Valintasi: ")

    if valinta == "1":
        icao_koodi = input("Syötä lentoaseman ICAO-koodi: ")
        nimi = input("Syötä lentoaseman nimi: ")
        lentoasemat[icao_koodi] = nimi
        print("Lentoasema tallennettu.")

    elif valinta == "2":
        icao_koodi = input("Syötä lentoaseman ICAO-koodi: ")
        if icao_koodi in lentoasemat:
            print("Lentoaseman nimi:", lentoasemat[icao_koodi])
        else:
            print("Lentoasemaa ei löytynyt.")

    elif valinta == "3":
        break

    else:
        print("Virheellinen valinta. Valitse 1, 2 tai 3.")

print("Lopetetaan.")

