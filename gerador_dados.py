#questão 4   
from faker import Faker
import random
from datetime import datetime, timedelta


faker = Faker("pt_BR")


class PessoaGerada:
    def __init__(self, nome, categoria, curso, cpf, email):
        self.__nome = nome
        self.__categoria = categoria
        self.__curso = curso
        self.__cpf = cpf
        self.__email = email

    def get_nome(self): return self.__nome
    def get_categoria(self): return self.__categoria
    def get_curso(self): return self.__curso
    def get_cpf(self): return self.__cpf
    def get_email(self): return self.__email

    def __str__(self):
        return (f"Nome: {self.__nome:<30} | Cat: {self.__categoria:<10} | "
                f"Curso: {self.__curso:<5} | CPF: {self.__cpf} | Email: {self.__email}")


class ProdutoGerado:
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
    def get_data_compra(self): return self.__data_compra
    def get_data_vencimento(self): return self.__data_vencimento
    def get_quantidade(self): return self.__quantidade

    def __str__(self):
        return (f"Produto: {self.__nome:<30} | "
                f"Compra: R${self.__preco_compra:.2f} | "
                f"Venda: R${self.__preco_venda:.2f} | "
                f"Vence: {self.__data_vencimento} | "
                f"Qtd: {self.__quantidade}")


class PagamentoGerado:
    def __init__(self, pessoa, produto, quantidade):
        if pessoa is None or produto is None:
            raise ValueError("Pessoa ou produto invalido.")

        self.__pessoa = pessoa
        self.__produto = produto
        self.__quantidade = quantidade
        self.__valor = round(produto.get_preco_venda() * quantidade, 2)
        dias_atras = random.randint(0, 30)
        self.__data_hora = datetime.now() - timedelta(days=dias_atras)

    def get_pessoa(self): return self.__pessoa
    def get_produto(self): return self.__produto
    def get_valor(self): return self.__valor
    def get_data_hora(self): return self.__data_hora

    def __str__(self):
        return (f"{self.__pessoa.get_nome():<30} comprou "
                f"{self.__quantidade}x '{self.__produto.get_nome()}' "
                f"= R${self.__valor:.2f} em {self.__data_hora.strftime('%d/%m/%Y %H:%M:%S')}")


class _No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaEncadeada:
    def __init__(self, nome="Lista"):
        self.__cabeca = None
        self.__tamanho = 0
        self.__nome = nome

    def adicionar(self, dado):
        novo_no = _No(dado)
        if self.__cabeca is None:
            self.__cabeca = novo_no
        else:
            atual = self.__cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no
        self.__tamanho += 1

    def get_tamanho(self): return self.__tamanho

    def elemento_aleatorio(self):
        if self.__cabeca is None:
            return None
        indice = random.randint(0, self.__tamanho - 1)
        atual = self.__cabeca
        for _ in range(indice):
            atual = atual.proximo
        return atual.dado

    def get_cabeca(self):
        return self.__cabeca

    def exibir(self):
        print(f"\n{self.__nome} ({self.__tamanho} registro(s)):")
        print("-" * 72)
        if self.__cabeca is None:
            print("   (vazia)")
        else:
            atual = self.__cabeca
            i = 1
            while atual:
                print(f"  [{i:02d}] {atual.dado}")
                atual = atual.proximo
                i += 1
        print("-" * 72)


_NOMES_PRODUTOS = [
    "Agua com gas do Orlando", "Coca 200ml", "Coca Zero 200ml",
    "Agua normal", "Amendoim", "Torcida", "Bonbon", "Pao de Mel Bauduco",
]

_PRECOS = {
    "Agua com gas do Orlando": (2.50, 3.50),
    "Coca 200ml": (2.00, 3.00),
    "Coca Zero 200ml": (2.00, 3.00),
    "Agua normal": (2.00, 3.00),
    "Amendoim": (2.00, 3.00),
    "Torcida": (2.00, 3.00),
    "Bonbon": (1.00, 1.50),
    "Pao de Mel Bauduco": (2.00, 3.00),
}


def gerar_pessoas(quantidade):
    categorias = ["aluno", "professor", "servidor"]
    cursos = ["IA", "ESG"]
    lista = ListaEncadeada("Pessoas Geradas")
    for _ in range(quantidade):
        lista.adicionar(PessoaGerada(
            nome=faker.name(),
            categoria=random.choice(categorias),
            curso=random.choice(cursos),
            cpf=faker.cpf(),
            email=faker.email(),
        ))
    return lista


def gerar_produtos(quantidade):
    lista = ListaEncadeada("Produtos Gerados")
    for _ in range(quantidade):
        nome = random.choice(_NOMES_PRODUTOS)
        pc, pv = _PRECOS[nome]
        qtd = random.randint(5, 50)
        dt_compra = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%d/%m/%Y")
        dt_venc = (datetime.now() + timedelta(days=random.randint(30, 365))).strftime("%d/%m/%Y")
        lista.adicionar(ProdutoGerado(nome, pc, pv, dt_compra, dt_venc, qtd))
    return lista


def gerar_pagamentos(lista_pessoas, lista_produtos, quantidade):
    lista = ListaEncadeada("Pagamentos Gerados")
    for _ in range(quantidade):
        pessoa = lista_pessoas.elemento_aleatorio()
        produto = lista_produtos.elemento_aleatorio()
        if pessoa is None or produto is None:
            continue
        lista.adicionar(PagamentoGerado(
            pessoa=pessoa,
            produto=produto,
            quantidade=random.randint(1, 3),
        ))
    return lista


if __name__ == "__main__":

    print("=" * 72)
    print("        QUESTAO 4 - GERADOR DE DADOS - CANTINA FATEC")
    print("=" * 72)

    print("\nGerando 5 pessoas...")
    pessoas = gerar_pessoas(5)
    pessoas.exibir()

    print("\nGerando 5 lotes de produtos...")
    produtos = gerar_produtos(5)
    produtos.exibir()

    print("\nGerando 8 pagamentos aleatorios...")
    pagamentos = gerar_pagamentos(pessoas, produtos, 8)
    pagamentos.exibir()

    print("\nDados gerados com sucesso!")
    print("Execute salvar_dados.py para salvar esses dados em disco.")