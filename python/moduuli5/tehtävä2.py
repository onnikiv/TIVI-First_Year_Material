luvut = [] # tyhjä lista

# Kysytään kokoajan lukuja, jos käyttäjä vastaa tyhjän merkkijonon, kysely loppuu.
while True:
    luku_syote = int(input("Anna luku: \n"))

    if luku_syote == "":
        break
    else:
        luku = int(luku_syote)
        luvut.append(luku)
print(f"Syötetyt luvut: {luvut}")