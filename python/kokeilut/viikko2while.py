#while-silmukat (loopit)

#jakolaskukone, jakaja ei voi olla nolla.
""" monen rivin merkkijono (lainausmerkeillä)
jaettava = float(input("Anna jaettava: \n"))
jakaja = float(input("Anna jakaja: \n"))
while jakaja == 0:
    print("Ei voi olla nolla.")
    jakaja = float(input("Anna jakaja: \n"))


tulos = jaettava / jakaja
print(f"Jakolaskun tulos: {tulos:.2f}")
"""
# iteroiva silmukka (käytetään "laskuria" silmukan toistokertojen määrittelyyn)
#i = 1  #iteraattori i

i = int(input("Mistä numerosta aloitetaan? \n"))
amount = int(input("Kuinka monta numeroa tulostetaan? \n"))
offset = int(input("Anna numeroiden väli: "))
max_number = amount * offset + i
while i < max_number:
    print(f"Numero on {i}")
    i = i + offset
print(f"i:n lopullinen arvo silmukan jälkeen: {i}.") # 11

#voit testata ehtolauseiden toimintaa tulostamalla niiden arvoja
print(i < i+1) # -> True