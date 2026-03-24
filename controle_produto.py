from datetime import datetime #estou mexendo com datas

class Produto:

    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_validade, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = datetime.strptime(data_compra, "%d/%m/%Y")
        self.data_validade = datetime.strptime(data_validade, "%d/%m/%Y")
        self.quantidade = quantidade

    def esta_vencido(self):
        return datetime.now() > self.data_validade

    def __str__(self):
        status = "VENCIDO" if self.esta_vencido() else "OK"
        return f"{self.nome} | Preço: R${self.preco_venda} | Qtde: {self.quantidade} | Validade: {self.data_validade.strftime('%d/%m/%Y')} | {status}"