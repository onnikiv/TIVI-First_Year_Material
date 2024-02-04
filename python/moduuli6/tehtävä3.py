def gallonat_litroiksi(gallonat): #Funktio gallonat litroiksi
    litrat = gallonat * 3.785
    return litrat


def paaohjelma():
    while True:
        gallonat_syotto = input("Syötä bensiinin määrä gallonoina (lopetus negatiivisella luvulla): \n")

        if gallonat_syotto[0] == '-' and gallonat_syotto[1:].replace('.', '', 1).isdigit():
            print("Lopetus")
            break

        elif gallonat_syotto.replace('.', '', 1).isdigit():
            gallonat = float(gallonat_syotto)
            litrat = gallonat_litroiksi(gallonat)
            print(f"{gallonat} nestegallonaa on {litrat:.2f} litraa.")

        else:
            print("Virheellinen syöte. Syötä luku.")


paaohjelma()
