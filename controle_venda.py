#questão 3 
from datetime import datetime


class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        self.__nome = nome
        self.__preco_compra = preco_compra
        self.__preco_venda = preco_venda
        self.__data_compra = data_compra
        self.__data_vencimento = data_vencimento
        self.__quantidade = quantidade

    def get_nome(self): return self.__nome
    def get_preco_compra(self): return self.__preco_compra
    def get_preco_venda(self): return self.__preco_venda
    def get_quantidade(self): return self.__quantidade

    def set_quantidade(self, nova):
        if nova < 0:
            raise ValueError("Quantidade nao pode ser negativa.")
        self.__quantidade = nova

    def __str__(self):
        return f"{self.__nome} | Venda: R${self.__preco_venda:.2f} | Qtd: {self.__quantidade}"


class _NoProduto:
    def __init__(self, produto):
        self.produto = produto
        self.proximo = None


class Estoque:
    def __init__(self):
        self.__cabeca = None
        self.__tamanho = 0

    def adicionar(self, produto):
        novo_no = _NoProduto(produto)
        if self.__cabeca is None:
            self.__cabeca = novo_no
        else:
            atual = self.__cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no
        self.__tamanho += 1

    def buscar(self, nome):
        atual = self.__cabeca
        while atual:
            if atual.produto.get_nome().lower() == nome.lower():
                return atual.produto
            atual = atual.proximo
        return None

    def dar_baixa(self, nome, qtd):
        atual = self.__cabeca
        anterior = None

        while atual:
            produto = atual.produto
            if produto.get_nome().lower() == nome.lower():
                if produto.get_quantidade() >= qtd:
                    nova_qtd = produto.get_quantidade() - qtd
                    produto.set_quantidade(nova_qtd)

                    if nova_qtd == 0:
                        if anterior is None:
                            self.__cabeca = atual.proximo
                        else:
                            anterior.proximo = atual.proximo
                        self.__tamanho -= 1

                    return True, "OK"
                else:
                    return False, f"Estoque insuficiente (disponivel: {produto.get_quantidade()})"
            anterior = atual
            atual = atual.proximo

        return False, "Produto nao encontrado"

    def exibir(self):
        print("\nEstoque atual:")
        atual = self.__cabeca
        while atual:
            print(f"   {atual.produto}")
            atual = atual.proximo


class Pessoa:
    def __init__(self, nome, categoria, curso):
        self.__nome = nome
        self.__categoria = categoria
        self.__curso = curso

    def get_nome(self): return self.__nome
    def get_categoria(self): return self.__categoria
    def get_curso(self): return self.__curso

    def __str__(self):
        return f"{self.__nome} ({self.__categoria} - {self.__curso})"


class _NoFila:
    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.proximo = None


class FilaAtendimento:
    def __init__(self):
        self.__frente = None
        self.__fundo = None
        self.__tamanho = 0

    def enfileirar(self, pessoa):
        novo_no = _NoFila(pessoa)
        if self.__fundo is None:
            self.__frente = novo_no
            self.__fundo = novo_no
        else:
            self.__fundo.proximo = novo_no
            self.__fundo = novo_no
        self.__tamanho += 1

    def desenfileirar(self):
        if self.__frente is None:
            return None
        pessoa = self.__frente.pessoa
        self.__frente = self.__frente.proximo
        if self.__frente is None:
            self.__fundo = None
        self.__tamanho -= 1
        return pessoa

    def get_tamanho(self): return self.__tamanho

    def exibir(self):
        print(f"\nFila de atendimento ({self.__tamanho} pessoa(s)):")
        atual = self.__frente
        pos = 1
        while atual:
            print(f"   [{pos}] {atual.pessoa}")
            atual = atual.proximo
            pos += 1


class ItemVenda:
    def __init__(self, produto_nome, quantidade, preco_unitario):
        self.__produto_nome = produto_nome
        self.__quantidade = quantidade
        self.__preco_unitario = preco_unitario

    def get_produto_nome(self): return self.__produto_nome
    def get_quantidade(self): return self.__quantidade
    def get_preco_unitario(self): return self.__preco_unitario

    def get_subtotal(self):
        return self.__quantidade * self.__preco_unitario

    def __str__(self):
        return f"{self.__produto_nome} x{self.__quantidade} = R${self.get_subtotal():.2f}"


class _NoItem:
    def __init__(self, item):
        self.item = item
        self.proximo = None


class Venda:
    __contador = 0

    def __init__(self, pessoa):
        Venda.__contador += 1
        self.__id = Venda.__contador
        self.__pessoa = pessoa
        self.__data_hora = datetime.now()
        self.__cabeca_itens = None
        self.__total = 0.0

    def get_id(self): return self.__id
    def get_total(self): return self.__total
    def get_pessoa(self): return self.__pessoa

    def adicionar_item(self, item):
        novo = _NoItem(item)
        if self.__cabeca_itens is None:
            self.__cabeca_itens = novo
        else:
            atual = self.__cabeca_itens
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo
        self.__total += item.get_subtotal()

    def tem_itens(self):
        return self.__cabeca_itens is not None

    def iterar_itens(self):
        atual = self.__cabeca_itens
        while atual:
            yield atual.item
            atual = atual.proximo

    def exibir(self):
        print(f"\nVENDA #{self.__id}")
        print(f"   Cliente  : {self.__pessoa}")
        print(f"   Data/hora: {self.__data_hora.strftime('%d/%m/%Y %H:%M:%S')}")
        atual = self.__cabeca_itens
        while atual:
            print(f"   {atual.item}")
            atual = atual.proximo
        print(f"   TOTAL    : R${self.__total:.2f}")


class _NoVenda:
    def __init__(self, venda):
        self.venda = venda
        self.proximo = None


class RegistroVendas:
    def __init__(self):
        self.__cabeca = None
        self.__receita = 0.0
        self.__total = 0

    def registrar(self, venda):
        novo = _NoVenda(venda)
        if self.__cabeca is None:
            self.__cabeca = novo
        else:
            atual = self.__cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo
        self.__receita += venda.get_total()
        self.__total += 1

    def get_receita(self): return self.__receita
    def get_total(self): return self.__total

    def exibir(self):
        print("\nREGISTRO DE VENDAS")
        print("=" * 60)
        if self.__cabeca is None:
            print("   Nenhuma venda registrada.")
            return
        atual = self.__cabeca
        while atual:
            atual.venda.exibir()
            atual = atual.proximo
        print("=" * 60)
        print(f"Vendas realizadas : {self.__total}")
        print(f"Receita total     : R${self.__receita:.2f}")


def realizar_venda(fila, estoque, registro, itens):
    pessoa = fila.desenfileirar()
    if pessoa is None:
        return

    venda = Venda(pessoa)

    for nome, qtd in itens:
        produto = estoque.buscar(nome)
        if produto is None:
            print(f"'{nome}' nao encontrado no estoque.")
            continue
        ok, msg = estoque.dar_baixa(nome, qtd)
        if ok:
            venda.adicionar_item(ItemVenda(nome, qtd, produto.get_preco_venda()))
        else:
            print(f"Nao foi possivel adicionar '{nome}': {msg}")

    if venda.tem_itens():
        registro.registrar(venda)
        venda.exibir()
    else:
        print(f"Nenhum item disponivel para {pessoa.get_nome()}. Venda nao registrada.")


if __name__ == "__main__":

    print("=" * 60)
    print("QUESTAO 3 - CONTROLE DE CONSUMO / VENDA")
    print("=" * 60)

    estoque = Estoque()
    estoque.adicionar(Produto("Coca 200ml", 2.00, 3.00, "", "", 10))
    estoque.adicionar(Produto("Bonbon", 1.00, 1.50, "", "", 20))
    estoque.exibir()

    fila = FilaAtendimento()
    fila.enfileirar(Pessoa("Vladimir", "aluno", "IA"))
    fila.enfileirar(Pessoa("Orlando The Best", "professor", "IA"))
    fila.enfileirar(Pessoa("Debora", "aluno", "IA"))
    fila.enfileirar(Pessoa("Natalia", "aluno", "IA"))
    fila.enfileirar(Pessoa("Luan", "servidor", "ESG"))
    fila.exibir()

    registro = RegistroVendas()

    print("\n--- Processando vendas ---")
    realizar_venda(fila, estoque, registro, [("Coca 200ml", 1), ("Bonbon", 2)])
    realizar_venda(fila, estoque, registro, [("Coca 200ml", 2)])
    realizar_venda(fila, estoque, registro, [("Bonbon", 1), ("Coca 200ml", 1)])

    registro.exibir()
    estoque.exibir()