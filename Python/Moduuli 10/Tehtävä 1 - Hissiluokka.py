
class Hissi:
    
    def __init__(self):
        self.pohja_kerros = 0
        self.korkein_kerros = 5
    

    def kerros_ylos(self):
        if self.pohja_kerros < self.korkein_kerros:
            self.pohja_kerros += 1
        else:
            print("Olet jo ylimmässä kerroksessa.")
    
    def kerros_alas(self):
        if self.pohja_kerros > 0:
            self.pohja_kerros -= 1
        else:
            print("Olet jo alimmassa kerroksessa.")

    def kerros(self):
        print(f"Olet kerroksessa {self.pohja_kerros}.")

    
hissi1 = Hissi()
hissi1.kerros_ylos(1)