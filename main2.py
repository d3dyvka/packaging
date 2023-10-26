f = open('god.txt', encoding='utf-8')
a = list()
for i in f:
    g = i.split(";")
    a.append({"id":int(g[0]), "name":g[1], "var":int(g[2]), "subgroup":int(g[3])})

first, _, _, fourth, *u, last = a
*gogo, = first, fourth, last
print(gogo)