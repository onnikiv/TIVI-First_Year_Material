import math


def pizzan_hinta(d, cost):
    return math.pi*(d/2/100)**2/cost
pizza1 = [int(input('Anna pizzan halkaisija senttimetreinä: ')), int(input('Anna pizzan hinta: '))]
pizza2 = [int(input('Anna pizzan halkaisija senttimetreinä: ')), int(input('Anna pizzan hinta: '))]

if pizzan_hinta(pizza1[0], pizza1[1])>pizzan_hinta(pizza2[0], pizza2[1]):
    print('Ensimmäien pizza on edullisempi pinta-alaa kohden')

else:
    print('Toinen pizza on edullisempi pinta-alaa kohden')

