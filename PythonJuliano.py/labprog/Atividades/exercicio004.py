print("Gerador de combinaçoes")
print("Digite os itens separados por vírgula para cada grupo.")

Frutas = []
Bebidas = []

for i in range (2):
    Frutas.append(input(f"Digite a {i+1}  fruta: "))
for i in range(2):
    Bebidas.append (input(f" Digite a {i+1} bebida: "))

print("-- Kits Alimenticios identificados -->")
for f in Frutas:
     for b in Bebidas:
         if not (f == "manga" and b == "leite"):
             print(f"combinaçao: {f} com {b}")
     else:
             print(f"Combinaço: {f} + {b}*** invalida***")

   