nome1 = input("Nome  aluno 1: ")
nome2 = input("Nome  aluno 2: ")
nome3 = input("Nome  aluno 3: ")

nota1 = float(input( f" Nota de {nome1}: "))
nota2 = float(input( f" Nota de {nome2}: "))
nota3 = float(input( f" Nota de {nome3}: "))

media = (nota1 + nota2 + nota3) / 3
print(f"A media de turma e´{media:.2f}")
if nota1 > media:
    print(f"Parabens {nome1}, sua troca {nota1}")
if nota2 > media: 
    print(f"Parabens {nome2}, sua troca {nota2}")
if nota2 > media: 
    print(f"Parabens {nome3}, sua troca {nota3}")