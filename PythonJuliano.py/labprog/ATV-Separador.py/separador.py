int(input("Digite 10 numeros inteiros unicos: "))

pares=[]
impares=[]

while len(pares) + len(impares) < 10:
    num = int(input("Numero: "))
    if num in pares or num in impares:
        print("Esse numero ja foi digitado! Tente outro")
        continue
    if  num %2 ==0 :
        pares.append(num)

    else:
        impares.append(num) 

print(f"\nVetor  de pares:{pares}")
print(f"\nVetor de impares:{impares}")