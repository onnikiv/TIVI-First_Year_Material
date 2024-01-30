""""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi että
siitä on karsittu pois kaikki parittomat luvut. Kirjoita testausta varten pääohjelma, jossa luot listan,
kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.
"""

def get_even_numbers(numbers):
    for i in range(len(numbers)-1):
        if numbers[i] % 2 != 0:
            numbers.pop(i)
    return numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 1, 3, 5]
even_numbers = get_even_numbers(numbers)
print(f"Alkuperäiset luvut: {numbers}, parilliset luvut: {even_numbers}")
