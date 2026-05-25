valor = int(input("Digite o valor em centavos: "))
print(f"Para valor {valor} centavos, a menor quantidade de moedas e: ")

moedas1real = valor // 100 
valor = valor % 100

moedas50 = valor // 50
valor = valor % 50

moedas25 = valor // 25
valor = valor % 25

moedas10 = valor // 10
valor = valor % 10

moedas5 = valor // 5
valor = valor % 5

moedas1 = valor 

if moedas1real > 0:
    print(f" -  {moedas1real} moedas(s) de 1 real")
if moedas50 > 0:
    print(f" _ {moedas50} moeda(s) de 50 centavos")
if moedas25 > 0: 
    print(f" - {moedas25} moeda(s) de 25 centavos")
if moedas10 > 0:
    print(f" - {moedas10} moedas(s) de 10 centavos")
if moedas5 > 0:
    print(f" - {moedas5} moedas(s) de 5 centavos")
if moedas1 > 0:
    print(f" - {moedas1} moedas(s) de 1 centavos")