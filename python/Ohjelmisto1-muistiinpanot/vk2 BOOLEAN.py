#BOOLEAN -->> true tai false shiz
#raha = 5
#ehto = raha > 2
#print(ehto)

#a = True
#b = True
#c = False
#d = False
#print(a and b)
a = False
b = False
c = True

d1 = (a and b) or c # sulut ensin
d2 = a and (b or c) #sulut ensin
d3 = a and b or c # and ensin sitten or
print(d1)
print(d2)
print(d3)