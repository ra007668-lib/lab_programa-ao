nome = input("Digte uma palavra: ")
# python
for caracter in nome:
    print(f"estou analizando a letra: {caracter}")

valor = 5
print(valor.isdigit())# resultado true
valor = "A"
print(valor.isdigit())# retorna falso
print(valor.isalpha())# retorna true