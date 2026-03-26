from datetime import datetime
import random

#criei classe produto
class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_vencimento, quantidade):
        self.__nome               = nome
        self.__preco_compra       = preco_compra
        self.__preco_venda        = preco_venda
        self.__data_vencimento    = data_vencimento
        self.__quantidade         = quantidade
        self.__quantidade_inicial = quantidade

    def get_nome(self):         return self.__nome
    def get_preco_compra(self): return self.__preco_compra
    def get_preco_venda(self):  return self.__preco_venda
    def get_quantidade(self):   return self.__quantidade

    def set_quantidade(self, nova):
        if nova < 0:
            raise ValueError("Quantidade nao pode ser negativa.")
        self.__quantidade = nova

    def restaurar(self):
        self.__quantidade = self.__quantidade_inicial

    def __str__(self):
        return f"{self.__nome:<30} Qtd: {self.__quantidade}"


class _No:
    def __init__(self, dado):
        self.dado    = dado
        self.proximo = None


class ListaEstoque:
    def __init__(self):
        self.__cabeca  = None
        self.__tamanho = 0

    def adicionar(self, produto):
        novo = _No(produto)
        if not self.__cabeca:
            self.__cabeca = novo
        else:
            atual = self.__cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo
        self.__tamanho += 1

    def buscar(self, nome):
        atual = self.__cabeca
        while atual:
            if atual.dado.get_nome().lower() == nome.lower():
                return atual.dado
            atual = atual.proximo
        return None

    def dar_baixa(self, nome, qtd):
        produto = self.buscar(nome)
        if produto is None:
            return False, "Produto nao encontrado"
        if produto.get_quantidade() < qtd:
            return False, f"Estoque insuficiente (disponivel: {produto.get_quantidade()})"
        produto.set_quantidade(produto.get_quantidade() - qtd)
        return True, "OK"

    def restaurar(self):
        atual = self.__cabeca
        while atual:
            atual.dado.restaurar()
            atual = atual.proximo

    def elemento_aleatorio(self):
        if self.__cabeca is None:
            return None
        indice = random.randint(0, self.__tamanho - 1)
        atual  = self.__cabeca
        for _ in range(indice):
            atual = atual.proximo
        return atual.dado

    def exibir(self):
        print("\nESTOQUE")
        print("=" * 60)
        atual = self.__cabeca
        while atual:
            print(f"   {atual.dado}")
            atual = atual.proximo
        print("=" * 60)


class ItemVenda:
    def __init__(self, nome, qtd, preco_venda, preco_custo):
        self.__nome        = nome
        self.__qtd         = qtd
        self.__preco_venda = preco_venda
        self.__preco_custo = preco_custo

    def get_nome(self):  return self.__nome
    def get_qtd(self):   return self.__qtd
    def get_total(self): return self.__qtd * self.__preco_venda
    def get_lucro(self): return self.__qtd * (self.__preco_venda - self.__preco_custo)

    def __str__(self):
        return f"{self.__nome} x{self.__qtd} = R${self.get_total():.2f}"


class _NoItem:
    def __init__(self, item):
        self.item    = item
        self.proximo = None


class Venda:
    def __init__(self, cliente):
        self.__cliente      = cliente
        self.__data         = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.__cabeca_itens = None
        self.__total        = 0.0

    def get_cliente(self): return self.__cliente
    def get_total(self):   return self.__total

    def adicionar(self, item):
        novo = _NoItem(item)
        if self.__cabeca_itens is None:
            self.__cabeca_itens = novo
        else:
            atual = self.__cabeca_itens
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo
        self.__total += item.get_total()

    def tem_itens(self):
        return self.__cabeca_itens is not None

    def iterar_itens(self):
        atual = self.__cabeca_itens
        while atual:
            yield atual.item
            atual = atual.proximo

    def exibir(self):
        print(f"\n  Cliente: {self.__cliente} | {self.__data}")
        atual = self.__cabeca_itens
        while atual:
            print(f"    {atual.item}")
            atual = atual.proximo
        print(f"    Total: R${self.__total:.2f}")


class _NoVenda:
    def __init__(self, venda):
        self.venda   = venda
        self.proximo = None


class RegistroVendas:
    def __init__(self):
        self.__cabeca  = None
        self.__total   = 0
        self.__receita = 0.0

    def registrar(self, venda):
        novo = _NoVenda(venda)
        if self.__cabeca is None:
            self.__cabeca = novo
        else:
            atual = self.__cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo
        self.__total   += 1
        self.__receita += venda.get_total()

    def esta_vazio(self):
        return self.__cabeca is None

    def relatorio_vendas(self):
        print("\nRELATORIO DE VENDAS")
        print("=" * 60)
        if self.esta_vazio():
            print("   Nenhuma venda realizada.")
            return
        atual = self.__cabeca
        while atual:
            atual.venda.exibir()
            atual = atual.proximo
        print("\n" + "=" * 60)
        print(f"   Vendas realizadas : {self.__total}")
        print(f"   Receita total     : R${self.__receita:.2f}")
        print("=" * 60)

    def relatorio_consumo_por_pessoa(self):
        print("\nRELATORIO DE CONSUMO POR PESSOA")
        print("=" * 60)
        if self.esta_vazio():
            print("   Nenhuma venda registrada.")
            return

        consumo = {}

        atual = self.__cabeca
        while atual:
            v       = atual.venda
            cliente = v.get_cliente()
            if cliente not in consumo:
                consumo[cliente] = {"total": 0.0, "itens": {}}
            consumo[cliente]["total"] += v.get_total()
            for item in v.iterar_itens():
                nome = item.get_nome()
                consumo[cliente]["itens"][nome] = (
                    consumo[cliente]["itens"].get(nome, 0) + item.get_qtd()
                )
            atual = atual.proximo

        for cliente, dados in consumo.items():
            print(f"\n  {cliente}")
            for nome, qtd in dados["itens"].items():
                print(f"    {nome}: {qtd} unidade(s)")
            print(f"    Total gasto: R${dados['total']:.2f}")

        print("\n" + "=" * 60)


_NOMES_CLIENTES = ["Vladimir", "Orlando", "Debora", "Natalia", "Luan"]


def gerar_vendas_automaticas(estoque, registro):
    if estoque.elemento_aleatorio() is None:
        print("Nenhum produto no estoque!")
        return

    geradas = 0
    for _ in range(5):
        cliente = random.choice(_NOMES_CLIENTES)
        venda   = Venda(cliente)

        for _ in range(random.randint(1, 3)):
            produto = estoque.elemento_aleatorio()
            if produto is None or produto.get_quantidade() == 0:
                continue
            qtd = random.randint(1, min(3, produto.get_quantidade()))
            ok, _ = estoque.dar_baixa(produto.get_nome(), qtd)
            if ok:
                venda.adicionar(ItemVenda(
                    produto.get_nome(), qtd,
                    produto.get_preco_venda(),
                    produto.get_preco_compra(),
                ))

        if venda.tem_itens():
            registro.registrar(venda)
            geradas += 1

    print(f"{geradas} venda(s) automatica(s) gerada(s).")


def menu(estoque, registro):
    opcoes = {
        "1": "Ver estoque",
        "2": "Gerar vendas automaticas",
        "3": "Restaurar estoque",
        "4": "Relatorio de vendas",
        "5": "Relatorio de consumo por pessoa",
        "6": "Adicionar produto",
        "0": "Sair",
    }

    while True:
        print("\n===== MENU - CANTINA FATEC =====")
        for chave, descricao in opcoes.items():
            print(f"  {chave} - {descricao}")

        op = input("Escolha: ").strip()

        if op == "0":
            print("Saindo...")
            break
        elif op == "1":
            estoque.exibir()
        elif op == "2":
            gerar_vendas_automaticas(estoque, registro)
        elif op == "3":
            estoque.restaurar()
            print("Estoque restaurado!")
        elif op == "4":
            registro.relatorio_vendas()
        elif op == "5":
            registro.relatorio_consumo_por_pessoa()
        elif op == "6":
            nome   = input("Nome do produto: ")
            pc     = float(input("Preço de compra: "))
            pv     = float(input("Preço de venda: "))
            venc   = input("Data de vencimento (dd/mm/yyyy): ")
            qtd    = int(input("Quantidade: "))
            estoque.adicionar(Produto(nome, pc, pv, venc, qtd))
            print(f"{nome} adicionado ao estoque!")
        else:
            print("Opcao invalida.")


if __name__ == "__main__":

    estoque = ListaEstoque()
    estoque.adicionar(Produto("Agua com gas do Orlando", 2.50, 3.50, "25/03/2027", 12))
    estoque.adicionar(Produto("Coca 200ml",              2.00, 3.00, "22/03/2027", 12))
    estoque.adicionar(Produto("Coca Zero 200ml",         2.00, 3.00, "22/03/2027", 12))
    estoque.adicionar(Produto("Agua normal",             2.00, 3.00, "28/03/2027", 12))
    estoque.adicionar(Produto("Amendoim",                2.00, 3.00, "10/04/2027", 10))
    estoque.adicionar(Produto("Torcida",                 2.00, 3.00, "05/04/2027", 10))
    estoque.adicionar(Produto("Bonbon",                  1.00, 1.50, "30/12/2026", 40))
    estoque.adicionar(Produto("Pao de Mel Bauduco",      2.00, 3.00, "20/12/2026", 12))

    registro = RegistroVendas()

    menu(estoque, registro)