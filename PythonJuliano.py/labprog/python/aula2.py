print("Criando uma lista e fazendo sua exibiçao")
comidas = ["pizza","churrasco","sorvete","bacon"]
print(comidas)

len(comidas)
print(len(comidas))

tamanho_da_lista= len(comidas) 
print(tamanho_da_lista)
texto="obabaotudobao"
print(f"O tamanho de {texto} é {len(texto)} ")

print(comidas[0])
print(comidas[2])
print(comidas[3])
print(f'O ultimo elemento e"{comidas[-1]}"')
print(f"O ultimo elemento e'{comidas[-1]}'")

range(10)
list(range(10))
print(list(range(10)))

print(list(range(2,10)))
print(list(range(20,30)))
print(list(range(20,30,2)))

print(f"Comidas = {comidas}")
comidas.reverse()
print(f"Comidas = {comidas}")

comidas.insert(0,"feijoada")
print(f"Comidas = {comidas}")