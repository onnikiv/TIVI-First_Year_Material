tuuma_str = float(input("Anna mitta tuumana \n"))
cm = 2.54 * tuuma_str
print(f"senttimetreinä: {cm}")

# desimaaleja kaksi piissä
import math
munpi = math.pi
print(f"{munpi:.2f}") # .2f kertoo kuinka monta desimaalia printataan
print(f"{munpi:10.5f}") # 10 kertoo kuinka suureen kenttään se printtaa komennon
print(f"{munpi:20.5f}")
print(f"{munpi:30.2f}")
print(f"{munpi:>50.2f}")
print(f"{munpi:<50.2f}")
