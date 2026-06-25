def calcula_media(v):
    soma = 0
    for e in v:
        soma+=e
    media = soma/len(v)
    return media
a = [1,2,3,4,5]
print(calcula_media(a))
b = [10,20,30,40,50]
print(calcula_media(b))