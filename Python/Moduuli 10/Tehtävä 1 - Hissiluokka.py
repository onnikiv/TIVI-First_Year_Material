class Hissi:
    
    def __init__(self, kerros=0):
        self.kerros = kerros

    def kerros_alas(self):
        kerros = kerros - 1
        print(f"Menty alaspäin.")

    def kerros_ylos(self):
        kerros = kerros + 1
        print(f"Menty ylöspäin.")


    def siirry_kerrokseen(self, kerros):
        kerros_syote = int(input("Mihin kerrokseen haluat mennä? "))
        