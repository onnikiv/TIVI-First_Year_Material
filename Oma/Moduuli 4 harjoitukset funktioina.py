# ---------------------------------------------------------------------------------------------------------

# MODUULI 4, TEHTÄVÄ 1

def kolmella_jaolliset_alle_tuhat():
    i = 0
    while i < 1000:
        print(f"{i}")
        i = i + 3

kolmella_jaolliset_alle_tuhat()

# MODUULI 4, TEHTÄVÄ 2
def tuuma_cm():
    tuuma = 2.54
    tuuma_input = 0
    while True:
        tuuma_input = float(input(f"Anna tuumat: \n"))
        if tuuma_input < 0:
            break
        print(f"Senttimetreinä: {tuuma_input * tuuma}.")
    
tuuma_cm()

# MODUULI 4, TEHTÄVÄ 3

def kysytaan_lukuja():
    isoin_luku = float("-inf")
    pienin_luku = float("inf")
    
    while True:
        luku_input = input("Anna luku: \n")
        if luku_input == "":
            break
        else:
            luku_input = int(luku_input)
            if luku_input > isoin_luku:
                isoin_luku = luku_input
            if luku_input < pienin_luku:
                pienin_luku = luku_input
    print(f"Pienin luku on {pienin_luku} ja isoin luku on {isoin_luku}.")

kysytaan_lukuja()

# MODUULI 4, TEHTÄVÄ 4

def arpa_kone():
    import random
    random_luku = random.randint(1, 10) # luodaan random luku
    while True: # luodaan looppi, joka jatkuu kunnes arvataan oikein
        arvaus = int(input("Arvaa luku väliltä 1-10: \n"))
        if arvaus == random_luku:
            print("Onneksi olkoon, arvasit oikein!")
            break
        elif arvaus < random_luku:
            print("Luku on suurempi.")
        elif arvaus > random_luku:
            print("Luku on pienempi.")
        else:
            print("Väärin, arvaa uudelleen.")

arpa_kone()

# MODUULI 4, TEHTÄVÄ 5

def salasana_ja_tunnus():
    tunnus = "python"
    salasana = "rules"
    while True:
        tunnus_input = input("Anna tunnus: \n").lower()
        salasana_input = input("Anna salasana: \n").lower()
        if tunnus_input == tunnus and salasana_input == salasana:
            print("Tervetuloa!")
            break
        else:
            print("Väärin, yritä uudelleen.")

salasana_ja_tunnus()

# MODUULI 4, TEHTÄVÄ 6

def piin_likiarvo():
    import random

    N = n = 0

    while N < 10:
        #arvotaan yksi piste
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        N += 1
        print(f"Arvottu piste: {x}, {y}")
        if x * x + y * y < 1:
            n += 1
    print(f"Pisteitä yhteensä: {N}, joista ympyrän sisällä {n}.")

    
    pi = 4 * n / N
    print(f"Piin likiarvo on: {pi}")

piin_likiarvo()