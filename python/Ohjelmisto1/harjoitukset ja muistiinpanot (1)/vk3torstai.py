# # MONIKKO, JOUKKO JA SANAKIRJA
#
# munmonikko = (1,3,5,9,12)
# print(munmonikko[2:])
#
# munmonikko = (1, 3, 5)
# eka, toka, kolmas = munmonikko
# print(toka)

 # mun1 = (1,2,3)
 # mun1.append(5)
 # print(mun1)
 # EI TOIMI KOSKA TUPLE, EI voi lisätä tupleen

'''
# Tsekataan tuplayksiköt listasta
lista = ["John", 1, 5, 3, 1, "John", "True", "John"]
lista2 = []
def listat():
    for i in lista:
        if i not in lista2 or type(i) == bool:
            lista2.append(i)
listat()
print(lista2)
'''
#True print testi tsydeemi
# string = ""
# if string:
#     print("hello")
# else:
#     print("bye")

#print(True in [1,2,3])
# Lisätään toinen lista toiseen.
# lista = [1, 2, 3, 4]
# lista2 = [4, [6, 8], 9]
# lista3 = lista.extend(lista2)
#
# print(lista[5][1])
'''
x = 5
#print(id(x))
x = 6
#print(id(x))

lista = [1,2,3]
listab = [4, 5] 
listac = lista.extend(listab)
print(lista)
print(listac)
# print(id(lista))
# lista.append(4)
# print(id(lista))
'''

#JOUKKO <-- Joukouilla ei ole järjestystä, listoilla on
#listoissa append lisää listan loppupäähän, set toimii joukoissa että se vaan lisätään joukkoon (.add/.remove)
#add komento joukoissa ei lisää tuplana jos on sama id( tai johonkin joukkoon lisätään kaksi kertaa)
#nimet = {} <- ei voikäyttää koska aaltosulut on varattu dictionaryllle

'''nimet = set() # nimet joukko alustetaan tyhjänä'''

lista = ["John", 1, 5, 3, 1, "John", 1]
lista2 = set(lista)
print(lista2)

## TAI oneliner
print(list(set(["John", 1, 5, 3, 1, "John", 1])))
