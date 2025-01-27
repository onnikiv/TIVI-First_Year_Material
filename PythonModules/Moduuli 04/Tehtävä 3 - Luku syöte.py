numero = 0
isoin_luku = float("-inf")
pienin_luku = float("inf")

while True:
    luku = input("Anna luku: \n")
    if luku == "":
        break
    else:
        luku = int(luku)
        if luku > isoin_luku:
            isoin_luku = luku
        if luku < pienin_luku:
            pienin_luku = luku
print(f"Pienin luku on {pienin_luku} ja isoin luku on {isoin_luku}.")