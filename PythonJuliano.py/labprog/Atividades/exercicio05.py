op = input(" Deseja somar (S) ou MultiplicaR (M)? ")
if (op == "S" or op == "M"):
    x = float(input("Digite o primeiro numero: "))
    y = float(input("Digite o segundo o numero: "))
    if (op == "S"):
        r = x + y
        print( "O resultado da soma é ", r)
    elif (op == 'M'):
        r = x * y
        print("O resulatdo da soma é ", r)
    else:
        print("Opção invalida!")  