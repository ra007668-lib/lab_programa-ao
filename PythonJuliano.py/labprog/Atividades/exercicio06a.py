n_desejado =int(input("Quantos numeros perfeitos voce encontar: "))
encontrados = 0
numero_testado = 2 #começamos dop 2 (1 nao e perfeito)
print(f"Buscando os {n_desejado} primerios numeros perfeitos")
while encontrados < n_desejado:
    soma_divisores = 0
    # encontra os divisores do "numero_testado"
    for i in range(1, numero_testado):
        if numero_testado % i == 0 :
            soma_divisores += i


    #verificar se a soma é igual ao numero
    if soma_divisores == numero_testado:
        encontrados +=1
        print(f"{encontrados}. numero perfeito encontrado:{numero_testado}")          
    numero_testado += 1


