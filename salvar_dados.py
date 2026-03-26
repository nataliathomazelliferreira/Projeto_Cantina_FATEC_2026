import pickle  # para salvar e carregar objetos Python em arquivos
import os      # para manipulação de arquivos e pastas
from datetime import datetime  # para registrar a data e hora de criação

from gerador_dados import (
    gerar_pessoas,   # função que gera dados de pessoas
    gerar_produtos,  # função que gera dados de produtos
    gerar_pagamentos, # função que gera dados de pagamentos
)

# Classe que representa um snapshot do estado atual da cantina
class Snapshot:
    def __init__(self, descricao, pessoas, produtos, pagamentos):
        self.__descricao = descricao  # descrição do snapshot (ex: "Backup inicial")
        self.__criado_em = datetime.now()  # data e hora de criação
        self.__pessoas = pessoas          # objeto com dados das pessoas
        self.__produtos = produtos        # objeto com dados dos produtos
        self.__pagamentos = pagamentos    # objeto com dados dos pagamentos

    # Métodos de acesso para cada atributo privado
    def get_descricao(self): return self.__descricao
    def get_criado_em(self): return self.__criado_em
    def get_pessoas(self): return self.__pessoas
    def get_produtos(self): return self.__produtos
    def get_pagamentos(self): return self.__pagamentos

    # Representação em string do snapshot para exibição
    def __str__(self):
        return f"[Snapshot] {self.__descricao} | Criado em: {self.__criado_em.strftime('%d/%m/%Y %H:%M:%S')}"

# Classe que gerencia a persistência de objetos em arquivos
class GerenciadorArquivo:
    @staticmethod
    def salvar(obj, caminho):
        try:
            # Cria a pasta se ela não existir
            pasta = os.path.dirname(caminho)
            if pasta and not os.path.exists(pasta):
                os.makedirs(pasta)

            # Salva o objeto em arquivo binário usando pickle
            with open(caminho, "wb") as f:
                pickle.dump(obj, f)
            return True
        except (OSError, pickle.PicklingError):
            return False  # retorna False se houver erro ao salvar

    @staticmethod
    def carregar(caminho):
        if not os.path.exists(caminho):
            return None  # retorna None se o arquivo não existir
        try:
            # Carrega o objeto do arquivo usando pickle
            with open(caminho, "rb") as f:
                return pickle.load(f)
        except (OSError, pickle.UnpicklingError):
            return None  # retorna None se houver erro ao carregar

# Código principal executado quando o arquivo é rodado
if __name__ == "__main__":

    print("=" * 72)
    print("QUESTAO 5 - PERSISTENCIA DE DADOS - CANTINA FATEC")
    print("=" * 72)

    print("\nGerando dados via Questao 4...")
    # Gerando dados simulados
    pessoas = gerar_pessoas(5)       # 5 pessoas
    produtos = gerar_produtos(5)     # 5 produtos
    pagamentos = gerar_pagamentos(pessoas, produtos, 8)  # 8 pagamentos

    # Exibindo os dados
    pessoas.exibir()
    produtos.exibir()
    pagamentos.exibir()

    # Criando o primeiro snapshot
    snap = Snapshot("Backup inicial", pessoas, produtos, pagamentos)
    print(f"\n{snap}")

    # Salvando o snapshot em arquivo
    if GerenciadorArquivo.salvar(snap, "data/dados_cantina.pkl"):
        print("Dados salvos com sucesso.")

    print("\n" + "=" * 72)
    print("Simulando reinicio do sistema - carregando dados do disco...")
    print("=" * 72)

    # Carregando os dados do arquivo
    dados = GerenciadorArquivo.carregar("data/dados_cantina.pkl")

    if dados:
        print(f"\nSnapshot recuperado: {dados}")
        # Exibindo os dados recuperados
        dados.get_pessoas().exibir()
        dados.get_produtos().exibir()
        dados.get_pagamentos().exibir()

    print("\nGerando segundo snapshot com novos produtos...")
    # Criando novos produtos e pagamentos
    novos_produtos = gerar_produtos(3)
    novos_pagamentos = gerar_pagamentos(pessoas, novos_produtos, 4)

    # Criando o segundo snapshot
    snap2 = Snapshot("Segundo turno", pessoas, novos_produtos, novos_pagamentos)

    # Salvando o segundo snapshot
    if GerenciadorArquivo.salvar(snap2, "data/dados_cantina_v2.pkl"):
        print("Segundo snapshot salvo com sucesso.")

    # Carregando o segundo snapshot
    dados2 = GerenciadorArquivo.carregar("data/dados_cantina_v2.pkl")

    if dados2:
        print(f"\nSegundo snapshot recuperado: {dados2}")
        dados2.get_produtos().exibir()
        dados2.get_pagamentos().exibir()