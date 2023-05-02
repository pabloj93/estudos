
#programa de estudo, classe simples
class Pessoa: #cria a classe Pessoa
    def __init__(self, nome, endereco): #inicia a classe e pega os valores dos atributos
        self.set_nome(nome)
        self.set_endereco(endereco)
#funções simples para atribuir e retornar os atributos
    def set_nome(self, nome):
        self.nome = nome

    def set_endereco(self, endereco):
        self.endereco = endereco

    def get_nome(self):
        return self.nome

    def get_endereco(self):
        return self.endereco


classe = input("Gostaria de usar a classe Pessoa? Sim ou Não")

if classe == "Sim":
    nome = input("Digite um nome:")

    endereco = input("Digite o endereço:")

    pessoa = Pessoa(nome, endereco)

    print(f'Nome: {pessoa.get_nome()}, Endereço: {pessoa.get_endereco()}')
else:
    print("Fim do Programa")

