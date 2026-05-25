frase= input("Digite uma frase : (ex: Aula 01 de SQL)")
conta_letras=0
conta_numeros=0
for caracter in frase:
    if caracter.isalpha():
        conta_letras += 1
    elif caracter.isdigit():
        conta_numeros += 1

print(f"na sua frase existem: {conta_letras} letras e {conta_numeros} numeros.")
