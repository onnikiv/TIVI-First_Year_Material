# MODUULI 4, TEHTÄVÄ 1

def kolmella_jaolliset_alle_tuhat():
    i = 0
    while i < 1000:
        print(f"{i}")
        i = i + 3

# kolmella_jaolliset_alle_tuhat()

# MODUULI 4, TEHTÄVÄ 2
def tuuma_cm():
    tuuma = 2.54
    tuuma_input = 0
    while True:
        tuuma_input = float(input(f"Anna tuumat: \n"))
        if tuuma_input < 0:
            break
        print(f"Senttimetreinä: {tuuma_input * tuuma}.")
    
# tuuma_cm()

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

