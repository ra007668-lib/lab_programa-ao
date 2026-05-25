while True:
    num=int(input("\nDigite um numero inteiro positivo: "))
    # conta divisores
    qtde_divisores = 0
    print(f"Divisores de {num}: ",end= "")
    # loop para encontrar e exibir os divisores
    for i in range (1, num+1):
        if num%i==0:
            print(i, end=" ")
            qtde_divisores += 1

    # verificar se o numero e primo baseado na qtde
    print()
    if qtde_divisores == 2:
        print(f"Conclusao : O numero {num} e primo")
    else:
        print(f"Conclusao: O numero {num} NAO e primo (possui{qtde_divisores} divisores)")

    continuar=input("\nDeseja analisar outro numero?(S/N): "). upper()
    if continuar != "S":
        break
