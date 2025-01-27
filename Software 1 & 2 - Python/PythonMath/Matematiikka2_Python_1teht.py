# MATEMATIIKKA2 - 1. TEHTÄVÄ - PYTHON
import numpy as np

# [1.1.] - 1.tehtävä: Muunna asteiksi 
def eka_teht():
    eka_a = 2.493 # rad
    eka_b = 0.911 # rad
    ekan_teht_list = []
    ekan_teht_list.append(eka_a)
    ekan_teht_list.append(eka_b)
    kirjain = "a"
    print("1. Muunna asteiksi")
    
    for i in ekan_teht_list:
        print(f"{kirjain}) {np.degrees(i):.2f}° = {i:.2f} rad")
        kirjain = "b"

# [1.1.] - 2.tehtävä: Muunna radiaaneiksi
def toka_teht():
    toka_a = 137.7 #deg
    toka_b = 62.3 #deg
    tokan_teht_list = []
    tokan_teht_list.append(toka_a)
    tokan_teht_list.append(toka_b)
    kirjain = "a"
    print("\n2. Muunna radiaaneiksi")
    
    for i in tokan_teht_list:
        print(f"{kirjain}) {np.radians(i):.2f}° = {i:.2f} rad")
        kirjain = "b"
 
# [2.2.3.] - 3.tehtävä Laadi taulukko...

def taulukko_teht():
    c = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360] #deg
    print("\n3. Laadi taulukko...")
    
    for i in c:
        print(f"{i}° = {np.radians(i):.2f} rad")


# [2.2.1] - 2.tehtävä: Suorakulmainen kolmio

def kolmio_teht():
    a = 1.6 #m
    b = 2.3 #m
    c= np.hypot(a, b)
    print(f"\n2. Suorakulmion sivut:\na = {a} (m) - kateetti\nb = {b} (m) - kateetti\nc = {c:.2f} (m) - hypotenuusa\n")

eka_teht()
toka_teht()
taulukko_teht()
kolmio_teht()