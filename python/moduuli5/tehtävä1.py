import random

arpakuutioiden_lukum = int(input("Anna arpakuutioiden lukumäärä: \n"))

if arpakuutioiden_lukum <= 0:
    print("Arpakuutioiden lukumäärän pitää olla positiivinen.")
else:
    tuloksen_summa = 0
    for i in range(arpakuutioiden_lukum):
        silmaluku = random.randint(1,6)
        print(f"Heitto: {silmaluku}")
        tuloksen_summa += silmaluku

print(f"Heitettyjen arpakuutioiden summa: {tuloksen_summa}")