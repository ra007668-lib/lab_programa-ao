frase = input("Digite uma frase: ")+" "
palavra_atual = ""
lista_palavras = []

for caractere in frase:
    if caractere != " ":
        palavra_atual += caractere
    else:
        if palavra_atual != "":
            lista_palavras.append(palavra_atual)
            palavra_atual=""
print(F"Vetor de palvaras gerado: {lista_palavras}")