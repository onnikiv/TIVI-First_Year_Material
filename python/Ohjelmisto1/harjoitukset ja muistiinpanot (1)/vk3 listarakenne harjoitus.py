# luvut = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
#
# parittomat_luvut = []
#
# for luku in luvut:
#     if luku % 2 != 0:
#         parittomat_luvut.append(luku)
# print(f'Parittomat luvut: {parittomat_luvut}')

# todennakoisyys = [0.52, 0.49, 0.72, 0.81, 0.12, 0.11]
# tyhlist = []
# for x in todennakoisyys:
#     if x > 0.5:
#         tyhlist.append(1)
#     if x < 0.5:
#         tyhlist.append(0)
# print(tyhlist)


tyhlista = []
prob = [0.52, 0.49, 0.72, 0.81, 0.12, 0.11]
pituus = len(prob)

print(pituus)

nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]
#remove, pop

nimet.pop(3)
print(nimet)

nimet.remove("Ahmed")
print(nimet)