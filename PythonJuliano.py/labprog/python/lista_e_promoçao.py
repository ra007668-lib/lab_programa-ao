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




#------------



import itertools

# 1. Receber os dados do usuário para três grupos
print("PROMOÇAO NA LOJA")
print("Sempre que voce comprar a combinação de 3 grupos de produtos diferentes, Voce poderá receber um desconto 80% nos preço")
print("--- Gerador de Combinações ---")
print("Digite os itens separados por vírgula para cada grupo.")

print("Eletrodosmeticos")
input("Digite quantos produtos voçe vai levar: ")
grupo1 = input("Digite seus produtos: ").split(',')
print("Comidas")
input("Digite quantos produtos voçe vai levar: ")
grupo2 = input("Digite seus produtos: ").split(',')
print("Utilidades")
input("Digite quantos produtos voçe vai levar: ")
grupo3 = input("Digite seus produtos: ").split(',')


grupo1 = [item.strip() for item in grupo1]
grupo2 = [item.strip() for item in grupo2]
grupo3 = [item.strip() for item in grupo3]

combinacoes = list(itertools.product(grupo1, grupo2, grupo3))

print(f"\nTotal de combinações geradas: {len(combinacoes)}")
print("-" * 30)
for i, combo in enumerate(combinacoes, 1):
    print(f"{i}: {combo}")

