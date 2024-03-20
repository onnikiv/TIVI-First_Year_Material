import random
numero = random.randint(1,10)
arvaus = int(input('Arvaa numero: '))
while arvaus != numero:
    if arvaus < numero:
        print('Liian pieni arvaus.')
    elif arvaus > numero:
        print('Liian suuri arvaus.')
    arvaus = int(input('Arvaa numero: '))
print('Oikea arvaus')