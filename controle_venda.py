#QUESTÃO 3 

from datetime import datetime

class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.data_vencimento = data_vencimento
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.nome} | Venda: R${self.preco_venda:.2f} | Qtd: {self.quantidade}"


class NoProduto:
    def __init__(self, produto):
        self.produto = produto
        self.proximo = None


class Estoque:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0

    def adicionar(self, produto):
        novo_no = NoProduto(produto)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no
        self.tamanho += 1

    def buscar(self, nome):
        atual = self.cabeca
        while atual:
            if atual.produto.nome.lower() == nome.lower():
                return atual.produto
            atual = atual.proximo
        return None

    def dar_baixa(self, nome, qtd):
        produto = self.buscar(nome)
        if produto is None:
            return False, "Produto não encontrado"
        if produto.quantidade < qtd:
            return False, f"Estoque insuficiente (disponível: {produto.quantidade})"
        produto.quantidade -= qtd
        return True, "OK"

    def exibir(self):
        print("\n📦 Estoque atual:")
        atual = self.cabeca
        while atual:
            print(f"   • {atual.produto}")
            atual = atual.proximo


class Pessoa:
    def __init__(self, nome, categoria, curso):
        self.nome = nome
        self.categoria = categoria
        self.curso = curso

    def __str__(self):
        return f"{self.nome} ({self.categoria} – {self.curso})"


class NoFila:
    def __init__(self, pessoa):
        self.pessoa = pessoa
        self.proximo = None


class FilaAtendimento:
    def __init__(self):
        self.frente = None
        self.fundo = None
        self.tamanho = 0

    def enfileirar(self, pessoa):
        novo_no = NoFila(pessoa)

        if self.fundo is None:
            self.frente = novo_no
            self.fundo = novo_no
        else:
            self.fundo.proximo = novo_no
            self.fundo = novo_no

        self.tamanho += 1
        print(f"🟢 {pessoa.nome} entrou na fila. Posição: {self.tamanho}")

    def desenfileirar(self):
        if self.frente is None:
            print("⚠️ Fila vazia.")
            return None

        pessoa = self.frente.pessoa
        self.frente = self.frente.proximo

        if self.frente is None:
            self.fundo = None

        self.tamanho -= 1
        return pessoa


class ItemVenda:
    def __init__(self, produto_nome, quantidade, preco_unitario):
        self.produto_nome = produto_nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    @property
    def subtotal(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return f"{self.produto_nome} x{self.quantidade} = R${self.subtotal:.2f}"


# ✅ CORREÇÃO AQUI (fora do método)
class NoItem:
    def __init__(self, item):
        self.item = item
        self.proximo = None


class NoVenda:
    def __init__(self, venda):
        self.venda = venda
        self.proximo = None


class Venda:
    _contador = 0

    def __init__(self, pessoa):
        Venda._contador += 1
        self.id = Venda._contador
        self.pessoa = pessoa
        self.data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.cabeca_itens = None
        self.total = 0.0

    def adicionar_item(self, item):
        novo = NoItem(item)

        if self.cabeca_itens is None:
            self.cabeca_itens = novo
        else:
            atual = self.cabeca_itens
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo

        self.total += item.subtotal

    def exibir(self):
        print(f"\n🧾 VENDA #{self.id}")
        print(f"Cliente: {self.pessoa}")
        atual = self.cabeca_itens
        while atual:
            print(f"   • {atual.item}")
            atual = atual.proximo
        print(f"TOTAL: R${self.total:.2f}")


class RegistroVendas:
    def __init__(self):
        self.cabeca = None
        self.receita = 0.0

    def registrar(self, venda):
        novo = NoVenda(venda)

        if self.cabeca is None:
            self.cabeca = novo
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo

        self.receita += venda.total

    def exibir(self):
        atual = self.cabeca
        while atual:
            atual.venda.exibir()
            atual = atual.proximo


def realizar_venda(fila, estoque, registro, itens):
    pessoa = fila.desenfileirar()
    if pessoa is None:
        return

    venda = Venda(pessoa)

    for nome, qtd in itens:
        produto = estoque.buscar(nome)

        if produto is None:
            continue

        ok, _ = estoque.dar_baixa(nome, qtd)

        if ok:
            venda.adicionar_item(ItemVenda(nome, qtd, produto.preco_venda))

    if venda.cabeca_itens:
        registro.registrar(venda)
        venda.exibir()


if __name__ == "__main__":

    estoque = Estoque()
    estoque.adicionar(Produto("Coca 200ml", 2, 3, "", "", 10))
    estoque.adicionar(Produto("Bonbon", 1, 1.5, "", "", 20))

    fila = FilaAtendimento()

    fila.enfileirar(Pessoa("Vladimir", "aluno", "IA"))
    fila.enfileirar(Pessoa("Orlando The Best", "professor", "ESG"))
    fila.enfileirar(Pessoa("Debora", "aluno", "IA"))
    fila.enfileirar(Pessoa("Natalia", "aluno", "IA"))
    fila.enfileirar(Pessoa("Luan", "servidor", "IA"))

    registro = RegistroVendas()

    realizar_venda(fila, estoque, registro, [("Coca 200ml", 1), ("Bonbon", 2)])

    registro.exibir()