luku_string = input("Anna luku: \n")
alkuluku = 0
if luku_string.isdigit():   #Tarkistetaan syöttö, jos luku niin tehdään merkkijonosta(str) luku(int).
    luku = int(luku_string)

    if luku < 2:    #Jos alle 2 ei voi olla alkuluku
        print(f"{luku} ei ole alkuluku.")
    else:
        alkuluku = True  # Aluksi alkuluku on totta.
        for i in range(2, int(luku ** 0.5) + 1):
            if luku % i == 0:
                alkuluku = False
                break
    if alkuluku:
        print(f"{luku} on alkuluku.")
    else:
        print(f"{luku} ei ole alkuluku.")
else:
    print("Virheellinen syöte. Syötä kokonaisluku.")