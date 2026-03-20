class Produto: #criar um dado novo, chama produto, esse dado vai ter nome, preco de compra, preco de venda, data de compra, data de validade e quantidade.
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_validade, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.data_validade = data_validade
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.nome} | Preço: R${self.preco_venda} | Quantidade: {self.quantidade} | Validade: {self.data_validade}"