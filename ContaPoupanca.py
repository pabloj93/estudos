from abc import ABC, abstractmethod
from Conta import Conta

class ContaPoupanca(ABC, Conta):
    def __init__(self, numero, cpf, nomeTitular, saldo, clientes, IOF, IR, taxarendimento):
        Conta.__init__(self, numero, cpf, nomeTitular, saldo, clientes)
        self.IOF = IOF
        self.IR = IR
        self.taxarendimento = taxarendimento

    @abstractmethod
    def CalculoRendimento(self):
        pass