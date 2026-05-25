investimento_mensal= float(input("Quanto sera investimento por mes? R$"))
taxa_juros_mensal= float(input(" juros mensal (1 para 1%)?"))/100
saldo = 0 
ano_atual = 1 
while True:
    fon mes in range (1,13):
    saldo += investimento_mensal
    saldo += saldo*taxa_juros_mensal
print(f"\nsaldo do investimento apos {ano_atual} ano(s) : R$ {saldo:.2F}")
opçao=input("Deseja processar mais 1 ano/(S/N): ").upper()
if opçao == "S": 
    ano_atual +=1 
else:
    print("Simlaçao encerrada")
    break