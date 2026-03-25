#QUESTÃO 3 

from datetime import datetime

class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        self.nome            = nome
        self.preco_compra    = preco_compra
        self.preco_venda     = preco_venda
        self.data_compra     = data_compra
        self.data_vencimento = data_vencimento
        self.quantidade      = quantidade

    def __str__(self):
        return f"{self.nome} | Venda: R${self.preco_venda:.2f} | Qtd: {self.quantidade}"


class NoProduto:
    def __init__(self, produto):
        self.produto  = produto
        self.proximo  = None


class Estoque:
    def __init__(self):
        self.cabeca  = None
        self.tamanho = 0

    def adicionar(self, produto):
        novo_no          = NoProduto(produto)
        novo_no.proximo  = self.cabeca
        self.cabeca      = novo_no
        self.tamanho    += 1

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
        self.nome      = nome
        self.categoria = categoria
        self.curso     = curso

    def __str__(self):
        return f"{self.nome} ({self.categoria} – {self.curso})"


class NoFila:
    def __init__(self, pessoa):
        self.pessoa   = pessoa
        self.proximo  = None


class FilaAtendimento:
    def __init__(self):
        self.frente  = None
        self.fundo   = None
        self.tamanho = 0

    def enfileirar(self, pessoa):
        novo_no = NoFila(pessoa)

        if self.fundo is None:
            self.frente = novo_no
            self.fundo  = novo_no
        else:
            self.fundo.proximo = novo_no
            self.fundo         = novo_no

        self.tamanho += 1
        print(f"🟢 {pessoa.nome} entrou na fila. Posição: {self.tamanho}")

    def desenfileirar(self):
        if self.frente is None:
            print("⚠️  Fila vazia — ninguém para atender.")
            return None

        pessoa_atendida = self.frente.pessoa
        self.frente     = self.frente.proximo

        if self.frente is None:
            self.fundo = None

        self.tamanho -= 1
        return pessoa_atendida

    def esta_vazia(self):
        return self.frente is None

    def exibir(self):
        print(f"\n👥 Fila de atendimento ({self.tamanho} pessoa(s)):")
        atual = self.frente
        pos   = 1
        while atual:
            print(f"   [{pos}] {atual.pessoa}")
            atual    = atual.proximo
            pos     += 1


class ItemVenda:
    def __init__(self, produto_nome, quantidade, preco_unitario):
        self.produto_nome    = produto_nome
        self.quantidade      = quantidade
        self.preco_unitario  = preco_unitario

    @property
    def subtotal(self):
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return (f"{self.produto_nome} x{self.quantidade} "
                f"@ R${self.preco_unitario:.2f} = R${self.subtotal:.2f}")


class NoVenda:
    def __init__(self, venda):
        self.venda   = venda
        self.proximo = None


class Venda:
    _contador = 0

    def __init__(self, pessoa):
        Venda._contador += 1
        self.id          = Venda._contador
        self.pessoa      = pessoa
        self.data_hora   = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.cabeca_itens = None
        self.total       = 0.0

    def adicionar_item(self, item):
        class NoItem:
            def __init__(self, i):
                self.item    = i
                self.proximo = None

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
        print(f"\n🧾 VENDA #{self.id} — {self.data_hora}")
        print(f"   Cliente: {self.pessoa}")
        print("   Itens:")
        atual = self.cabeca_itens
        while atual:
            print(f"     • {atual.item}")
            atual = atual.proximo
        print(f"   💰 TOTAL: R${self.total:.2f}")


class RegistroVendas:
    def __init__(self):
        self.cabeca  = None
        self.tamanho = 0
        self.receita = 0.0

    def registrar(self, venda):
        novo_no = NoVenda(venda)

        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

        self.tamanho += 1
        self.receita  += venda.total

    def exibir_todas(self):
        print("\n📋 TODAS AS VENDAS REGISTRADAS:")
        print("=" * 50)
        if self.cabeca is None:
            print("   Nenhuma venda registrada.")
            return
        atual = self.cabeca
        while atual:
            atual.venda.exibir()
            atual = atual.proximo
        print("=" * 50)
        print(f"   Total de vendas: {self.tamanho} | Receita total: R${self.receita:.2f}")


def realizar_venda(fila, estoque, registro_vendas, itens_pedido):
    pessoa = fila.desenfileirar()
    if pessoa is None:
        return

    print(f"\n🛒 Atendendo: {pessoa}")

    venda = Venda(pessoa)

    for nome_prod, qtd in itens_pedido:
        produto = estoque.buscar(nome_prod)

        if produto is None:
            print(f"   ❌ Produto '{nome_prod}' não encontrado.")
            continue

        sucesso, mensagem = estoque.dar_baixa(nome_prod, qtd)

        if sucesso:
            item = ItemVenda(nome_prod, qtd, produto.preco_venda)
            venda.adicionar_item(item)
            print(f"   ✅ {item}")
        else:
            print(f"   ⚠️  {nome_prod}: {mensagem}")

    if venda.cabeca_itens is not None:
        registro_vendas.registrar(venda)
        venda.exibir()
    else:
        print("   ⚠️  Venda cancelada — nenhum item disponível.")


if __name__ == "__main__":

    print("=" * 65)
    print("    QUESTÃO 3 – CONTROLE DE CONSUMO/VENDA – CANTINA FATEC")
    print("=" * 65)

    estoque = Estoque()
    estoque.adicionar(Produto("Água com gás do Orlando", 2.50, 3.50, "13/03/2026", "25/03/2027", 12))
    estoque.adicionar(Produto("Coca 200ml",              2.00, 3.00, "13/03/2026", "22/03/2027", 12))
    estoque.adicionar(Produto("Coca Zero 200ml",         2.00, 3.00, "13/03/2026", "22/03/2027", 12))
    estoque.adicionar(Produto("Água normal",             2.00, 3.00, "13/03/2026", "28/03/2027", 12))
    estoque.adicionar(Produto("Amendoim",                2.00, 3.00, "12/03/2026", "10/04/2027",  6))
    estoque.adicionar(Produto("Torcida",                 2.00, 3.00, "12/03/2026", "05/04/2027", 10))
    estoque.adicionar(Produto("Bonbon",                  1.00, 1.50, "10/03/2026", "30/12/2026", 40))
    estoque.adicionar(Produto("Pão de Mel Bauduco",      2.00, 3.00, "11/03/2026", "20/12/2026", 12))

    fila = FilaAtendimento()

    print("\n📥 Pessoas chegando na cantina...\n")
    fila.enfileirar(Pessoa("Ana Lima",       "aluno",     "IA"))
    fila.enfileirar(Pessoa("Carlos Souza",   "professor", "ESG"))
    fila.enfileirar(Pessoa("Beatriz Mendes", "aluno",     "IA"))

    fila.exibir()

    registro = RegistroVendas()

    print("\n" + "─" * 55)
    realizar_venda(fila, estoque, registro,
                   [("Coca 200ml", 1), ("Bonbon", 2)])

    print("\n" + "─" * 55)
    realizar_venda(fila, estoque, registro,
                   [("Água com gás do Orlando", 1), ("Pão de Mel Bauduco", 1)])

    print("\n" + "─" * 55)
    realizar_venda(fila, estoque, registro,
                   [("Amendoim", 3)])

    registro.exibir_todas()
    estoque.exibir()