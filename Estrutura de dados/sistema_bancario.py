menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input (menu)

    if opcao == "1":
        valor = float(input("Informe o valor desejado para deposito:"))
    
        if valor > 0:
           saldo += valor
           extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou!Por favor insira um valor valido.")    

    elif opcao == "2":
        valor = float(input("Informe o valor desejado para saque:"))

        excede_saldo = valor>saldo

        excede_limite = valor>limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excede_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excede_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        
        elif excedeu_saques:
            print("Operação falhou! Você execedeu o limite diario de saques.")       
       
        elif valor > 0:
            saldo-= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"     
        else:
            print("Operação falhou!O valor informado é inválido.")    
    
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        print("Operação finalizada! Até logo!")
        break
        1

    else:
        print("Operação inválida, por favor seleciona novamente a operação desejada.")  