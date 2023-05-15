from abc import ABC, abstractmethod
from Conta import Conta
import datetime
class ContaPoupanca(ABC, Conta):
    def __init__(self, numero, cpf, nomeTitular, saldo, clientes, IOF, IR, taxarendimento, dataabertura = datetime.datetime.today):
        Conta.__init__(self, numero, cpf, nomeTitular, saldo, clientes)
        self.IOF = IOF
        self.IR = IR
        self.taxarendimento = taxarendimento
        self.dataabertura = dataabertura

    @abstractmethod
    def CalculoRendimento(self):
        pass