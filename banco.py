saldo = 0
extrato = 0
qta_saque = 0
qta_deposito = 0
limite_saque_dias = 3
limite_saque_valor = 500
numero_saques = 0
numero_depositos = 0

usuarios = []
contas = []
AGENCIA = "0001"

def criar_usuario(nome, data_nascimento, cpf, endereco):
    # Remove caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verifica se já existe usuário com este CPF
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("\nERRO: Já existe um usuário cadastrado com este CPF.")
            return False
    
    # Cria um novo dicionário com os dados do usuário
    novo_usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    
    # Adiciona o novo usuário à lista de usuários usando append
    usuarios.append(novo_usuario)
    
    print("\nUsuário criado com sucesso!")
    print(f"Total de usuários cadastrados: {len(usuarios)}")
    return True

def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += valor
        print("\nÊxito na operação!")
        print(f"Saldo final: R$ {saldo:.2f}")
        return saldo, extrato
    else:
        print("\nErro na operação: Valor inválido.")
        return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    print("\n-----MENU SAQUE-----")
    
    if saldo <= 0:
        print("ERRO NA OPERAÇÃO: Saldo insuficiente.")
        return saldo, extrato
        
    if numero_saques >= limite_saques:
        print("ERRO NA OPERAÇÃO: Limite de saque diário excedido")
        return saldo, extrato
        
    if valor > limite:
        print("ERRO NA OPERAÇÃO: Valor máximo de saque excedido.")
        return saldo, extrato
        
    if valor > saldo:
        print("ERRO NA OPERAÇÃO: Saldo insuficiente para realizar o saque.")
        return saldo, extrato
            
    saldo -= valor
    extrato -= valor
    numero_saques += 1
    print("\nÊxito na operação!")
    print(f"Saldo final: R$ {saldo:.2f}")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n-----MENU EXTRATO-----")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print(f"Valor em movimentações: R$ {extrato:.2f}")
    
    if extrato == 0:
        print("Não foram realizadas movimentações.")
    else:
        if extrato > 0:
            print("Tipo de movimentação: Depósitos")
        else:
            print("Tipo de movimentação: Saques")
    
    return saldo, extrato

def criar_conta_corrente(usuario):
    # Verifica se o usuário existe
    if not usuarios:
        print("\nERRO: Não existem usuários cadastrados.")
        return False
        
    # Verifica se o CPF do usuário existe na lista de usuários
    usuario_encontrado = None
    for user in usuarios:
        if user['cpf'] == usuario['cpf']:
            usuario_encontrado = user
            break
    
    if not usuario_encontrado:
        print("\nERRO: Usuário não encontrado.")
        return False
    
    # Gera o número da conta (sequencial)
    numero_conta = len(contas) + 1
    
    # Cria a nova conta
    nova_conta = {
        'agencia': AGENCIA,
        'numero_conta': numero_conta,
        'usuario': usuario_encontrado
    }
    
    # Adiciona a nova conta à lista de contas
    contas.append(nova_conta)
    
    print("\nConta criada com sucesso!")
    print(f"Agência: {AGENCIA}")
    print(f"Número da conta: {numero_conta}")
    print(f"Titular: {usuario_encontrado['nome']}")
    return True

while True:
    print("\n---MENU PRINCIPAL---")
    print("""
          [1] - Depositar.
          [2] - Sacar.
          [3] - Imprimir extrato.
          [4] - Criar usuário.
          [5] - Criar conta corrente.
          [6] - Sair.
          """)
    escolha = int(input("Selecione uma opção: "))
    
    if escolha == 1:
        valor = float(input("Digite o valor a ser depositado: "))
        saldo, extrato = deposito(saldo, valor, extrato)
        
    elif escolha == 2:
        valor = float(input("Digite o valor a ser sacado: "))
        saldo, extrato = saque(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite_saque_valor,
            numero_saques=numero_saques,
            limite_saques=limite_saque_dias
        )
        
    elif escolha == 3:
        saldo, extrato = exibir_extrato(saldo, extrato=extrato)
        
    elif escolha == 4:
        nome = input("Digite o nome completo: ")
        data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
        cpf = input("Digite o CPF: ")
        logradouro = input("Digite o logradouro: ")
        numero = input("Digite o número: ")
        bairro = input("Digite o bairro: ")
        cidade = input("Digite a cidade: ")
        estado = input("Digite a sigla do estado: ")
        
        endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"
        
        criar_usuario(nome, data_nascimento, cpf, endereco)
        
    elif escolha == 5:
        if not usuarios:
            print("\nERRO: Não existem usuários cadastrados.")
            continue
            
        print("\nUsuários cadastrados:")
        for i, usuario in enumerate(usuarios, 1):
            print(f"{i} - {usuario['nome']} (CPF: {usuario['cpf']})")
            
        try:
            indice = int(input("\nDigite o número do usuário para criar a conta: ")) - 1
            if 0 <= indice < len(usuarios):
                criar_conta_corrente(usuarios[indice])
            else:
                print("\nERRO: Usuário não encontrado.")
        except ValueError:
            print("\nERRO: Entrada inválida.")
        
    else:
        break
    