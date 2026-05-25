possibilidade = [True , False]

total_de_linhas = 0
total_T = 0
total_F = 0

num = int(input("Quantas variavies voce deseja utilizar? : "))
qual_formula = input (f"Digite  formula (use a, b e c como variaveis:): ").lower()

if num== 2:
        vars = ['p', 'q']
elif num == 3:
        vars = ['p', 'q', 'r']
else:
    print("Número inválido. Escolha 2 ou 3.")
   
if num == 3:
    for p in possibilidade:
        for q in possibilidade:
            for r in possibilidade:
                if eval(qual_formula):
                    res_f = "verdeiro"
                    total_T += 1
                else:
                 res_f = "Falso"
                total_F += 1
                print( f" P = {p} \t Q = {q} \t R = {r} \t Formula = {res_f}")
            total_de_linhas += 1
    if (total_de_linhas == total_T):
            prporiedades_semantica = "TAUTOLOGIA"
    elif (total_de_linhas == total_F):
        prporiedades_semantica = "CONTRADITORIA"
    else:
        prporiedades_semantica = "SATISFATORIA"

else:
    for p in possibilidade:
        for q in possibilidade:
            if eval(qual_formula):
                    res_f = "verdeiro"
                    total_T += 1
            else:
                res_f = "Falso"
                total_F += 1
            print( f" P = {p} \t Q = {q}  \t Formula = {res_f}")
            total_de_linhas += 1
    if (total_de_linhas == total_T):
            prporiedades_semantica = "TAUTOLOGIA"
    elif (total_de_linhas == total_F):
        prporiedades_semantica = "CONTRADITORIA"
    else:
        prporiedades_semantica = "SATISFATORIA"    







print(f"Total de linhas {total_de_linhas}")
print(f"Total de linhas com resultado true : {total_T}")
print(f"Total de linhas com resultado false : {total_F} ")
print(f"Esta Formula e {prporiedades_semantica}")