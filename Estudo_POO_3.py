from Conta import Conta
from Clientes import Cliente
from Extrato import Extrato
cliente1 = Cliente(123, "Joao", "Rua 1")
cliente2 = Cliente(345, "Maria","Rua 2")
conta1 = Conta(1, 123, 'Joao', 0, [cliente1,cliente2])
conta1.gerarExtrato()
conta1.depositar(1500)
conta1.sacar(500)
conta1.gerarExtrato()
print(conta1.clientes[1].endereco)
conta1.extrato.extratocompleto(conta1.numero)