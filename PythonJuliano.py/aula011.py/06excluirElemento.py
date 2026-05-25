lista = [1,2,3,4]
pos = 2
# temp = []
# for i in range(len(lista)):
#     if i != pos:
#         temp.append(lista[i])
# lista = temp


del lista[pos]
e = lista.pop(2)
print(e)
print(lista)

