class Building:
    def __init__(self, address, num_floors):
        self.address = address
        self.num_floors = num_floors


class Apartment(Building):
    def __init__(self, address, num_floors, floor, num):
        super().__init__(address, num_floors)
        self.floor = floor
        self.num = num

    def print_info(self):
        print(f'Apartment {self.num} floor: {self.floor}')


myApartment = Apartment("Keskuskatu 1", 7, 6, 20)

myApartment.print_info()

##########################


class Engine:
    count = 0

    def __init__(self, capacity, type = "fuel"):
        self.capacity = capacity
        self.type = type
        Engine.count = Engine.count + 1
        self.sn = Engine.count


class Vehicle:
    def __init__(self, brand, model, year, engine):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = engine

    def start(self):
        print(f'Vehicle {self.year} {self.model} {self.brand} {self.engine.type} {self.engine.sn}')

    def stop(self):
        print(f'Vehicle {self.year} {self.model} {self.brand} {self.engine.type} {self.engine.sn}')


engine1 = Engine(145)
engine2 = Engine(150, "Hybrid")
vehicle1 = Vehicle("brand", "model", 2007, engine1,)


###############################################################

from flask import Flask, Response

app = Flask(__name__)


@app.route("/min/<a>/<b>/<c>/")
def find_min(a, b, c):
    #   k = min(a, b, c)
    luku1 = int(a)
    luku2 = int(b)
    luku3 = int(c)

    result = min(luku1, luku2, luku3)

    response = {
        "a": luku1,
        "b": luku2,
        "c": luku3,
        "min": result
    }
    return response

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1',port=3000)