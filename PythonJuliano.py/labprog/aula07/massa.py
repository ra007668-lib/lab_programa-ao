# 1. Entrada de dados
print("--- CALCULADORA DE IMC ---")
massa = float(input("informe o peso (kg): "))
altura = float(input("informe a altura (m):  "))

# 2. Processamento : IMC = massa / altura^2
# em Pythoon, a potencia e feita com **

imc = massa / (altura ** 2)

# 3. Classificaçao (Logica IF-ELIF-ElSE)
if imc < 18.5:
    classificaçao = "abaixo do peso"
elif imc <= 24.9:
    classificaçao = "saudavel"
elif imc <= 29.9:
    classificaçao = "peso em excesso"
elif imc <= 34.9: 
    classificaçao = "Obseidade Grau 1"
elif imc <= 39.9:
    classificaçao = "Obesidade Grau 2 (severa)"
else:
    calssificaçao = "Obesidade Grau 3 (morbida)"

#4. Saida de dados.
print("-" * 30)
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificaçao: {calssificaçao}")


