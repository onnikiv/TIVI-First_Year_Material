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