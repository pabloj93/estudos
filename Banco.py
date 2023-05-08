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
        print(f"Qual será o tipo de conta:\n"
              f"1 - Conta Corrente Comum\n"
              f"2 - Conta Corrente Especial\n"
              f"3 - Conta Poupança Comum\n"
              f"4 - Conta Poupança Especial\n")

        tipo = eval(input("Opção 1, 2, 3 ou 4?\n"))

        if tipo != 1:
            print("Ainda em construção\n")
            self.menu()

        else:

            numero = len(self.contas) + 1

            cpf = input("Digite o cpf do titular (com pontos e traço)\n")

            nomeTitular = input("Digite o nome do titular:\n")

            endereco = input("Digite o endereço do titular:\n")

            saldo = eval(input("Digite o saldo inicial da conta\n"))

            clientes = Cliente(cpf, nomeTitular, endereco)

            conta = Conta(numero, cpf, nomeTitular, saldo, clientes)

            self.contas.append(conta)

            print(f"Conta corrente comum número {numero} criada\n")

            self.menu()
    def menu(self):
        menu = eval(input("O que gostaria de fazer:\n"
                          "1 - Adicionar Conta\n"
                          "99 - Fechar Banco\n"))
        while menu != 99:

            if menu == 1:
                self.adicionaconta()
            elif menu == 99:
                menu = 99


def abrirbanco():
    codigo = eval(input("Digite o código do banco:\n"))
    nome = input("Digite o nome do banco:\n")
    banco = Banco(codigo, nome)
    banco.menu()

abrirbanco()





