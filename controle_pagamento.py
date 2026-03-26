#questão 2
from datetime import datetime


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


class Pagamento:
    def __init__(self, pessoa, valor):
        if not isinstance(pessoa, Pessoa):
            raise TypeError("pessoa deve ser instancia de Pessoa.")
        if valor <= 0:
            raise ValueError("Valor do pagamento deve ser positivo.")

        self.__pessoa = pessoa
        self.__valor = valor
        self.__data_hora = datetime.now() 

    def get_pessoa(self): return self.__pessoa
    def get_valor(self): return self.__valor
    def get_data_hora(self): return self.__data_hora

    def __str__(self):
        data_formatada = self.__data_hora.strftime("%d/%m/%Y %H:%M:%S")
        return f"{self.__pessoa} | R${self.__valor:.2f} | {data_formatada}"


class _NoPilha:
    def __init__(self, pagamento):
        self.pagamento = pagamento
        self.abaixo = None


class PilhaPagamentos:
    def __init__(self):
        self.__topo = None
        self.__tamanho = 0
        self.__total_arrecadado = 0.0

    def empilhar(self, pagamento):
        if not isinstance(pagamento, Pagamento):
            raise TypeError("Apenas objetos Pagamento podem ser empilhados.")

        novo_no = _NoPilha(pagamento)
        novo_no.abaixo = self.__topo
        self.__topo = novo_no
        self.__tamanho += 1
        self.__total_arrecadado += pagamento.get_valor()

        return True  

    def desempilhar(self):
        if self.__topo is None:
            return None

        pagamento_removido = self.__topo.pagamento
        self.__topo = self.__topo.abaixo
        self.__tamanho -= 1
        self.__total_arrecadado -= pagamento_removido.get_valor()

        return pagamento_removido  

    def espiar(self):
        if self.__topo is None:
            return None
        return self.__topo.pagamento

    def get_tamanho(self): return self.__tamanho
    def get_total_arrecadado(self): return self.__total_arrecadado

    def exibir(self):
        dados = []

        atual = self.__topo
        while atual is not None:
            dados.append(atual.pagamento)
            atual = atual.abaixo

        return dados  


if __name__ == "__main__":

    print("=" * 72)
    print("QUESTAO 2 - CONTROLE DE PAGAMENTO")
    print("=" * 72)

    pessoa1 = Pessoa("Vladimir", "aluno", "IA")
    pessoa2 = Pessoa("Orlando The Best", "professor", "ESG")
    pessoa3 = Pessoa("Debora", "aluno", "IA")
    pessoa4 = Pessoa("Natalia", "aluno", "IA")
    pessoa5 = Pessoa("Luan", "servidor", "IA")

    pag1 = Pagamento(pessoa1, 3.00)
    pag2 = Pagamento(pessoa2, 1.50)
    pag3 = Pagamento(pessoa3, 6.00)
    pag4 = Pagamento(pessoa4, 3.50)
    pag5 = Pagamento(pessoa5, 3.00)

    pilha = PilhaPagamentos()

    for pag in [pag1, pag2, pag3, pag4, pag5]:
        pilha.empilhar(pag)
        print(f"Pagamento registrado: {pag}")

    print("\nREGISTROS DE PAGAMENTO (mais recente primeiro):")
    print("-" * 72)
    for i, pagamento in enumerate(pilha.exibir(), 1):
        print(f"[{i:02d}] {pagamento}")

    print("-" * 72)
    print(f"Total de pagamentos : {pilha.get_tamanho()}")
    print(f"Total arrecadado    : R${pilha.get_total_arrecadado():.2f}")

    print(f"\nUltimo pagamento (topo): {pilha.espiar()}")

    print("\nEstornando ultimo pagamento...")
    removido = pilha.desempilhar()
    if removido:
        print(f"Pagamento estornado: {removido}")

    print("\nAtualizado:")
    print("-" * 72)
    for i, pagamento in enumerate(pilha.exibir(), 1):
        print(f"[{i:02d}] {pagamento}")