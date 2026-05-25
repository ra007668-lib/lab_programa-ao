camisas=("Social","Verde","Regata")
calcas=("jeans","Azul","Bermuda")
calcados=("tenis","Sapato")

for c in camisas :
    for l in calcas :
        for s in calcados:
            if (not( c == "Verde" and l == "azul")) and (s == "tenis" or c != "Social"):
                print(f"{c} , {l} e {s}"  )
                  


