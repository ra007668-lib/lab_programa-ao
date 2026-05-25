lista = [1,2,10,5,20]
i, e = 0 , 10
# while i < len(lista) and lista[i] != e:
#     i += 1
# if i == len(lista):
#     i = -1



if e in lista:
    i = lista.index(e)
else:
 i = -1

print(i)