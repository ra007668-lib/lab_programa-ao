possibilidade = [True , False]

total_de_linhas = 0
total_T = 0
total_F = 0


qual_formula = input(f"Digite a formula (use p, q e r como variaveis:):").lower()


for P in possibilidade:
    for Q in possibilidade:
         for R in possibilidade:
            if  (P or Q ) and R:
                res_f = "verdeiro"
                total_T += 1
            else:
                res_f = "Falso"
                total_F += 1
            print( f" P = {P} \t Q = {Q} \t R = {R} \t Formula = {res_f}")
            total_de_linhas += 1
if (total_de_linhas == total_T):
    prporiedades_semantica = "TAUTOLOGIA"
elif (total_de_linhas == total_F):
    prporiedades_semantica = "CONTRADITORIA"
else:
    prporiedades_semantica = "SATISFATORIA"

# 

print(f"Total de linhas {total_de_linhas}")
print(f"Total de linhas com resultado true : \033[1m {total_T} \033[0m")
print(f"Total de linhas com resultado true :{total_F}")
print(f"Esta Formula e {prporiedades_semantica}")