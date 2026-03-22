from controle_produto import Produto
from controle_estoque import Estoque

# Criando o estoque
estoque = Estoque()

p1 = Produto("Água com gás do Orlando", 2.50, 3.50, "13/03/2026", "25/03/2026", 12)
p2 = Produto("Coca 200ml", 2.00, 3.00, "13/03/2026", "22/03/2026", 12)
p3 = Produto("Coca Zero 200ml", 2.00, 3.00, "13/03/2026", "22/03/2026", 12)
p4 = Produto("Água normal", 2.00, 3.00, "13/03/2026", "28/03/2026", 12)
p5 = Produto("Amendoim", 2.00, 3.00, "12/03/2026", "10/04/2026", 6)
p6 = Produto("Torcida", 2.00, 3.00, "12/03/2026", "05/04/2026", 10)
p7 = Produto("Bonbon", 1.00, 1.50, "10/03/2026", "30/05/2026", 40)
p8 = Produto("Pão de Mel Bauduco", 2.00, 3.00, "11/03/2026", "20/04/2026", 12)

# Adicionando no estoque
estoque.adicionar_produto(p1)
estoque.adicionar_produto(p2)
estoque.adicionar_produto(p3)
estoque.adicionar_produto(p4)
estoque.adicionar_produto(p5)
estoque.adicionar_produto(p6)
estoque.adicionar_produto(p7)
estoque.adicionar_produto(p8)

# Mostrar produtos
estoque.mostrar_produtos()

# Simular venda
estoque.vender_produto("Coca 200ml")

# Mostrar novamente
print("\nApós venda:")
estoque.mostrar_produtos()