print("Criando uma lista e fazendo sua exibiçao")
musicas = ["rock","pop","jazz","blues","rap"]
print(musicas)
len(musicas)
print(len(musicas))

tamanho_da_lista= len(musicas) 
print(tamanho_da_lista)
nova_musica = int("Digite a uma niova musica: ")
musicas.insert(6,(nova_musica))
print(f"lista de musica = {musicas}")