alkuluvut = []
luku = 0
luku_syote = int(input("Anna luku: \n"))
if (luku_syote / luku_syote) == 0:
    if luku_syote % 1 == 0:

    alkuluvut.append(luku)
    if luku_syote == "":
        print("Virheellinen syöte.")
    else:
        print("Tämä ei ole alkuluku")


print(f"{luku} on alkuluku")
