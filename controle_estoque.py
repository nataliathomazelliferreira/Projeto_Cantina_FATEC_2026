#questão 1
class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        self.__nome            = nome
        self.__preco_compra    = preco_compra
        self.__preco_venda     = preco_venda
        self.__data_compra     = data_compra
        self.__data_vencimento = data_vencimento
        self.__quantidade      = quantidade

    def get_nome(self):            return self.__nome
    def get_preco_compra(self):    return self.__preco_compra
    def get_preco_venda(self):     return self.__preco_venda
    def get_data_compra(self):     return self.__data_compra
    def get_data_vencimento(self): return self.__data_vencimento
    def get_quantidade(self):      return self.__quantidade

    def set_quantidade(self, nova):
        if nova < 0:
            raise ValueError("Quantidade não pode ser negativa.")
        self.__quantidade = nova

    def set_preco_venda(self, novo):
        if novo <= 0:
            raise ValueError("Preço de venda deve ser positivo.")
        self.__preco_venda = novo

    def __str__(self):
        return (f"Produto: {self.__nome:<30} | "
                f"Compra: R${self.__preco_compra:>5.2f} | "
                f"Venda: R${self.__preco_venda:>5.2f} | "
                f"Comprado em: {self.__data_compra} | "
                f"Vence em: {self.__data_vencimento} | "
                f"Qtd: {self.__quantidade}")


class _No:
    def __init__(self, produto):
        self.produto = produto
        self.proximo = None


class ListaEstoque:
    def __init__(self):
        self.__cabeca  = None
        self.__tamanho = 0

    def __converter_data(self, data_str):
        d, m, a = data_str.split("/")
        return (int(a), int(m), int(d))

    # 🔥 AGORA ORDENA POR DATA DE COMPRA (produto mais velho primeiro)
    def inserir_ordenado(self, produto):
        novo_no   = _No(produto)
        data_novo = self.__converter_data(produto.get_data_compra())

        if self.__cabeca is None:
            self.__cabeca = novo_no
            self.__tamanho += 1
            return

        if data_novo < self.__converter_data(self.__cabeca.produto.get_data_compra()):
            novo_no.proximo = self.__cabeca
            self.__cabeca   = novo_no
            self.__tamanho += 1
            return

        atual = self.__cabeca
        while atual.proximo is not None:
            if data_novo < self.__converter_data(atual.proximo.produto.get_data_compra()):
                novo_no.proximo = atual.proximo
                atual.proximo   = novo_no
                self.__tamanho += 1
                return
            atual = atual.proximo

        atual.proximo   = novo_no
        self.__tamanho += 1

    # 🔥 AGORA RETORNA O PRODUTO
    def buscar(self, nome):
        atual = self.__cabeca
        while atual is not None:
            if atual.produto.get_nome().lower() == nome.lower():
                return atual.produto
            atual = atual.proximo
        return None

    # ✔️ EDITAR QUANTIDADE (isso atende o requisito)
    def atualizar_quantidade(self, nome, nova_quantidade):
        produto = self.buscar(nome)
        if produto is not None:
            produto.set_quantidade(nova_quantidade)
            print(f"Quantidade de '{nome}' atualizada para {nova_quantidade}.")
        else:
            print(f"Produto '{nome}' nao encontrado no estoque.")

    # 🔥 VENDA CORRETA (PEGA O MAIS ANTIGO PRIMEIRO)
    def dar_baixa(self, nome, quantidade_vendida):
        atual = self.__cabeca

        while atual is not None:
            produto = atual.produto

            if produto.get_nome().lower() == nome.lower():
                if produto.get_quantidade() >= quantidade_vendida:
                    produto.set_quantidade(produto.get_quantidade() - quantidade_vendida)
                    print(f"Baixa de {quantidade_vendida} unidade(s) de '{nome}'. Restam: {produto.get_quantidade()}")
                    return True
                else:
                    print(f"Estoque insuficiente no lote mais antigo de '{nome}'.")
                    return False

            atual = atual.proximo

        print(f"Produto '{nome}' nao encontrado.")
        return False

    def get_tamanho(self):
        return self.__tamanho

    def calcular_valor_estoque(self):
        total_custo = 0.0
        total_venda = 0.0
        atual = self.__cabeca
        while atual:
            p = atual.produto
            total_custo += p.get_preco_compra() * p.get_quantidade()
            total_venda += p.get_preco_venda()  * p.get_quantidade()
            atual = atual.proximo
        return total_custo, total_venda

    def exibir(self):
        print("\nESTOQUE ATUAL (mais antigo primeiro):")
        print("-" * 90)
        if self.__cabeca is None:
            print("   Estoque vazio.")
        else:
            atual   = self.__cabeca
            posicao = 1
            while atual is not None:
                print(f"[{posicao:02d}] {atual.produto}")
                atual   = atual.proximo
                posicao += 1
        print("-" * 90)
        custo, venda = self.calcular_valor_estoque()
        print(f"Total de itens: {self.__tamanho} | "
              f"Valor custo: R${custo:.2f} | Valor venda: R${venda:.2f}")


if __name__ == "__main__":

    print("=" * 90)
    print("QUESTAO 1 - CONTROLE DE ESTOQUE")
    print("=" * 90)

    p1 = Produto("Agua", 2.50, 3.50, "10/03/2026", "25/03/2027", 20)
    p2 = Produto("Agua", 2.50, 3.50, "15/03/2026", "25/03/2027", 10)  # mais novo

    estoque = ListaEstoque()
    estoque.inserir_ordenado(p1)
    estoque.inserir_ordenado(p2)

    estoque.exibir()

    print("\nVenda de 5 Aguas (deve sair do mais antigo):")
    estoque.dar_baixa("Agua", 5)

    print("\nAtualizando quantidade:")
    estoque.atualizar_quantidade("Agua", 50)

    estoque.exibir()