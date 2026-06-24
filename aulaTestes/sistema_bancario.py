def sacar(valor, saldo):
    if valor <= saldo and valor > 0:
        saldo = saldo - valor
        return saldo
    else:
        return "impossivel sacar esse valor!"
##valor_saque = int(input("Insira o valor que deseja sacar: "))
##saldo = int(1000)
##if valor_saque <= saldo:
##    print(f"Sacou R${valor_saque} do seu saldo de R${saldo}. Valor restante: R${sacar(valor_saque, saldo)}.")
##else:
##    print("Impossivel sacar esse valor")