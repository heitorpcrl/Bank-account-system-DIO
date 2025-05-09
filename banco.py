saldo = 1750.00
extrato = 0
qta_saque = 0
qta_deposito = 0
limite_saque_dias = 3
limite_saque_valor = 500
numero_saques = 0
numero_depositos = 0

def deposito():
    global numero_depositos, qta_deposito, saldo
    print("-----MENU DEPÓSITO-----")
    
    if qta_deposito >= 0:
        valor_deposito = int(input("Digite o valor a ser depositado: "))
        valor_deposito += qta_deposito
        numero_depositos += 1
        saldo -= valor_deposito
        print ("\nÊxito na operação !")
        print (f"Saldo final: R$ {saldo:.2f}")
    else:
        print("\nErro na operação, tente novamente.")


def saque():
    global numero_saques, saldo
    print("\n-----MENU SAQUE-----")
    
    if saldo <= 0:
        print("ERRO NA OPERAÇÃO: Saldo insuficiente.")
        return
        
    if limite_saque_dias <= 3 and limite_saque_valor <= 500:
        valor_saque = int(input("\nDigite o valor a ser sacado: "))
        
        if valor_saque > saldo:
            print("ERRO NA OPERAÇÃO: Saldo insuficiente para realizar o saque.")
            return
            
        if valor_saque > limite_saque_valor:
            print("ERRO NA OPERAÇÃO: Valor máximo de saque excedido.")
            return
            
        saldo += valor_saque
        numero_saques += 1
        print("\nÊxito na operação!")
        print(f"Saldo final: R$ {saldo}")
        
    elif limite_saque_dias > 3:
        print("ERRO NA OPERAÇÃO: Limite de saque diário excedido")
    elif limite_saque_valor > 500:
        print("ERRO NA OPERAÇÃO: Valor máximo de saque excedido.")
    else:
        print("ERRO NA OPERAÇÃO: Tente novamente.")
    
        
def extrato():
    global numero_depositos, numero_saques, saldo
    if numero_depositos == 0 and numero_saques == 0 :
        print ("ERRO NA OPERAÇÃO: Não foram realizadas movimentações.")
    else:
        print ("\n-----MENU EXTRATO-----")
        print (f"Número de saques realizados: {numero_saques}")
        print (f"Número de depósitos realizados: {numero_depositos} ")    
        print (f"Saldo final R$ {saldo:.2f}")
    
    
while True:
    print("\n---MENU PRINCIPAL---")
    print("""
          [1] - Depositar.
          [2] - Sacar.
          [3] - Imprimir extrato.
          [4] - Sair.
          """)
    escolha = int(input("Selecione uma opção: "))
    
    if escolha == 1:
        banco = deposito()
        
    elif escolha == 2:
        banco = saque()
        
    elif escolha == 3:
        banco = extrato()
        
    else:
        break
    