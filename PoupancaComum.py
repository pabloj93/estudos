from ContaPoupanca import ContaPoupanca
from Conta import Conta
import datetime

class PoupancaComum(ContaPoupanca, Conta):
    def __init__(self, numero, cpf, nomeTitular, saldo, clientes, IOF, IR, taxarendimento, dataabertura = datetime.datetime.today):
        Conta.__init__(self, numero, cpf, nomeTitular, saldo, clientes)
        ContaPoupanca.__init__(self, numero, cpf, nomeTitular, saldo, clientes, IOF, IR, taxarendimento, dataabertura)

    def CalculoRendimento(self):
        dias = abs((datetime.datetime.today - self.dataabertura).days)
        rendimento = self.saldo*(self.taxarendimento/30)*dias
        valor = self.saldo * (self.taxarendimento /30) - rendimento * self.IOF * self.IR
        self.saldo += rendimento
        self.saldo -= rendimento*self.IOF*self.IR
        self.extrato.transacoes.append(["RENDIMENTO APÓS IMPOSTOS", valor, "SALDO", self.saldo, "Data", datetime.datetime.today()])