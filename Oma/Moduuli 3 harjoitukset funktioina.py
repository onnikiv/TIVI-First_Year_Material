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
        print("Virheellinen hyttiluokka.")

hyttiluokat()


# MODUULI 3, TEHTÄVÄ 3

def hemoglobiini_arvo():
    sukupuoli = input("Anna sukupuoli: \n").lower().capitalize()
    hemoglobiini_input = float(input("Anna hemoglobiini: \n"))
    if sukupuoli is not str and hemoglobiini_input is not float:
        print("Virheellinen syöte.")
    if sukupuoli == "Mies":
        if hemoglobiini_input < 134:
            print("Hemoglobiiniarvo miehelle on alhainen.")
        elif hemoglobiini_input > 170:
            print("Hemoglobiiniarvo miehelle on korkea.")
        else:
            print("Hemoglobiiniarvo miehelle on normaali.")
    elif sukupuoli == "Nainen":
        if hemoglobiini_input < 117:
            print("Hemoglobiiniarvo naiselle on alhainen.")
        elif hemoglobiini_input > 157:
            print("Hemoglobiiniarvo naiselle on korkea.")
        else:
            print("Hemoglobiiniarvo naiselle on normaali.")

hemoglobiini_arvo()


# MODUULI 3, TEHTÄVÄ 4

def onko_karkausvuosi():
    # jos vuoden jakojäännös on 0, se on karkausvuosi
    # ja jos vuoden 100:n jakojäännös on 0, se ei ole karkausvuosi
    # mutta jos vuoden 100:n jaettavan vuoden 400:n jakojäännös on 0, se on karkausvuosi

    karkausvuosi_input = int(input("Anna vuosiluku: \n"))
    if karkausvuosi_input % 4 == 0 and (karkausvuosi_input % 100 != 0 or karkausvuosi_input % 400 == 0):
        print(f"Vuosi {karkausvuosi_input} on karkausvuosi.")
    else:
        print(f"Vuosi {karkausvuosi_input} ei ole karkausvuosi.")

onko_karkausvuosi()