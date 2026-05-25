# leia Idade
PORCENTAGEM_AGUA = float(input("Informe o nivel atual do reservatorio (%): "))
# processamento
if PORCENTAGEM_AGUA >= 90:
 status = "ALERTA: Nivel Critico (Transbordamento)"
elif PORCENTAGEM_AGUA  >= 50:
  status ="Nivel Adequado."
elif PORCENTAGEM_AGUA >= 20:
 status = "Nivel Baixo (Atenção)"
else:
 status = "ALERTA: Reservatorio Vazio!"
print(f"SISTEMA: {status}")
