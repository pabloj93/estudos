from ContaPoupanca import ContaPoupanca
from Conta import Conta
import datetime

class PoupancaRemunerada(ContaPoupanca, Conta):
    def __init__(self, numero, cpf, nomeTitular, saldo, clientes, IOF, IR, taxarendimento):
        Conta.__init__(self, numero, cpf, nomeTitular, saldo, clientes)
        ContaPoupanca.__init__(self, IOF, IR, taxarendimento)

    def CalculoRendimento(self, valor):
        valor = self.saldo*(self.taxarendimento/30) - self.saldo*self.IOF*self.IR
        self.saldo += self.saldo*(self.taxarendimento/30)
        self.saldo -= self.saldo*self.IOF
        self.extrato.transacoes.append(["RENDIMENTO APÓS IMPOSTOS", valor, "SALDO", self.saldo, "Data", datetime.datetime.today()])