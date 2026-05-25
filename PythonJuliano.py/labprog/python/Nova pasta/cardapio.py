print("Opçoes de marmitas")
proteina =["peixes","Ovo","Frango"]
carboitrados = ["Batata doce","Arroz","Quinosa"]
saladas = ["Espinafre","Alface","Brocolis"]

for pr in proteina:
    for cb in carboitrados:
        for sl in saladas:

            if (not (pr ==  "peixes" and cb == "batata doce")) and \
                  (( sl == " espinafre" ) == ( pr == "Ovo")) and \
                  (pr != cb and cb != sl and pr != sl):
                
                    print( f" Marmita :{pr} + {cb} + {sl}")


#if (a != b) and (b != c ) and (c != a):
#    if (dia =="quarta") or (estudante == "sim") or (Idade == 12):
#        if (bom == "digital") == (eletro == "senha") and (not acess == "B1"):
#            if not(fruta == "melancia" and bebida == "leite") or (valor > 10):