#importando a classe conta e usando seus métodos
from Conta import Conta

conta1 = Conta(1, 123, 'Joao',0)
conta2 = Conta(3, 456, 'Maria',0)

if (conta1 != conta2):
    print("Endereços diferentes de memória")

conta1.depositar(1000)
conta1.transfereValor(conta2,500)
print(conta1.saldo)
print(conta2.saldo)
