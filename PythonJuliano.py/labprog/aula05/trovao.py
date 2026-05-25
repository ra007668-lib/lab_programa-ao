# 1 - definiçao da cosntante fisica (velocidade do som em m/s)

velocidade_som = 340

#leia tempo - tempo em segundos
tempo = float(input("digite o tempo entre o clarao e o trovao(em segundos): "))

#processamento
# distancia em metros = velocidade * tempo

distanciaMetros = velocidade_som * tempo # 2720 metros

# convertendo para quilometros
distanciaKm = distanciaMetros / 1000
# 4 - saida de dados
print(f" O raio caiu a uma distancia aproximada de {distanciaKm:.2f} km ")
