n = int(input("Quantos valores voce deseja inserir: "))
soma_quadrados = 0
for i in range(1, n+1):
    valor = float (input(f"Digite o {i} valor: "))
    soma_quadrados += valor** 2

print(f"\nA soma dos quadrados dos {n} valores é: {soma_quadrados:.2f}")