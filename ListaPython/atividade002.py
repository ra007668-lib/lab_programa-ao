#vetor1 = 2.5
#vetor2 = 7.5
#vetor3 = 10.0
#vetor4 = 4.0
#media = (vetor1 + vetor2  + vetor3 + vetor4 ) / 4
#print(f"A media dos vetores é: {media:.2f}")

#print(" O velor mais proximo da media é:")

vetor = [2.5, 7.5, 10.0, 4.0]
soma = 0
for valor in vetor:
    soma += valor
media = soma / len(vetor)

proximo_da_media = vetor[0]
menor_distancia =  abs(vetor[0] - media)
for valor in vetor:
    distancia_atual = abs(valor - media)
    if distancia_atual < menor_distancia:
        menor_distancia = distancia_atual
        proximo_da_media = valor


print(f"Vetor: {vetor}")
print(f"Media: {media:1f}")
print(f"Valor mais proximno da media: {proximo_da_media}")
