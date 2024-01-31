luvut = [] # tyhjä lista
suurimmat_luvut = 0
# Kysytään kokoajan lukuja, jos käyttäjä vastaa tyhjän merkkijonon, kysely loppuu.
while True:
    luku_syote = input("Anna luku: \n")

    if luku_syote == "" or luku_syote == " ":
        break
    else:
        luku = int(luku_syote)
        luvut.append(luku)
        luvut.sort(reverse=True)

print(f"Suurimmat luvut: {luvut[:5]}.")

