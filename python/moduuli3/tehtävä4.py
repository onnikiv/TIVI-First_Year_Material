karkausvuosi = int(input("Anna vuosiluku: \n"))
if karkausvuosi % 100 == 0 and karkausvuosi % 400 == 0 or karkausvuosi % 100 != 0 and karkausvuosi % 4 == 0:
    print("Tämä vuosi on karkausvuosi")
else:
    print("Tämä ei ole karkausvuosi")
