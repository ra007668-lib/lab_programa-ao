import itertools

print("Criando uma lista e fazendo sua exibiçao")
comidas = ["tomate","agriao","file de frango","pao de queijo","mel"]
print(f"lista de ingredientes disponiveis: {comidas}")

len(comidas)
print(f"Total: {len(comidas)}")
contador=0
for a in comidas:
    for b in comidas:
        for c in comidas:
            if(a !=b) and (b!= c) and (a != c):

                print(f"{a} com {b} e {c}"  )
                contador+=1
print("Foram um total de {contador} combinaçoes,")




