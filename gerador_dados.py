# QUESTÃO 4 

from faker import Faker
import random
from datetime import datetime, timedelta

faker = Faker("pt_BR")


class PessoaGerada:
    def __init__(self, nome, categoria, curso, cpf, email):
        self.nome      = nome
        self.categoria = categoria
        self.curso     = curso
        self.cpf       = cpf
        self.email     = email

    def __str__(self):
        return (f"Nome: {self.nome} | Cat: {self.categoria} | "
                f"Curso: {self.curso} | CPF: {self.cpf} | Email: {self.email}")


class ProdutoGerado:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        self.nome            = nome
        self.preco_compra    = preco_compra
        self.preco_venda     = preco_venda
        self.data_compra     = data_compra
        self.data_vencimento = data_vencimento
        self.quantidade      = quantidade

    def __str__(self):
        return (f"Produto: {self.nome} | "
                f"Compra: R${self.preco_compra:.2f} | "
                f"Venda: R${self.preco_venda:.2f} | "
                f"Vence: {self.data_vencimento} | "
                f"Qtd: {self.quantidade}")


class PagamentoGerado:
    def __init__(self, pessoa, produto, quantidade):
        self.pessoa      = pessoa
        self.produto     = produto
        self.quantidade  = quantidade
        self.valor       = round(produto.preco_venda * quantidade, 2)

        dias_atras       = random.randint(0, 30)
        data_base        = datetime.now() - timedelta(days=dias_atras)
        self.data_hora   = data_base.strftime("%d/%m/%Y %H:%M:%S")

    def __str__(self):
        return (f"{self.pessoa.nome} comprou {self.quantidade}x "
                f"'{self.produto.nome}' = R${self.valor:.2f} em {self.data_hora}")


class No:
    def __init__(self, dado):
        self.dado    = dado
        self.proximo = None


class ListaEncadeada:
    def __init__(self, nome="Lista"):
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
        print(f"\n📋 {self.nome} ({self.tamanho} registro(s)):")
        print("-" * 70)

        if self.cabeca is None:
            print("   (vazia)")
            return

        atual = self.cabeca
        i     = 1
        while atual:
            print(f"  [{i:02d}] {atual.dado}")
            atual = atual.proximo
            i    += 1

        print("-" * 70)


def gerar_pessoas(quantidade):
    categorias = ["aluno", "professor", "servidor"]
    cursos     = ["IA", "ESG"]

    lista = ListaEncadeada("Pessoas Geradas")

    for _ in range(quantidade):
        nome      = faker.name()
        categoria = random.choice(categorias)
        curso     = random.choice(cursos)
        cpf       = faker.cpf()
        email     = faker.email()

        pessoa = PessoaGerada(nome, categoria, curso, cpf, email)
        lista.adicionar(pessoa)

    return lista


def gerar_produtos(quantidade):
    nomes_base = [
        "Água com gás do Orlando", "Coca 200ml", "Coca Zero 200ml",
        "Água normal", "Amendoim", "Torcida", "Bonbon", "Pão de Mel Bauduco"
    ]

    precos = {
        "Água com gás do Orlando": (2.50, 3.50),
        "Coca 200ml":              (2.00, 3.00),
        "Coca Zero 200ml":         (2.00, 3.00),
        "Água normal":             (2.00, 3.00),
        "Amendoim":                (2.00, 3.00),
        "Torcida":                 (2.00, 3.00),
        "Bonbon":                  (1.00, 1.50),
        "Pão de Mel Bauduco":      (2.00, 3.00),
    }

    lista = ListaEncadeada("Produtos Gerados")

    for _ in range(quantidade):
        nome       = random.choice(nomes_base)
        pc, pv     = precos[nome]
        qtd        = random.randint(5, 50)

        dias_compra  = random.randint(0, 30)
        dt_compra    = datetime.now() - timedelta(days=dias_compra)
        data_compra  = dt_compra.strftime("%d/%m/%Y")

        dias_venc     = random.randint(30, 365)
        dt_venc       = datetime.now() + timedelta(days=dias_venc)
        data_venc     = dt_venc.strftime("%d/%m/%Y")

        produto = ProdutoGerado(nome, pc, pv, data_compra, data_venc, qtd)
        lista.adicionar(produto)

    return lista


def gerar_pagamentos(lista_pessoas, lista_produtos, quantidade):
    pessoas  = []
    atual    = lista_pessoas.cabeca
    while atual:
        pessoas.append(atual.dado)
        atual = atual.proximo

    produtos = []
    atual    = lista_produtos.cabeca
    while atual:
        produtos.append(atual.dado)
        atual = atual.proximo

    lista = ListaEncadeada("Pagamentos Gerados")

    for _ in range(quantidade):
        pessoa    = random.choice(pessoas)
        produto   = random.choice(produtos)
        qtd       = random.randint(1, 3)

        pagamento = PagamentoGerado(pessoa, produto, qtd)
        lista.adicionar(pagamento)

    return lista


if __name__ == "__main__":

    print("=" * 70)
    print("        QUESTÃO 4 – GERADOR DE DADOS – CANTINA FATEC")
    print("=" * 70)

    print("\n👥 Gerando 5 pessoas...")
    pessoas  = gerar_pessoas(5)
    pessoas.exibir()

    print("\n📦 Gerando 5 lotes de produtos...")
    produtos = gerar_produtos(5)
    produtos.exibir()

    print("\n💳 Gerando 8 pagamentos aleatórios...")
    pagamentos = gerar_pagamentos(pessoas, produtos, 8)
    pagamentos.exibir()

    print("\n✅ Dados gerados com sucesso!")
    print("   (Use questao5.py para salvar esses dados em disco.)")