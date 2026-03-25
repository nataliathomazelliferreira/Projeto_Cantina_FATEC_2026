#QUESTÃO 2
from datetime import datetime

class Pessoa:
    def __init__(self, nome, categoria, curso):
        self.nome = nome
        self.categoria = categoria
        self.curso = curso

    def __str__(self):
        return f"{self.nome} ({self.categoria} – {self.curso})"


class Pagamento:
    def __init__(self, pessoa, valor):
        self.pessoa = pessoa
        self._valor = valor
        self.data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def get_valor(self):
        return self._valor

    def __str__(self):
        return (f"👤 {self.pessoa} | "
                f"💰 R${self._valor:.2f} | "
                f"🕐 {self.data_hora}")


class NoPilha:
    def __init__(self, pagamento):
        self.pagamento = pagamento
        self.abaixo = None


class PilhaPagamentos:
    def __init__(self):
        self.topo = None
        self.tamanho = 0
        self.total_arrecadado = 0.0

    def empilhar(self, pagamento):
        novo_no = NoPilha(pagamento)
        novo_no.abaixo = self.topo
        self.topo = novo_no
        self.tamanho += 1
        self.total_arrecadado += pagamento.get_valor()
        print(f"✅ Pagamento registrado: {pagamento}")

    def desempilhar(self):
        if self.topo is None:
            print("⚠️ Nenhum pagamento registrado.")
            return None

        pagamento_removido = self.topo.pagamento
        self.topo = self.topo.abaixo
        self.tamanho -= 1
        self.total_arrecadado -= pagamento_removido.get_valor()

        print(f"↩️ Pagamento removido: {pagamento_removido}")
        return pagamento_removido

    def espiar(self):
        if self.topo is None:
            print("⚠️ Pilha vazia.")
            return None

        return self.topo.pagamento

    def exibir(self):
        print("\n💳 REGISTROS DE PAGAMENTO (mais recente primeiro):")
        print("-" * 70)

        if self.topo is None:
            print("Nenhum pagamento registrado.")
            return

        atual = self.topo
        posicao = 1

        while atual is not None:
            print(f"[{posicao}] {atual.pagamento}")
            atual = atual.abaixo
            posicao += 1

        print("-" * 70)
        print(f"Total de pagamentos: {self.tamanho}")
        print(f"Total arrecadado: R${self.total_arrecadado:.2f}")


if __name__ == "__main__":

    print("=" * 70)
    print("QUESTÃO 2 – CONTROLE DE PAGAMENTO")
    print("=" * 70)

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

    pilha.empilhar(pag1)
    pilha.empilhar(pag2)
    pilha.empilhar(pag3)
    pilha.empilhar(pag4)
    pilha.empilhar(pag5)

    pilha.exibir()

    print(f"\nÚltimo pagamento: {pilha.espiar()}")

    pilha.desempilhar()

    pilha.exibir()