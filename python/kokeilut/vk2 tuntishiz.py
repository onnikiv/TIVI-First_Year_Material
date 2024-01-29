# import this
# import emoji -- ei wörki pycharmis
#user = input("Anna nimesi: \n")
#print(f"Moro, {user} 😂")

ikä = int(input("Anna ikäsi: \n"))
if 15 <= ikä < 18:
    paino = float(input("Anna paino (kg): \n"))
if (ikä >= 18 or (ikä >= 15 and paino >= 55)):
    print("Lääkkeen käyttö on sallittua.")
else:
    print("Lääkkeen käyttö on kielletty")
