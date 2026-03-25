from datetime import datetime
import pickle
import os

class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.data_vencimento = data_vencimento
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.nome} | R${self.preco_venda:.2f} | Qtd: {self.quantidade}"


class Pagamento:
    def __init__(self, nome_pessoa, categoria, valor, data_hora):
        self.nome_pessoa = nome_pessoa
        self.categoria = categoria
        self.valor = valor
        self.data_hora = data_hora

    def __str__(self):
        return f"{self.nome_pessoa} ({self.categoria}) | R${self.valor:.2f} | {self.data_hora}"


class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaEncadeada:
    def __init__(self, nome=""):
        self.cabeca = None
        self.tamanho = 0
        self.nome = nome

    def adicionar(self, dado):
        novo = No(dado)

        if self.cabeca is None:
            self.cabeca = novo
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo

        self.tamanho += 1

    def exibir(self):
        print(f"\n📋 {self.nome} ({self.tamanho}):")

        atual = self.cabeca
        i = 1

        while atual:
            print(f"[{i}] {atual.dado}")
            atual = atual.proximo
            i += 1


class Snapshot:
    def __init__(self, descricao, estoque, pagamentos):
        self.descricao = descricao
        self.criado_em = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.estoque = estoque
        self.pagamentos = pagamentos

    def __str__(self):
        return f"{self.descricao} | {self.criado_em}"


def salvar(obj, arquivo):
    try:
        with open(arquivo, "wb") as f:
            pickle.dump(obj, f)
        print("Dados salvos")
    except:
        print("Erro ao salvar")


def carregar(arquivo):
    if not os.path.exists(arquivo):
        print("Arquivo não existe")
        return None

    try:
        with open(arquivo, "rb") as f:
            return pickle.load(f)
    except:
        print("Erro ao carregar")
        return None


if __name__ == "__main__":

    estoque = ListaEncadeada("Estoque")

    estoque.adicionar(Produto("Água com gás do Orlando", 2.5, 3.5, "", "", 12))
    estoque.adicionar(Produto("Coca 200ml", 2, 3, "", "", 12))
    estoque.adicionar(Produto("Bonbon", 1, 1.5, "", "", 40))

    pagamentos = ListaEncadeada("Pagamentos")

    pagamentos.adicionar(Pagamento("Vladimir", "aluno", 3.0, "25/03/2026"))
    pagamentos.adicionar(Pagamento("Debora", "aluno", 6.0, "25/03/2026"))

    estoque.exibir()
    pagamentos.exibir()

    snap = Snapshot("Backup inicial", estoque, pagamentos)

    salvar(snap, "dados_cantina.pkl")

    print("\nCarregando dados...\n")

    dados = carregar("dados_cantina.pkl")

    if dados:
        dados.estoque.exibir()
        dados.pagamentos.exibir()