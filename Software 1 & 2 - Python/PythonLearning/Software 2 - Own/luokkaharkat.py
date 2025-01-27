"""class Auto:
    
    def __init__(self, rekisteri_nro, max_nopeus, ajettu_matka=0):
        self.rekisteri_nro = rekisteri_nro
        self.max_nopeus = max_nopeus
        self.ajettu_matka = ajettu_matka

    def aja_matka(self, matka):
        self.ajettu_matka += matka
    
    def ominaisuudet(self):
         print(f"Rekisteri: {self.rekisteri_nro} --- Max nopeus: {self.max_nopeus} --- Ajettu matka: {self.ajettu_matka} ")
                
auto1 = Auto("ABC-123", 100)
auto1.ominaisuudet()
auto1.aja_matka(235)
auto1.ominaisuudet()


# http://127.0.0.1:3000/summa?luku1=<arvo>&luku2=<arvo>

from flask import Flask, request

app = Flask(__name__)
@app.route('/summa')
def summa():
    args = request.args
    luku1 = float(args.get("luku1"))
    luku2 = float(args.get("luku2"))
    summa = luku1+luku2

    vastaus = {
        "luku1" : luku1,
        "luku2" : luku2,
        "summa" : summa
    }

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
    
"""
from flask import Flask

app = Flask(__name__)
@app.route('/summa/<luku1>/<luku2>')
def summa(luku1, luku2):
    
        luku1 = float(luku1)
        luku2 = float(luku2)
        summa = luku1+luku2

        vastaus = {
            "luku1": luku1,
            "luku2": luku2,
            "summa": summa
            }
        return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)