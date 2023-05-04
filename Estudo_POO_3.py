from Conta import Conta
from Clientes import Cliente
from ContaEspecial import ContaEspecial
from Extrato import Extrato
cliente1 = Cliente(123, "Joao", "Rua 1")
cliente2 = Cliente(345, "Maria","Rua 2")
conta1 = Conta(1, 123, 'Joao', 0, [cliente1,cliente2])
conta1.gerarSaldo()
conta1.depositar(1500)
conta1.sacar(500)
conta1.gerarSaldo()
print(conta1.clientes[1].endereco)
conta1.extrato.extratocompleto(conta1.numero)
cliente1 = Cliente("123","Joao","Rua X")
cliente2 = Cliente("456","Maria","Rua W")
cliente3 = Cliente("789","Joana", "Rua H")
conta1 = Conta(1,123, "Joao", 2000, [cliente1,cliente2])
conta2 = ContaEspecial(3,789, "Joana", 1000, [cliente3],2000)
conta2.depositar(100)
conta2.sacar(2000)
conta2.extrato.extratocompleto(conta2.numero)


