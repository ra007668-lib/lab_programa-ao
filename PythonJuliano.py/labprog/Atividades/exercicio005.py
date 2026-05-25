print("Combinaçoes para pintura")
tintas = ['oleo', 'latex', 'acrilica']
pinceis = ['rolo', 'cerda' , 'esponja']
solventes = ['agua', ' aguarras',' thinner']
contador = 0

for t in tintas: 
    for p in pinceis:
        for s in solventes:
            if (not(t == 'oleo' and s == "agua")) and \
                 (p == "rolo" or t != " latex"):
                print(f"Projeto: {t}, {p}e {s}")
                contador+=1
print(f"Foram definidas {contador} combinaçoes.")


