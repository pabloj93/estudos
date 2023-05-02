#classe extrato que acumula e imprime movimentações da conta
class Extrato:
    def __init__(self):
        self.transacoes = []

    def extratocompleto(self, numeroconta):
        print(f"Extrato: {numeroconta} \n")
        for p in self.transacoes:
            print(f"{p[0]} {p[1]: 10.2f} - {p[2]} {p[3].strftime('%d/%m/%y  %I:%M')}")
