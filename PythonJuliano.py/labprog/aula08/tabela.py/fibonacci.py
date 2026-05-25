n_termos = int(input("Quantos termos da serie de fibonacci deseja ver: "))
a, b = 0, 1
contador = 0
print("Sequencia de Fibonacci")
while contador <= n_termos :
    print(a,end = ", " if contador < n_termos else "")
    # logica de altualizaçao F(n)= F( n-1) + F(n -2)
    proximo = a + b 
    a = b
    b = proximo
    contador +=1