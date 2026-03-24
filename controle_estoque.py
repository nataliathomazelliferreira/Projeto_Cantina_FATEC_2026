from controle_produto import Produto

class Estoque:

    def __init__(self):
        self._produtos = []

    def adicionar_produto(self, produto):
        self._produtos.append(produto)

    def mostrar_produtos(self):
        for produto in self._produtos:
            print(produto)

    def vender_produto(self, nome_produto):

        for produto in self._produtos:

            if produto.nome == nome_produto:

                if produto.esta_vencido():
                    print("Produto vencido! Não pode vender.")
                    return None

                if produto.quantidade > 0:
                    produto.quantidade -= 1
                    print(f"Venda realizada: {produto.nome}")
                    return produto
                else:
                    print("Produto sem estoque!")
                    return None

        print("Produto não encontrado!")
        return None