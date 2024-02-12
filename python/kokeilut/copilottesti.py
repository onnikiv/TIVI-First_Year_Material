import math

def ratkaise_toisen_asteen_yhtalo(a, b, c):
    diskriminantti = b**2 - 4*a*c

    if diskriminantti > 0:
        x1 = (-b + math.sqrt(diskriminantti)) / (2*a)
        x2 = (-b - math.sqrt(diskriminantti)) / (2*a)
        return x1, x2
    elif diskriminantti == 0:
        x = -b / (2*a)
        return x
    else:
        return "Ei reaaliratkaisuja"

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

ratkaisut = ratkaise_toisen_asteen_yhtalo(a, b, c)
print(ratkaisut)