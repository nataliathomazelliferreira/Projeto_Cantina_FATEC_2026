class Produto: #criar um dado novo, chama produto, esse dado vai ter nome, preco de compra, preco de venda, data de compra, data de validade e quantidade.
    #def vou usar para definir uma funcao
    #def init estou criando uma funcao dentro dessa classe, quando alguem criar um produto vai executar isso automaticamente
    #def init 
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_validade, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.data_validade = data_validade
        self.quantidade = quantidade
#def str para definir como o objeto aparece quando eu uso print
    def __str__(self):
        return f"{self.nome} | Preço: R${self.preco_venda} | Quantidade: {self.quantidade} | Validade: {self.data_validade}"

# classe Produto: serve como um molde para criar produtos da cantina, e todo produto terá as mesmas características, que são os atributos.
# objeto: cada produto criado (ex: coca, água) é um objeto da classe Produto
# atributos: sao as características de cada produto: nome, preco, quantidade, validade