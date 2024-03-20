print("Anna paino")

leivis = float(input("Leiviskät: "))
naula = float(input("Naulat: "))
luoti = float(input("Luodit: "))
paino = 13.3 * ((leivis * 20 + naula) * 32 + luoti)
print("Massa nykymittojen mukaan: " + str(int(paino / 1000)) + " kiloa " + str(int(paino % 1000)) + " grammaa.")
