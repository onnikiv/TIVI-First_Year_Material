luvut = [] # tyhjä lista
suurimmat_luvut = 0
# Kysytään kokoajan lukuja, jos käyttäjä vastaa tyhjän merkkijonon, kysely loppuu.
while True:
    luku_syote = input("Anna luku: \n")

    if luku_syote == "" or luku_syote == " ":
        break
    else:
        luku = luku_syote
        luvut.append(luku)
        suurimmat_luvut = sorted(luvut, reverse=True)[:5]
print(f"Suurimmat luvut: {suurimmat_luvut}.")

