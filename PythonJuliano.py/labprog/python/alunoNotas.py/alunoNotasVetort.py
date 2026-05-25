qtde_alunos= 3
nomes = []
notas = []
media = 0
for i in range(qtde_alunos):
    nomes.append(input(F"Nome do aluno{i+1}: "))
    notas.append(float(input(f"Nota de {nomes[i]}: ")))
    media = media + notas [i]


media = media + notas / qtde_alunos
print(f"\nA media da turma e {media}: .2f \n")

print("Aluno com nota acima da medida: ")
for i in range(qtde_alunos):
    if notas[i > media:]:
        print(f"Parabens {nomes [1]}! Sua nota foi {notas[i]:.2f}")
print(nomes,notas)

