# # myrange = range(1, 10, 2) # hyppää aina kaksi lukua
# #
# # print(list(myrange))
# #
# # for number in myrange:
# #     print(number)
# tyhlist = []
# luvut = range(0, 100, 11)
# for luku in luvut:
#     tyhlist.append(luku)
#
# tyhlist.pop(0)
# print(tyhlist)
#
# for luku in range(6):
#     print("Moi")
#
#
tyhlist = []
myrange = range(5,95,5)
for luku in myrange:
    tyhlist.append(luku)

print(tyhlist[::-1])
