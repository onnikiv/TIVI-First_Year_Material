import random


def Nopan_heitto(eyeInt):
    return random.randint(1, eyeInt)


tahkot = int(input("Anna nopan tahkojen määrä: \n"))
noppa = 0

while noppa != tahkot:
        noppa = Nopan_heitto(tahkot)
        print(noppa)
