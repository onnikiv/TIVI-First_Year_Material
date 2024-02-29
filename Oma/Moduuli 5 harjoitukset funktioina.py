# ---------------------------------------------------------------------------------------------------------

# MODUULI 5, TEHTÄVÄ 1 

def useampi_arpakuutio():
    
    import random
    
    tuloksen_summa = 0 # alustettu nollaksi
    arpakuutioiden_lukum = int(input("Anna arpakuutioiden lukumäärä: \n")) # inputti noppien määrälle

    if arpakuutioiden_lukum <= 0: # ei voi olla negatiivinen
        print("Arpakuutioiden lukumäärän pitää olla positiivinen.")
    else: # muuten heitetään nopat
        tuloksen_summa = 0 # summa aluksi nolla
        heitto = 1 # heitto aluksi yksi

        for i in range(arpakuutioiden_lukum):
            silmaluku = random.randint(1,6) # yksittäinen noppa
            print(f"Heitto: {heitto} , Silmäluku: {silmaluku}") # ensimmäinen heitto on yksi, silmäluku on random jne.
            tuloksen_summa += silmaluku
            heitto += 1 # heitto kasvaa yhdellä joka kierroksella, siihen asti kun ollaan päästy haluttujen heittojen määrään
        print(f"Heitettyjen arpakuutioiden summa: {tuloksen_summa}")

# useampi_arpakuutio()


# MODUULI 5, TEHTÄVÄ 2

def viisi_suurinta_lukua():
    luvut = [] 
    luku_input = input("Anna luku: \n")
    
    while True:
        if luku_input == "":
            break
        else:
            luku_input = int(luku_input)
            luvut.append(luku_input)
            luku_input = input("Anna luku: \n")
    
    luvut.sort(reverse=True)
    print("Viisi suurinta lukua ovat: ")
    
    for luku in range(0,5):
        print(luvut[luku])

viisi_suurinta_lukua()


# MODUULI 5, TEHTÄVÄ 3


