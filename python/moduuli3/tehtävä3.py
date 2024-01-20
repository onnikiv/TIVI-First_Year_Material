sukupuoli = str(input("Anna sukupuoli: \n"))
hemoglobiini = float(input("Anna hemoglobiini: \n"))

if sukupuoli.lower() == "mies":
    if 134 <= hemoglobiini <= 195:
        print("Miehelle hemoglobiini arvo on normaali.")
    elif hemoglobiini > 195:
        print("Miehen hemoglobiiniarvo on korkea.")
    else:
        print("Miehen hemoglobiiniarvo on alhainen.")
elif sukupuoli.lower() == "nainen":
    if 117 <= hemoglobiini <= 175:
        print("Naiselle hemoglobiini arvo on normaali.")
    elif hemoglobiini > 175:
        print("Naiselle hemoglobiiniarvo on korkea.")
    else:
        print("Naiselle hemoglobiiniarvo on alhainen.")
else:
    print("Väärä sukupuoli.")
