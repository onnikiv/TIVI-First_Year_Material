def kolmella_jaolliset_alle_tuhat():
    i = 0
    while i < 1000:
        print(f"{i}")
        i = i + 3

#kolmella_jaolliset_alle_tuhat()

def tuuma_cm():
    tuuma = 2.54
    tuuma_input = 0
    while True:
        tuuma_input = float(input(f"Anna tuumat: \n"))
        if tuuma_input < 0:
            break
        print(f"Senttimetreinä: {tuuma_input * tuuma}.")
    
tuuma_cm()

