n= int(input("Digite um numero para verificar se e produto de 3 consecutivos"))
triangular =False
i = 1
# testamos enquanto o produto for menor oui igual a n
while i * (i+1)*(i+2) <= n:
    if i * (i+1)*(i+2) == n:
        print(f"sim! {n} e o produto de {i}x{i+1}x{i+2}")
        triangular = True
        break
    i +=1

if not triangular:
    print(f"O numero {n} Nao e produto de 3 inteiros consecutivos.")
