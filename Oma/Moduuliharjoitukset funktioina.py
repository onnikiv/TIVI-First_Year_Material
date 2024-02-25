# ---------------------------------------------------------------------------------------------------------

# MODUULI 2, TEHTÄVÄ 1 
def tervehdys():
    nimi = input("Anna nimesi: \n")
    print(f"Hei {nimi}!")
tervehdys()



# MODUULI 2, TEHTÄVÄ 2 
def circle_rad_to_area():
    rad = float(input("Anna ympyrän säde: \n"))
    area = 3.14 * rad**2
    print(f"Ympyrän pinta-ala on {area}")
circle_rad_to_area()



# MODUULI 2, TEHTÄVÄ 3 
def suorakulmio():
    kanta = float(input("Anna suorakulmion kanta: \n"))
    korkeus = float(input("Anna suorakulmion korkeus: \n"))
    pinta_ala = kanta * korkeus
    piiri = 2 * (kanta + korkeus)
    print(f"Suorakulmion pinta-ala on {pinta_ala} ja piiri on {piiri}.")
suorakulmio()


# MODUULI 2, TEHTÄVÄ 4 
def kolme_numeroa():
    luku1 = float(input("Anna ensimmäinen luku: \n"))
    luku2 = float(input("Anna toinen luku: \n"))
    luku3 = float(input("Anna kolmas luku: \n"))
    summa = luku1 + luku2 + luku3
    keskiarvo = summa / 3
    print(f"Lukujen summa on {summa} ja keskiarvo on {keskiarvo:.2f}.")
kolme_numeroa()


# MODUULI 2, TEHTÄVÄ 5 
def massat_kilogrammoiksi():
    leiviskä_syote = float(input("Anna leiviskät"))
    naula_syote = float(input("Anna naulat"))
    luoti_syote = float(input("Anna luodit"))
    paino = 13.3 * ((leiviskä_syote * 20 + naula_syote) * 32 + luoti_syote) 
    print(f"Massa nykymittojen mukaan {paino/1000:.1f} kilogrammaa ja {paino%1000:.2f} grammaa")
massat_kilogrammoiksi()


# MODUULI 2, TEHTÄVÄ 6 
import random

def random_kolmiluku():
    luku1 = random.randint(0,9)
    luku2 = random.randint(0,9)
    luku3 = random.randint(0,9)
    print(f"{luku1}{luku2}{luku3}")
random_kolmiluku()

def random_neliluku():
    luku1 = random.randint(1,6)
    luku2 = random.randint(1,6)
    luku3 = random.randint(1,6)
    luku4 = random.randint(1,6)
    print(f"{luku1}{luku2}{luku3}{luku4}")
random_neliluku()

# ---------------------------------------------------------------------------------------------------------
# MODUULI 3, TEHTÄVÄ 1 
def kuha_tehtava():
    kuhan_pituus = float(input("Anna kuhan pituus senttimetreinä: \n"))
    if kuhan_pituus < 37:
        print(f"Kuha on alimittainen. Laske kuha takaisin järveen. Kuha on {37-kuhan_pituus} liian lyhyt. ")

kuha_tehtava()

# MODUULI 3, TEHTÄVÄ 2

def hyttiluokat():
    syotto = input("Anna hyttiluokka: \n").upper()
    if syotto == "LUX":
        print("LUX on parvekkeellinen hytti yläkannella..")
    elif syotto == "A":
        print("A on ikkunallinen hytti autokannen yläpuolella.")
    elif syotto == "B":
        print("B on ikkunaton hytti autokannen yläpuolella.")
    elif syotto == "C":
        print("C on ikkunaton hytti autokannen alapuolella.")
    else:
        print("Virheellinen syöttö.")

hyttiluokat()