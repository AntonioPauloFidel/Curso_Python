menu="[d]Depositar", "[s]Sacar" ,"[e]Extrato" ,"[q]Sair"

saldo=0
limite_saque=3
quantidade_saque=0
extrato=""
limite=500
while True:
    print(menu)
    opcao=input("Digite a opçao desejada")
    if opcao=='q':
        break
    elif opcao=='e':
        print(saldo)
    elif opcao=='d':
        deposito=float(input("Digete o valor a ser depositador"))
        saldo+=deposito
    elif opcao=='s':
        if quantidade_saque>=limite_saque:
            print("Voce ja realizou todos os saques posiveis")
        else:
            valor=float(input("Qual valor deseja sacar"))
            if valor>saldo+limite:
                print("valor de saque indisponivel")
            else:
                print(f"Voce sacou:{valor}")
                saldo-=valor
