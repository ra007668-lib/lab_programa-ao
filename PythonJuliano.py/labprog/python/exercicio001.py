import itertools

print("Criando uma lista e fazendo sua exibiçao")
comidas = ["tomate","agriao","file de frango","pao de queijo","mel"]
print(f"lista de ingredientes disponiveis: {comidas}")

len(comidas)
print(f"Total: {len(comidas)}")
print(f'O ultimo elemento é: "{comidas[-1]}"')

print("Possiveis combinaçoês:")
# 1. Definir o grupo de elementos
grupo = ["tomate","agriao","file de frango","pao de queijo","mel"]

# 2. Gerar combinações de 3 elementos (r=3)
# Sem repetir elementos da mesma posição
combinacoes = list(itertools.combinations(grupo, 3))

# 3. Mostrar o resultado
for combo in combinacoes:
    print(combo)

# Saída:
# ('a', 'b', 'c')
# ('a', 'b', 'd')
# ('a', 'b', 'e')
# ('a', 'c', 'd')
# ...
