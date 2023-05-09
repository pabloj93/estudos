import datetime
from Extrato import Extrato
from Conta import Conta
from Clientes import Cliente
from ContaEspecial import ContaEspecial
from ContaPoupanca import ContaPoupanca
from PoupancaComum import PoupancaComum
from PoupancaRemunerada import PoupancaRemunerada

class Banco:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.contas = []

    def adicionaconta(self):
        numero = len(self.contas) + 1
        cpf = input("Digite o cpf do titular (com pontos e traço):\n")
        nomeTitular = input("Digite o nome do titular:\n")
        endereco = input("Digite o endereço do titular:\n")
        saldo = eval(input("Digite o saldo inicial da conta:\n"))
        clientes = Cliente(cpf, nomeTitular, endereco)

        print(f"Qual será o tipo de conta:\n"
              f"1 - Conta Corrente Comum\n"
              f"2 - Conta Corrente Especial\n"
              f"3 - Conta Poupança Comum\n"
              f"4 - Conta Poupança Especial\n")

        tipo = eval(input("Opção 1, 2, 3 ou 4?\n"))

        if tipo == 1:
            conta = Conta(numero, cpf, nomeTitular, saldo, clientes)
            self.contas.append(conta)
            print(f"Conta corrente comum número {numero} criada\n")

        elif tipo == 2:
            limite = eval(input("Digite o limite da conta:\n"))
            conta = ContaEspecial(numero, cpf, nomeTitular, saldo, clientes, limite)
            self.contas.append(conta)
            print(f"Conta corrente especial número {numero} criada\n")

        elif tipo == 3:
            IOF = eval(input("Digite a taxa de IOF que será aplicada:\n"))
            IR = eval(input("Digite a taxa de IR que será aplicada:\n"))
            taxarendimento = eval(input("Digite a taxa de rendimento que será aplicada:\n"))
            conta = PoupancaComum(numero, cpf, nomeTitular, saldo, clientes, IOF, IR, taxarendimento)
            self.contas.append(conta)
            print(f"Conta poupança comum número {numero} criada\n")

        elif tipo == 4:
            IOF = eval(input("Digite a taxa de IOF que será aplicada:\n"))
            IR = 0
            taxarendimento = eval(input("Digite a taxa de rendimento que será aplicada:\n"))
            conta = PoupancaRemunerada(numero, cpf, nomeTitular, saldo, clientes, IOF, IR, taxarendimento)
            self.contas.append(conta)
            print(f"Conta poupança remunerada número {numero} criada\n")

        self.menu()

    def depositar(self):
        numero = eval(input("Digite o número da conta em que irá depositar:\n"))
        for conta in self.contas:
            if numero == conta.numero:
                valor = eval(input("Digite o valor a ser depositado:\n"))
                conta.depositar(valor)
                print(f"Você depositou {valor} na conta {numero}\n")
            else:
                print("Conta não existe\n")
                self.depositar()

        self.menu()

    def saldo(self):
        numero = eval(input("Digite o número da conta que gostaria de ver o saldo:\n"))
        for conta in self.contas:
            if numero == conta.numero:
                conta.gerarSaldo()
            else:
                print("Conta não existe\n")
                self.saldo()

        self.menu()
    def menu(self):
        while True:
            menu = eval(input("O que gostaria de fazer:\n"
                              "1 - Adicionar Conta\n"
                              "2 - Depositar\n"
                              "3 - Saldo Simples\n"
                              "99 - Fechar Banco\n"))
            if menu == 1:
                self.adicionaconta()
            elif menu == 2:
                self.depositar()
            elif menu == 3:
                self.saldo()
            else:
                break




def abrirbanco():
    codigo = eval(input("Digite o código do banco:\n"))
    nome = input("Digite o nome do banco:\n")
    banco = Banco(codigo, nome)
    banco.menu()

abrirbanco()


### if __name__ == "__main__":
###    main()


