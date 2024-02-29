# ---------------------------------------------------------------------------------------------------------

# MODUULI 5, TEHTÄVÄ 1 

def useampi_arpakuutio():
    
    import random
    
    tuloksen_summa = 0      # alustettu nollaksi
    arpakuutioiden_lukum = int(input("Anna arpakuutioiden lukumäärä: \n"))      # inputti noppien määrälle

    if arpakuutioiden_lukum <= 0:       # ei voi olla negatiivinen
        print("Arpakuutioiden lukumäärän pitää olla positiivinen.")

    else:       # muuten heitetään nopat
        tuloksen_summa = 0 # summa aluksi nolla
        heitto = 1 # heitto aluksi yksi

        for i in range(arpakuutioiden_lukum):
            silmaluku = random.randint(1,6) # yksittäinen noppa
            print(f"Heitto: {heitto} , Silmäluku: {silmaluku}") # ensimmäinen heitto on yksi, silmäluku on random jne.
            tuloksen_summa += silmaluku
            heitto += 1 # heitto kasvaa yhdellä joka kierroksella, siihen asti kun ollaan päästy haluttujen heittojen määrään
        print(f"Heitettyjen arpakuutioiden summa: {tuloksen_summa}")

useampi_arpakuutio()

