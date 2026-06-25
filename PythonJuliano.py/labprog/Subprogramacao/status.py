aluno = input("Digite o nome do aluno(a): ")

calcula_media = []
nota1 = int(input("Digite a nota: "))
nota2 = int(input("Digite a nota: "))
nota3 = int(input("Digite a nota: "))

notas = [nota1, nota2, nota3]


def calcula_media(v):
    soma = 0
    for e in v:
        soma+=e
    media = soma/len(v)
    return media
media_final = calcula_media(notas)




print(f"\nA média do(a) {aluno} é: {media_final:.2f}")

if media_final >= 6:
    print("aprovado")
elif media_final  >= 4: 
    print("verificaçao_suplementar")
else:
    print("reprovado")




#
