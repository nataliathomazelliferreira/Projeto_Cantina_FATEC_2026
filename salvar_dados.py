#QUESTÃO 5

from datetime import datetime
import pickle
import os

class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        self.nome            = nome
        self.preco_compra    = preco_compra
        self.preco_venda     = preco_venda
        self.data_compra     = data_compra
        self.data_vencimento = data_vencimento
        self.quantidade      = quantidade

    def __str__(self):
        return (f"{self.nome} | Compra: R${self.preco_compra:.2f} | "
                f"Venda: R${self.preco_venda:.2f} | "
                f"Vence: {self.data_vencimento} | Qtd: {self.quantidade}")


class Pagamento:
    def __init__(self, nome_pessoa, categoria, valor, data_hora):
        self.nome_pessoa = nome_pessoa
        self.categoria   = categoria
        self.valor       = valor
        self.data_hora   = data_hora

    def __str__(self):
        return (f"{self.nome_pessoa} ({self.categoria}) | "
                f"R${self.valor:.2f} | {self.data_hora}")


class No:
    def __init__(self, dado):
        self.dado    = dado
        self.proximo = None


class ListaEncadeada:
    def __init__(self, nome=""):
        self.cabeca  = None
        self.tamanho = 0
        self.nome    = nome

    def adicionar(self, dado):
        novo_no = No(dado)
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no
        self.tamanho += 1

    def exibir(self):
        print(f"\n📋 {self.nome} ({self.tamanho} item(ns)):")
        print("-" * 60)
        if self.cabeca is None:
            print("   (vazia)")
            return
        atual = self.cabeca
        i = 1
        while atual:
            print(f"  [{i}] {atual.dado}")
            atual = atual.proximo
            i    += 1
        print("-" * 60)


class Snapshot:
    def __init__(self, descricao, estoque, pagamentos):
        self.descricao  = descricao
        self.criado_em  = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.estoque    = estoque
        self.pagamentos = pagamentos

    def __str__(self):
        return (f"Snapshot: '{self.descricao}' | "
                f"Criado em: {self.criado_em} | "
                f"Produtos: {self.estoque.tamanho} | "
                f"Pagamentos: {self.pagamentos.tamanho}")


def salvar(objeto, caminho_arquivo):
    try:
        with open(caminho_arquivo, "wb") as arquivo:
            pickle.dump(objeto, arquivo)

        print(f"✅ Dados salvos em: '{caminho_arquivo}'")
        return True

    except Exception as erro:
        print(f"❌ Erro ao salvar: {erro}")
        return False


def carregar(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        print(f"❌ Arquivo '{caminho_arquivo}' não encontrado.")
        return None

    try:
        with open(caminho_arquivo, "rb") as arquivo:
            objeto = pickle.load(arquivo)

        print(f"✅ Dados carregados de: '{caminho_arquivo}'")
        return objeto

    except Exception as erro:
        print(f"❌ Erro ao carregar: {erro}")
        return None


def deletar_arquivo(caminho_arquivo):
    if os.path.exists(caminho_arquivo):
        os.remove(caminho_arquivo)
        print(f"🗑️  Arquivo '{caminho_arquivo}' removido.")
    else:
        print(f"⚠️  Arquivo '{caminho_arquivo}' não existe.")


def listar_arquivos_salvos(pasta="."):
    print(f"\n📁 Arquivos .pkl encontrados em '{pasta}':")
    encontrou = False

    for nome_arquivo in os.listdir(pasta):
        if nome_arquivo.endswith(".pkl"):
            caminho    = os.path.join(pasta, nome_arquivo)
            tamanho_kb = os.path.getsize(caminho) / 1024
            print(f"  • {nome_arquivo} ({tamanho_kb:.2f} KB)")
            encontrou = True

    if not encontrou:
        print("  (nenhum arquivo .pkl encontrado)")


if __name__ == "__main__":

    print("=" * 65)
    print("      QUESTÃO 5 – PERSISTÊNCIA DE DADOS – CANTINA FATEC")
    print("=" * 65)

    estoque = ListaEncadeada("Estoque")
    estoque.adicionar(Produto("Água com gás do Orlando", 2.50, 3.50, "13/03/2026", "25/03/2027", 12))
    estoque.adicionar(Produto("Coca 200ml",              2.00, 3.00, "13/03/2026", "22/03/2027", 12))
    estoque.adicionar(Produto("Coca Zero 200ml",         2.00, 3.00, "13/03/2026", "22/03/2027", 12))
    estoque.adicionar(Produto("Água normal",             2.00, 3.00, "13/03/2026", "28/03/2027", 12))
    estoque.adicionar(Produto("Amendoim",                2.00, 3.00, "12/03/2026", "10/04/2027",  6))
    estoque.adicionar(Produto("Torcida",                 2.00, 3.00, "12/03/2026", "05/04/2027", 10))
    estoque.adicionar(Produto("Bonbon",                  1.00, 1.50, "10/03/2026", "30/12/2026", 40))
    estoque.adicionar(Produto("Pão de Mel Bauduco",      2.00, 3.00, "11/03/2026", "20/12/2026", 12))

    pagamentos = ListaEncadeada("Pagamentos")
    pagamentos.adicionar(Pagamento("Ana Lima",       "aluno",     3.00, "25/03/2026 09:10:00"))
    pagamentos.adicionar(Pagamento("Carlos Souza",   "professor", 1.50, "25/03/2026 09:15:33"))
    pagamentos.adicionar(Pagamento("Beatriz Mendes", "aluno",     6.00, "25/03/2026 09:22:47"))

    print("\n📊 Dados antes de salvar:")
    estoque.exibir()
    pagamentos.exibir()

    snap = Snapshot("Abertura da Cantina – 25/03/2026", estoque, pagamentos)
    print(f"\n📸 {snap}")

    ARQUIVO = "cantina_snapshot.pkl"
    salvar(snap, ARQUIVO)

    print("\n🔄 Simulando reinicialização do sistema...")
    print("   (Carregando dados salvos do disco...)\n")

    snap_carregado = carregar(ARQUIVO)

    if snap_carregado:
        print(f"\n📸 Snapshot recuperado: {snap_carregado}")

        print("\n📦 Estoque recuperado:")
        snap_carregado.estoque.exibir()

        print("\n💳 Pagamentos recuperados:")
        snap_carregado.pagamentos.exibir()

    listar_arquivos_salvos(".")