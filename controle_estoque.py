from produto import Produto

class Estoque: 
    #def = definir uma função
    #__init__ = função especial que roda quando o objeto é criado
    #self = o próprio objeto
    #quando eu criar um estoque, isso aqui vai acontecer automaticamente

    def __init__(self):
        self._produtos = []
#self = esse estoque
# _produtos = nome da lista, _ no produto significa que esta encapsulado
#[] = lista vazia
        
    def adicionar_produto(self, produto):
        self._produtos.append(produto)
#adicionar os produtos
#append para colocar os produtos dentro da lista

    def mostrar_produtos(self):
        for produto in self._produtos:
            print(produto)
    #mostrar tudo que tenho de produtos
    #

    def vender_produto(self, nome_produto):
#vender produto pelo nome dele

        for produto in self._produtos:
            if produto.nome == nome_produto:
                if produto.quantidade > 0:
                    produto.quantidade -= 1
                    print(f"Venda realizada: {produto.nome}")
                    return produto
                else:
                    print("Produto sem estoque!")
                    return None

        print("Produto não encontrado!")
        return None