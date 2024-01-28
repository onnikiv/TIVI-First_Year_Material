import random

randomi_luku = random.randint(1, 10)
luku_input = int(input(f"Anna luku väliltä 1-10 \n"))
while randomi_luku == luku_input:
    print("Oikea vastaus:")
    if luku_input <= randomi_luku:
        print("Liian korkea")