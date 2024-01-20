valinta = str(input("Anna hyttiluokka \n")).lower()
if valinta == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif valinta == "a":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif valinta == "b":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif valinta == "c":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")
