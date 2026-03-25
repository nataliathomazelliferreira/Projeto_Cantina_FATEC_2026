
# QUESTÃO 1

class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.data_vencimento = data_vencimento
        self.quantidade = quantidade

    def __str__(self):
        return (f"Produto: {self.nome} | "
                f"Compra: R${self.preco_compra:.2f} | "
                f"Venda: R${self.preco_venda:.2f} | "
                f"Comprado em: {self.data_compra} | "
                f"Vence em: {self.data_vencimento} | "
                f"Qtd: {self.quantidade}")

class No:
    def __init__(self, produto):
        self.produto = produto
        self.proximo = None

class ListaEstoque:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0

    def _converter_data(self, data_str):
        partes = data_str.split("/")
        return (int(partes[2]), int(partes[1]), int(partes[0]))
 
    def inserir_ordenado(self, produto):
        novo_no = No(produto)
        data_novo = self._converter_data(produto.data_vencimento)

        if self.cabeca is None:
            self.cabeca = novo_no
            self.tamanho += 1
            return

        data_cabeca = self._converter_data(self.cabeca.produto.data_vencimento)
        if data_novo < data_cabeca:
            novo_no.proximo = self.cabeca  
            self.cabeca = novo_no          
            self.tamanho += 1
            return

        atual = self.cabeca 
        while atual.proximo is not None:
            data_proximo = self._converter_data(atual.proximo.produto.data_vencimento)

            if data_novo < data_proximo:
                novo_no.proximo = atual.proximo 
                atual.proximo = novo_no          
                self.tamanho += 1
                return

            atual = atual.proximo

        atual.proximo = novo_no
        self.tamanho += 1

    def buscar(self, nome):
        atual = self.cabeca 

        while atual is not None:  
            if atual.produto.nome.lower() == nome.lower():
                return atual 
            atual = atual.proximo

        return None

    def atualizar_quantidade(self, nome, nova_quantidade):
        no = self.buscar(nome)  

        if no is not None: 
            no.produto.quantidade = nova_quantidade  
            print(f"✅ Quantidade de '{nome}' atualizada para {nova_quantidade}.")
        else:
            print(f"❌ Produto '{nome}' não encontrado no estoque.")

    def dar_baixa(self, nome, quantidade_vendida):
        no = self.buscar(nome)  

        if no is None:
            print(f"❌ Produto '{nome}' não encontrado.")
            return False

        if no.produto.quantidade < quantidade_vendida:
            print(f"⚠️  Estoque insuficiente para '{nome}'. Disponível: {no.produto.quantidade}")
            return False

        no.produto.quantidade -= quantidade_vendida
        print(f"✅ Baixa de {quantidade_vendida} unidade(s) de '{nome}'. Restam: {no.produto.quantidade}")
        return True

    def exibir(self):
        print("\n📦 ESTOQUE ATUAL (ordem de prioridade — vence primeiro, vende primeiro):")
        print("-" * 75)

        if self.cabeca is None:  
            print("   Estoque vazio.")
            return

        atual = self.cabeca 
        posicao = 1         

        while atual is not None:  
            print(f"  [{posicao}] {atual.produto}")  
            atual = atual.proximo                    
            posicao += 1

        print("-" * 75)
        print(f"  Total de produtos cadastrados: {self.tamanho}")

if __name__ == "__main__":

    print("=" * 75)
    print("         QUESTÃO 1 – CONTROLE DE ESTOQUE – CANTINA FATEC")
    print("=" * 75)

    p1 = Produto("Água com gás do Orlando", 2.50, 3.50, "13/03/2026", "25/03/2027", 12)
    p2 = Produto("Coca 200ml",              2.00, 3.00, "13/03/2026", "22/03/2027", 12)
    p3 = Produto("Coca Zero 200ml",         2.00, 3.00, "13/03/2026", "22/03/2027", 12)
    p4 = Produto("Água normal",             2.00, 3.00, "13/03/2026", "28/03/2027", 12)
    p5 = Produto("Amendoim",                2.00, 3.00, "12/03/2026", "10/04/2027",  6)
    p6 = Produto("Torcida",                 2.00, 3.00, "12/03/2026", "05/04/2027", 10)
    p7 = Produto("Bonbon",                  1.00, 1.50, "10/03/2026", "30/12/2026", 40)
    p8 = Produto("Pão de Mel Bauduco",      2.00, 3.00, "11/03/2026", "20/12/2026", 12)

    estoque = ListaEstoque()

    estoque.inserir_ordenado(p1)
    estoque.inserir_ordenado(p2)
    estoque.inserir_ordenado(p3)
    estoque.inserir_ordenado(p4)
    estoque.inserir_ordenado(p5)
    estoque.inserir_ordenado(p6)
    estoque.inserir_ordenado(p7)
    estoque.inserir_ordenado(p8)

    estoque.exibir()

    print("\n🛒 Simulando venda de 3x Bonbon...")
    estoque.dar_baixa("Bonbon", 3)

    print("\n✏️  Atualizando quantidade de Amendoim para 20...")
    estoque.atualizar_quantidade("Amendoim", 20)

    print("\n🛒 Tentando vender 100x Torcida (mais do que existe)...")
    estoque.dar_baixa("Torcida", 100)

    estoque.exibir()