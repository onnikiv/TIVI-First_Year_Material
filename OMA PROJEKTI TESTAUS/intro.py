#-------------------------------------------------------------------------------
# ONNIN SPAGETTI KOODIA

from Asciiartfunc import welcome_text_to_ascii # Tuodaan Asciiartfunc.py tiedostosta welcome_text_to_ascii() funktio tähän tiedostoon.


def intro(): # Intro funktio TestiTestiTesti
    welcome_text_to_ascii() # Kutsutaan Asciiartfunc.py tiedostosta welcome_text_to_ascii() funktiota, jolla saadaan hieno ASCII taideteos.
    while True: # Looppi joka kysyy käyttäjältä haluaako hän aloittaa pelin, jos vastaus on "yes" peli alkaa, jos "no" peli loppuu. Muussa tapauksessa kysytään uudelleen.
        intro_input = input("Do you wish to Start the game? (yes/no): \n").lower()
        if intro_input == "yes":
            print("\nGreat! Let's get started!")
            return True # Palauttaa True jos käyttäjä vastaa "yes" ja peli jatkuu.
        elif intro_input == "no":
            print("\nGoodbye!")
            return False # Palauttaa False jos käyttäjä vastaa "no" ja peli loppuu.
        else:
            print("\nInvalid input, please try again:")


def airplane_model_choice(): #Funktio lentokonemallin valintaan. Kysyy käyttäjältä haluamansa lentokonemallin ja tulostaa valinnan. Jos käyttäjä antaa väärän syötteen, pyytää syöttämään uudelleen.
    while True: 
        airplane_model_input = input("Choose your airplane model (1-3): \n 1. Boeing 737 \n 2. Airbus A320 \n 3. Saab JA 37 Viggen \n").lower()
        if airplane_model_input == "1":
            print("You have chosen the Boeing 737.")
            break
        elif airplane_model_input == "2":
            print("You have chosen the Airbus A320.")
            break
        elif airplane_model_input == "3":
            print("You have chosen the Saab JA 37 Viggen.")
            break
        else:
            print("\nInvalid input, please try again:")


def intro_airplane_func(): #Funktio joka kutsuu molemmat "intro ja airplane_model_choice" funktiot <--- siirretään myöhemmin main() funktioon.
    if intro(): # Tässä kohtaa testataan, että jos alussa sanotaan "no" niin peli loppuu, muussa tapauksessa kutsutaan airplane_model_choice() funktiota.
        airplane_model_choice() # Jos intro() palauttaa True, kutsutaan airplane_model_choice() funktiota.
    

intro_airplane_func() # Testataaan 

