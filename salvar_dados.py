#questão 5
import pickle
import os
from datetime import datetime

from questao4 import (
    gerar_pessoas,
    gerar_produtos,
    gerar_pagamentos,
)


class Snapshot:
    def __init__(self, descricao, pessoas, produtos, pagamentos):
        self.__descricao = descricao
        self.__criado_em = datetime.now()
        self.__pessoas = pessoas
        self.__produtos = produtos
        self.__pagamentos = pagamentos

    def get_descricao(self): return self.__descricao
    def get_criado_em(self): return self.__criado_em
    def get_pessoas(self): return self.__pessoas
    def get_produtos(self): return self.__produtos
    def get_pagamentos(self): return self.__pagamentos

    def __str__(self):
        return f"[Snapshot] {self.__descricao} | Criado em: {self.__criado_em.strftime('%d/%m/%Y %H:%M:%S')}"


class GerenciadorArquivo:
    @staticmethod
    def salvar(obj, caminho):
        try:
            pasta = os.path.dirname(caminho)
            if pasta and not os.path.exists(pasta):
                os.makedirs(pasta)

            with open(caminho, "wb") as f:
                pickle.dump(obj, f)
            return True
        except (OSError, pickle.PicklingError):
            return False

    @staticmethod
    def carregar(caminho):
        if not os.path.exists(caminho):
            return None
        try:
            with open(caminho, "rb") as f:
                return pickle.load(f)
        except (OSError, pickle.UnpicklingError):
            return None


if __name__ == "__main__":

    print("=" * 72)
    print("QUESTAO 5 - PERSISTENCIA DE DADOS - CANTINA FATEC")
    print("=" * 72)

    print("\nGerando dados via Questao 4...")
    pessoas = gerar_pessoas(5)
    produtos = gerar_produtos(5)
    pagamentos = gerar_pagamentos(pessoas, produtos, 8)

    pessoas.exibir()
    produtos.exibir()
    pagamentos.exibir()

    snap = Snapshot("Backup inicial", pessoas, produtos, pagamentos)
    print(f"\n{snap}")

    if GerenciadorArquivo.salvar(snap, "data/dados_cantina.pkl"):
        print("Dados salvos com sucesso.")

    print("\n" + "=" * 72)
    print("Simulando reinicio do sistema - carregando dados do disco...")
    print("=" * 72)

    dados = GerenciadorArquivo.carregar("data/dados_cantina.pkl")

    if dados:
        print(f"\nSnapshot recuperado: {dados}")
        dados.get_pessoas().exibir()
        dados.get_produtos().exibir()
        dados.get_pagamentos().exibir()

    print("\nGerando segundo snapshot com novos produtos...")
    novos_produtos = gerar_produtos(3)
    novos_pagamentos = gerar_pagamentos(pessoas, novos_produtos, 4)

    snap2 = Snapshot("Segundo turno", pessoas, novos_produtos, novos_pagamentos)

    if GerenciadorArquivo.salvar(snap2, "data/dados_cantina_v2.pkl"):
        print("Segundo snapshot salvo com sucesso.")

    dados2 = GerenciadorArquivo.carregar("data/dados_cantina_v2.pkl")

    if dados2:
        print(f"\nSegundo snapshot recuperado: {dados2}")
        dados2.get_produtos().exibir()
        dados2.get_pagamentos().exibir()