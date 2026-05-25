num = int(input("Digite um numero : "))
contador = 0
if num == 0:
    contador = 1
else:
    temp = num
    while temp > 0:
        temp = temp // 10 # remove o ultimo digito
        contador += 1

print(f" O numero {num} possui {contador} digitos.")