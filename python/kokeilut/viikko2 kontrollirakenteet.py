#sisäiset kontrollirakenteet ja satunnaisuus
import random
"""
random_number = random.randint(1,3)
print(f"Arvottu numero: {random_number}")
"""
#pelin "asetukset"
player_count = 6
dice_amount = 1

best_player = None
best_result = 0

#jokainen pelaaja suorittaa vurollaan, aloitetaan pelaajasta 1
current_player = 1
while current_player <= player_count:
    result = 0 # silmälukujen summa ennen heittoja
    throw_count = 0 # iteraattori nopan heittojen määrälle
    # noppia heitetään dice_amount - muuttujassa asetettu määrä
    while throw_count < dice_amount:
        die = random.randint(1, 6)
        print(f"Pelaaja {current_player} , {throw_count+1}. Heitto {die}:")
        result = result + die
        throw_count += 1 # sama kuin throw_count = throw_count + 1
    print(f"Pelaajan {current_player} tulos: {result}")
    #testataan saantiinko uusi paras tulos, ja tallennetaan tarvittaessa edellisen
    #parhaan tuloksen "tilalle" ja päivitetään samalla paras pelaaja
    if result > best_result:
        best_result = result
        best_player = f"Pelaaja {current_player}"
    # jos tulos ei ole parempi, mutta ton sama kuin edellinen paras tulos
    # yhdistetään pelaajan nimi edellisen parhaan pelaajan nimen lisäksi samaan stringiin
    elif result == best_result:
        best_player = best_player + f", Pelaaja {current_player}"
    current_player = current_player + 1
print(f"Paras tulos: {best_result}, {best_player}.")


#break-komento, "heittää" ulos aktiivisesta silmukasta, suoritus jatkuu koodilohkon jälkeen

counter = 0
while True: # ikuinen silmukka
    print(f"Laskuri eka {counter}.")
    counter += 1
    if counter == 5:
        break # poistuu silmukan koodilohkosta samantien, allaoleva ei tulostu
    print(f"Laskuri toka {counter}.")