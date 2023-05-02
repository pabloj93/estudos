import datetime
from Extrato import Extrato

class Conta:
    #inicia a classe conta com seus atributos
    def __init__(self, numero,cpf, nomeTitular, saldo, clientes ):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
        self.clientes = clientes
        self.dataabertura = datetime.datetime.today()
        self.extrato = Extrato()
    #método depositar, adiciona saldo na conta
    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["DEPOSITO", valor, "Data", datetime.datetime.today()])
    #método sacar, subtrai saldo na conta
    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
            return True
    #método gerar extrato, apresenta o saldo da conta
    def gerarExtrato(self):
        print(f"numero: {self.numero}\ncpf:{self.cpf}\nsaldo:{self.saldo}")
    #método de transferencia de saldo
    def transfereValor(self, contaDestino, valor):
        if self.saldo<valor:
            return("Não existe saldo suficiente")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", datetime.datetime.today()])
            return("Transferência realizada")