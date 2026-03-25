# QUESTÃO 6

from datetime import datetime

class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_vencimento, quantidade):
        self.nome            = nome
        self.preco_compra    = preco_compra
        self.preco_venda     = preco_venda
        self.data_compra     = data_compra
        self.data_vencimento = data_vencimento
        self.quantidade      = quantidade   
        self.quantidade_inicial = quantidade 

    def __str__(self):
        return (f"{self.nome} | "
                f"Custo: R${self.preco_compra:.2f} | "
                f"Venda: R${self.preco_venda:.2f} | "
                f"Vence: {self.data_vencimento} | "
                f"Qtd atual: {self.quantidade}")


class ItemVenda:
    """Um produto dentro de uma venda."""
    def __init__(self, produto_nome, quantidade, preco_unitario, preco_custo):
        self.produto_nome   = produto_nome
        self.quantidade     = quantidade
        self.preco_unitario = preco_unitario 
        self.preco_custo    = preco_custo     

    @property
    def receita(self):
        return self.quantidade * self.preco_unitario  

    @property
    def custo(self):
        return self.quantidade * self.preco_custo 

    @property
    def lucro(self):
        return self.receita - self.custo         


class Venda:
    """Uma venda completa com cliente, itens e totais."""
    _contador = 0

    def __init__(self, nome_cliente, categoria):
        Venda._contador   += 1
        self.id            = Venda._contador
        self.nome_cliente  = nome_cliente
        self.categoria     = categoria
        self.data_hora     = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.cabeca_itens  = None  
        self.total_receita = 0.0
        self.total_custo   = 0.0

    def adicionar_item(self, item):
    
        class NoItem:
            def __init__(self, i):
                self.item = i
                self.proximo = None

        novo = NoItem(item)
        if self.cabeca_itens is None:
            self.cabeca_itens = novo
        else:
            atual = self.cabeca_itens
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo

    
        self.total_receita += item.receita
        self.total_custo   += item.custo

    @property
    def lucro_total(self):
        return self.total_receita - self.total_custo

class No:
    def __init__(self, dado):
        self.dado    = dado
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.cabeca  = None
        self.tamanho = 0

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

    def buscar_produto(self, nome):
   
        atual = self.cabeca
        while atual:
            if hasattr(atual.dado, 'nome') and atual.dado.nome.lower() == nome.lower():
                return atual.dado
            atual = atual.proximo
        return None

def separador(char="=", largura=65):
    """Imprime uma linha separadora."""
    print(char * largura)


def relatorio_estoque(lista_estoque):
    """
    Relatório de estoque atual.
    Mostra todos os produtos, suas quantidades e alertas de vencimento.
    """
    separador()
    print("           📦 RELATÓRIO DE ESTOQUE")
    separador()
    print(f"  {'Produto':<28} {'Vence':<14} {'Qtd':>5} {'Venda':>8} {'Custo':>8}")
    separador("-")

    hoje       = datetime.now()
    total_prod = 0    
    alertas    = []   

    atual = lista_estoque.cabeca 
    while atual:
        p = atual.dado   

        partes    = p.data_vencimento.split("/")
        dt_venc   = datetime(int(partes[2]), int(partes[1]), int(partes[0]))
        dias_rest = (dt_venc - hoje).days  

        alerta = "⚠️ " if dias_rest <= 30 else "  "

        print(f"  {alerta}{p.nome:<26} {p.data_vencimento:<14} "
              f"{p.quantidade:>5} R${p.preco_venda:>5.2f} R${p.preco_compra:>5.2f}")

        if dias_rest <= 30:
            alertas.append((p.nome, dias_rest))   

        total_prod += 1
        atual = atual.proximo   

    separador("-")
    print(f"  Total de produtos cadastrados: {total_prod}")

    if alertas:
        print(f"\n  ⚠️  PRODUTOS COM VENCIMENTO PRÓXIMO (≤ 30 dias):")
        for nome, dias in alertas:
            if dias < 0:
                print(f"     • {nome}: VENCIDO há {abs(dias)} dia(s)!")
            else:
                print(f"     • {nome}: vence em {dias} dia(s)")

    separador()


def relatorio_vendas(lista_vendas):
    """
    Relatório de todas as vendas realizadas.
    Mostra cada venda com seus itens, receita e lucro.
    """
    separador()
    print("           🧾 RELATÓRIO DE VENDAS")
    separador()

    if lista_vendas.cabeca is None:
        print("  Nenhuma venda registrada.")
        separador()
        return

    total_receita = 0.0 
    total_lucro   = 0.0  
    qtd_vendas    = 0     

    atual = lista_vendas.cabeca   
    while atual:
        v = atual.dado  

        print(f"\n  Venda #{v.id:02d} | {v.data_hora} | {v.nome_cliente} ({v.categoria})")
        print(f"  {'Produto':<28} {'Qtd':>4} {'Unit':>7} {'Subtotal':>9} {'Lucro':>8}")
        print("  " + "-" * 60)

        no_item = v.cabeca_itens
        while no_item:
            i = no_item.item
            print(f"  {i.produto_nome:<28} {i.quantidade:>4} "
                  f"R${i.preco_unitario:>5.2f} "
                  f"R${i.receita:>7.2f} "
                  f"R${i.lucro:>6.2f}")
            no_item = no_item.proximo

        print("  " + "-" * 60)
        print(f"  {'TOTAL DA VENDA':>43} R${v.total_receita:>7.2f} R${v.lucro_total:>6.2f}")

        total_receita += v.total_receita
        total_lucro   += v.lucro_total
        qtd_vendas    += 1

        atual = atual.proximo  

    separador("-")
    print(f"\n  Quantidade de vendas:  {qtd_vendas}")
    print(f"  Receita total:         R${total_receita:.2f}")
    print(f"  Lucro total:           R${total_lucro:.2f}")
    margem = (total_lucro / total_receita * 100) if total_receita > 0 else 0
    print(f"  Margem de lucro:       {margem:.1f}%")
    separador()


def relatorio_consumo(lista_vendas, lista_estoque):
    """
    Relatório de consumo por produto.
    Mostra quantas unidades de cada produto foram vendidas.
    Conceito: percorremos todas as vendas e acumulamos por produto
    usando uma lista encadeada de consumo.
    """
    separador()
    print("        📊 RELATÓRIO DE CONSUMO POR PRODUTO")
    separador()

    class NóConsumo:
        def __init__(self, nome):
            self.nome      = nome
            self.qtd_total = 0  
            self.receita   = 0.0    
            self.proximo   = None    

    cabeca_consumo = None

    def buscar_ou_criar(nome):
        
        nonlocal cabeca_consumo
        atual = cabeca_consumo
        while atual:
            if atual.nome == nome:
                return atual      
            atual = atual.proximo

        # Não encontrou: cria novo nó e insere no início
        novo = NóConsumo(nome)
        novo.proximo   = cabeca_consumo
        cabeca_consumo = novo
        return novo

    # Percorre todas as vendas e acumula o consumo por produto
    atual_venda = lista_vendas.cabeca
    while atual_venda:
        v = atual_venda.dado

        no_item = v.cabeca_itens
        while no_item:
            i     = no_item.item
            no_c  = buscar_ou_criar(i.produto_nome)   
            no_c.qtd_total += i.quantidade             
            no_c.receita   += i.receita                
            no_item         = no_item.proximo

        atual_venda = atual_venda.proximo

    # Exibe o relatório de consumo
    if cabeca_consumo is None:
        print("  Nenhum consumo registrado.")
        separador()
        return

    print(f"  {'Produto':<30} {'Qtd Vendida':>12} {'Receita':>10}")
    separador("-")

    total_unid    = 0
    total_receita = 0.0

    atual = cabeca_consumo
    while atual:
        print(f"  {atual.nome:<30} {atual.qtd_total:>12} R${atual.receita:>7.2f}")
        total_unid    += atual.qtd_total
        total_receita += atual.receita
        atual          = atual.proximo

    separador("-")
    print(f"  {'TOTAL':<30} {total_unid:>12} R${total_receita:>7.2f}")
    separador()


def relatorio_por_categoria(lista_vendas):
    """
    Relatório de gastos agrupados por categoria (aluno, professor, servidor).
    Mostra quanto cada grupo gastou na cantina.
    """
    separador()
    print("      💼 RELATÓRIO DE GASTOS POR CATEGORIA")
    separador()

    # Nó para acumular gastos por categoria (lista encadeada manual)
    class NóCategoria:
        def __init__(self, categoria):
            self.categoria  = categoria
            self.total      = 0.0
            self.qtd_vendas = 0
            self.proximo    = None

    cabeca_cat = None

    def buscar_ou_criar_cat(categoria):
        nonlocal cabeca_cat
        atual = cabeca_cat
        while atual:
            if atual.categoria == categoria:
                return atual
            atual = atual.proximo
        novo           = NóCategoria(categoria)
        novo.proximo   = cabeca_cat
        cabeca_cat     = novo
        return novo

    # Percorre as vendas e acumula por categoria
    atual = lista_vendas.cabeca
    while atual:
        v    = atual.dado
        no_c = buscar_ou_criar_cat(v.categoria)
        no_c.total      += v.total_receita
        no_c.qtd_vendas += 1
        atual            = atual.proximo

    print(f"  {'Categoria':<15} {'Qtd Vendas':>12} {'Total Gasto':>13}")
    separador("-")

    atual = cabeca_cat
    while atual:
        print(f"  {atual.categoria:<15} {atual.qtd_vendas:>12} R${atual.total:>10.2f}")
        atual = atual.proximo

    separador()

if __name__ == "__main__":

    print("=" * 65)
    print("         QUESTÃO 6 – RELATÓRIOS – CANTINA FATEC")
    print("=" * 65)

    # --- Montando o estoque com os produtos reais ---
    estoque = ListaEncadeada()
    p1 = Produto("Água com gás do Orlando", 2.50, 3.50, "13/03/2026", "25/03/2027", 12)
    p2 = Produto("Coca 200ml",              2.00, 3.00, "13/03/2026", "22/03/2027", 12)
    p3 = Produto("Coca Zero 200ml",         2.00, 3.00, "13/03/2026", "22/03/2027", 12)
    p4 = Produto("Água normal",             2.00, 3.00, "13/03/2026", "28/03/2027", 12)
    p5 = Produto("Amendoim",                2.00, 3.00, "12/03/2026", "10/04/2027",  6)
    p6 = Produto("Torcida",                 2.00, 3.00, "12/03/2026", "05/04/2027", 10)
    p7 = Produto("Bonbon",                  1.00, 1.50, "10/03/2026", "30/12/2026", 40)
    p8 = Produto("Pão de Mel Bauduco",      2.00, 3.00, "11/03/2026", "20/12/2026", 12)

    for p in [p1, p2, p3, p4, p5, p6, p7, p8]:
        estoque.adicionar(p)

    # --- Simulando vendas ---
    vendas = ListaEncadeada()

    
    v1 = Venda("Vladimir", "aluno")
    v1.adicionar_item(ItemVenda("Coca 200ml",         1, 3.00, 2.00))
    v1.adicionar_item(ItemVenda("Bonbon",             2, 1.50, 1.00))
    vendas.adicionar(v1)

    v2 = Venda("Prof. Orlando The Best", "professor")
    v2.adicionar_item(ItemVenda("Água com gás do Orlando", 1, 3.50, 2.50))
    v2.adicionar_item(ItemVenda("Pão de Mel Bauduco",      1, 3.00, 2.00))
    vendas.adicionar(v2)

    v3 = Venda("Debora", "aluno")
    v3.adicionar_item(ItemVenda("Amendoim",  3, 3.00, 2.00))
    v3.adicionar_item(ItemVenda("Torcida",   1, 3.00, 2.00))
    vendas.adicionar(v3)

    v4 = Venda("Luan", "servidor")
    v4.adicionar_item(ItemVenda("Coca Zero 200ml", 2, 3.00, 2.00))
    v4.adicionar_item(ItemVenda("Bonbon",          3, 1.50, 1.00))
    vendas.adicionar(v4)

    v5 = Venda("Natalia", "aluno")
    v5.adicionar_item(ItemVenda("Água normal",        1, 3.00, 2.00))
    v5.adicionar_item(ItemVenda("Pão de Mel Bauduco", 2, 3.00, 2.00))
    vendas.adicionar(v5)

    print()
    relatorio_estoque(estoque)

    print()
    relatorio_vendas(vendas)

    print()
    relatorio_consumo(vendas, estoque)

    print()
    relatorio_por_categoria(vendas)