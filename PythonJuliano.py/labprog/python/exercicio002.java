import itertools

# 1. Receber os dados do usuário para três grupos
print("PROMOÇAO NA LOJA")
print("Sempre que voce comprar a combinação de 3 grupos de produtos diferentes, Voce poderá receber um desconto 80% nos preço")
print("--- Gerador de Combinações ---")
print("Digite os itens separados por vírgula para cada grupo.")

# input().split(',') transforma a string entrada em uma lista
print("Eletrodosmeticos")
input("Digite quantos produtos voçe vai levar: ")
grupo1 = input("Digite seus produtos: ").split(',')
print("Comidas")
input("Digite quantos produtos voçe vai levar: ")
grupo2 = input("Digite seus produtos: ").split(',')
print("Utilidades")
input("Digite quantos produtos voçe vai levar: ")
grupo3 = input("Digite seus produtos: ").split(',')

# Remove espaços em branco extras que o usuário possa ter digitado
grupo1 = [item.strip() for item in grupo1]
grupo2 = [item.strip() for item in grupo2]
grupo3 = [item.strip() for item in grupo3]

# 2. Gerar as combinações (Produto Cartesiano)
# itertools.product pega um elemento de cada grupo e combina
combinacoes = list(itertools.product(grupo1, grupo2, grupo3))

# 3. Exibir os resultados
print(f"\nTotal de combinações geradas: {len(combinacoes)}")
print("-" * 30)
for i, combo in enumerate(combinacoes, 1):
    print(f"{i}: {combo}")