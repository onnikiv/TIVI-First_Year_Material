import random


def nopanheitto(): #Funktio yksittäiselle nopanheitolle
    return random.randint(1,6)


def haluttu_kutonen(): #Pyöritetään siihen asti kun tulee kuusi.
    heiton_numero = 1 #Alustetaan heitot numeroidusti
    while True:
        heitto = nopanheitto()
        print(f"Heitto {heiton_numero}, Nopan silmäluku: {heitto}")
        heiton_numero += 1
        if heitto == 6: #Kun tulee luvuksi kuusi -> print ja break
            print(f"Katohan tulihan se kutonen!")
            break


haluttu_kutonen()
