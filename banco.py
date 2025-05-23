from datetime import datetime
from typing import List, Dict

class Usuario:
    def __init__(self, nome: str, data_nascimento: str, cpf: str, endereco: str):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__cpf = ''.join(filter(str.isdigit, cpf))
        self.__endereco = endereco

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def data_nascimento(self) -> str:
        return self.__data_nascimento

    @property
    def endereco(self) -> str:
        return self.__endereco

class Conta:
    def __init__(self, agencia: str, numero_conta: int, usuario: Usuario):
        self.__agencia = agencia
        self.__numero_conta = numero_conta
        self.__usuario = usuario
        self.__saldo = 0
        self.__extrato = 0
        self.__numero_saques = 0
        self.__limite_saque_dias = 3
        self.__limite_saque_valor = 500

    @property
    def agencia(self) -> str:
        return self.__agencia

    @property
    def numero_conta(self) -> int:
        return self.__numero_conta

    @property
    def usuario(self) -> Usuario:
        return self.__usuario

    @property
    def saldo(self) -> float:
        return self.__saldo

    @property
    def extrato(self) -> float:
        return self.__extrato

    def __validar_saque(self, valor: float) -> bool:
        if self.__saldo <= 0:
            print("ERRO NA OPERAÇÃO: Saldo insuficiente.")
            return False
            
        if self.__numero_saques >= self.__limite_saque_dias:
            print("ERRO NA OPERAÇÃO: Limite de saque diário excedido")
            return False
            
        if valor > self.__limite_saque_valor:
            print("ERRO NA OPERAÇÃO: Valor máximo de saque excedido.")
            return False
            
        if valor > self.__saldo:
            print("ERRO NA OPERAÇÃO: Saldo insuficiente para realizar o saque.")
            return False
        
        return True

    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self.__saldo += valor
            self.__extrato += valor
            print("\nÊxito na operação!")
            print(f"Saldo final: R$ {self.__saldo:.2f}")
            return True
        print("\nErro na operação: Valor inválido.")
        return False

    def sacar(self, valor: float) -> bool:
        print("\n-----MENU SAQUE-----")
        
        if not self.__validar_saque(valor):
            return False
                
        self.__saldo -= valor
        self.__extrato -= valor
        self.__numero_saques += 1
        print("\nÊxito na operação!")
        print(f"Saldo final: R$ {self.__saldo:.2f}")
        return True

    def exibir_extrato(self) -> None:
        print("\n-----MENU EXTRATO-----")
        print(f"Saldo atual: R$ {self.__saldo:.2f}")
        print(f"Valor em movimentações: R$ {self.__extrato:.2f}")
        
        if self.__extrato == 0:
            print("Não foram realizadas movimentações.")
        else:
            if self.__extrato > 0:
                print("Tipo de movimentação: Depósitos")
            else:
                print("Tipo de movimentação: Saques")

class Banco:
    def __init__(self):
        self.__agencia = "0001"
        self.__usuarios: List[Usuario] = []
        self.__contas: List[Conta] = []

    @property
    def agencia(self) -> str:
        return self.__agencia

    @property
    def usuarios(self) -> List[Usuario]:
        return self.__usuarios

    @property
    def contas(self) -> List[Conta]:
        return self.__contas

    def __validar_cpf_existente(self, cpf: str) -> bool:
        for usuario in self.__usuarios:
            if usuario.cpf == cpf:
                print("\nERRO: Já existe um usuário cadastrado com este CPF.")
                return False
        return True

    def __encontrar_usuario(self, cpf: str) -> Usuario:
        for usuario in self.__usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None

    def criar_usuario(self, nome: str, data_nascimento: str, cpf: str, endereco: str) -> bool:
        cpf_limpo = ''.join(filter(str.isdigit, cpf))
        
        if not self.__validar_cpf_existente(cpf_limpo):
            return False
        
        novo_usuario = Usuario(nome, data_nascimento, cpf_limpo, endereco)
        self.__usuarios.append(novo_usuario)
        
        print("\nUsuário criado com sucesso!")
        print(f"Total de usuários cadastrados: {len(self.__usuarios)}")
        return True

    def criar_conta_corrente(self, usuario: Usuario) -> bool:
        if not self.__usuarios:
            print("\nERRO: Não existem usuários cadastrados.")
            return False
            
        usuario_encontrado = self.__encontrar_usuario(usuario.cpf)
        
        if not usuario_encontrado:
            print("\nERRO: Usuário não encontrado.")
            return False
        
        numero_conta = len(self.__contas) + 1
        nova_conta = Conta(self.__agencia, numero_conta, usuario_encontrado)
        self.__contas.append(nova_conta)
        
        print("\nConta criada com sucesso!")
        print(f"Agência: {self.__agencia}")
        print(f"Número da conta: {numero_conta}")
        print(f"Titular: {usuario_encontrado.nome}")
        return True

def main():
    banco = Banco()
    
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
            if not banco.contas:
                print("\nERRO: Não existem contas cadastradas.")
                continue
                
            print("\nContas disponíveis:")
            for i, conta in enumerate(banco.contas, 1):
                print(f"{i} - Conta {conta.numero_conta} - {conta.usuario.nome}")
                
            try:
                indice = int(input("\nDigite o número da conta: ")) - 1
                if 0 <= indice < len(banco.contas):
                    valor = float(input("Digite o valor a ser depositado: "))
                    banco.contas[indice].depositar(valor)
                else:
                    print("\nERRO: Conta não encontrada.")
            except ValueError:
                print("\nERRO: Entrada inválida.")
            
        elif escolha == 2:
            if not banco.contas:
                print("\nERRO: Não existem contas cadastradas.")
                continue
                
            print("\nContas disponíveis:")
            for i, conta in enumerate(banco.contas, 1):
                print(f"{i} - Conta {conta.numero_conta} - {conta.usuario.nome}")
                
            try:
                indice = int(input("\nDigite o número da conta: ")) - 1
                if 0 <= indice < len(banco.contas):
                    valor = float(input("Digite o valor a ser sacado: "))
                    banco.contas[indice].sacar(valor)
                else:
                    print("\nERRO: Conta não encontrada.")
            except ValueError:
                print("\nERRO: Entrada inválida.")
            
        elif escolha == 3:
            if not banco.contas:
                print("\nERRO: Não existem contas cadastradas.")
                continue
                
            print("\nContas disponíveis:")
            for i, conta in enumerate(banco.contas, 1):
                print(f"{i} - Conta {conta.numero_conta} - {conta.usuario.nome}")
                
            try:
                indice = int(input("\nDigite o número da conta: ")) - 1
                if 0 <= indice < len(banco.contas):
                    banco.contas[indice].exibir_extrato()
                else:
                    print("\nERRO: Conta não encontrada.")
            except ValueError:
                print("\nERRO: Entrada inválida.")
            
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
            banco.criar_usuario(nome, data_nascimento, cpf, endereco)
            
        elif escolha == 5:
            if not banco.usuarios:
                print("\nERRO: Não existem usuários cadastrados.")
                continue
                
            print("\nUsuários cadastrados:")
            for i, usuario in enumerate(banco.usuarios, 1):
                print(f"{i} - {usuario.nome} (CPF: {usuario.cpf})")
                
            try:
                indice = int(input("\nDigite o número do usuário para criar a conta: ")) - 1
                if 0 <= indice < len(banco.usuarios):
                    banco.criar_conta_corrente(banco.usuarios[indice])
                else:
                    print("\nERRO: Usuário não encontrado.")
            except ValueError:
                print("\nERRO: Entrada inválida.")
            
        else:
            break

if __name__ == "__main__":
    main()
    