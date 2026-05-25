# leia Idade
IDADE =  int(input("Digite a Idade do atleta: "))
# processamento
if IDADE < 5:
 categoria = "sem categoria ( muito jovem)"
elif IDADE <=7:
 categoria ="Infatil A "
elif IDADE <= 11:
 categoria = "infantil B"
elif IDADE <= 17:
 categoria = "Juvenil"
else:
 categoria = "Adulto"

print(f"O atleta pertence a categoria: {categoria}")
