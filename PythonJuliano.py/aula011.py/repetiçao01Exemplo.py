notas = [0] * 3  #[0,0,0]
soma = 0
for i in range(len(notas)):
    msg = f"{i+1} Nota do aluno: "
    notas[i] = float(input(msg))
    soma += notas[i] 

print(f"A media da turma é {soma/3}.")
