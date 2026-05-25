import random
num = int(input("Digite um numero entre 1 a 10: "))
soma = 0
numero_sorteado= random.randint(1,10)
print(numero_sorteado)
while num != numero_sorteado:
    soma = soma + numero_sorteado
    numero_sorteado = random.randint(1,10)
    print(numero_sorteado)
print("A soma é ",soma)