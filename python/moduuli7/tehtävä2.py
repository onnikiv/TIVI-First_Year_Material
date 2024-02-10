nimet_joukko = set()

def nimet_lisays():
    while True:
        uusi_nimi = input("Anna nimi (tyhjä lopettaa):\n").lower()
        
        if uusi_nimi == "":
            break
        
        elif uusi_nimi in nimet_joukko:
            print("Nimi on jo listalla")
        
        else: 
            nimet_joukko.add(uusi_nimi)
            print("Nimi lisätty")
    
    return nimet_joukko

nimet_lisays()
print(f"Syötetyt nimet: \n{nimet_joukko}")
