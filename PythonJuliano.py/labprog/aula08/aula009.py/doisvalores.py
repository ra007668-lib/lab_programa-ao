x = int(input("digite o dividendo (x) : "))
y = int(input("digite o divisor (y): "))
#guardar os valores originais
dividendo = x
divisor = y
quociente = 0


while x >= y :
    x -= y
    quociente += 1

resto = x
print("-"*40)
print(f"O resultado do {dividendo} / {divisor}: ")
print(f" Quociente (divisao interia): {quociente}")
print(f"")
