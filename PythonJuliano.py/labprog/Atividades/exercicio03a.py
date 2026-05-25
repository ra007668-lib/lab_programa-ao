num = int(input("Digite o primeiro numero:  "))
num2 = int(input("Digite o segundo numero: "))
contador_pares = 0
soma = 0
while num <=num2:
    if(num%2 == 0):
     contadSr_pares += 1
     soma = soma + num
    num = num + 1
print(contador_pares)
print("A soma é ", soma)