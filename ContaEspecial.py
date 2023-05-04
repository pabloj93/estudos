from Conta import Conta
import datetime


class ContaEspecial(Conta):
    def __init__(self, numero, cpf, nomeTitular, saldo, clientes, limite):
        Conta.__init__(self, numero, cpf, nomeTitular, saldo, clientes)
        self.limite = limite


    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "SALDO", self.saldo, "Data", datetime.datetime.today()])
            return True