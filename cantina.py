from controle_venda import Venda
from controle_produto import Produto
from controle_estoque import Estoque
from datetime import datetime

# Criando o estoque
estoque = Estoque()

# Criando produtos
produtos = [
    Produto("Água com gás do Orlando", 2.50, 3.50, "13/03/2026", "25/03/2026", 12),
    Produto("Coca 200ml", 2.00, 3.00, "13/03/2026", "22/03/2026", 12),
    Produto("Coca Zero 200ml", 2.00, 3.00, "13/03/2026", "22/03/2026", 12),
    Produto("Água normal", 2.00, 3.00, "13/03/2026", "28/03/2026", 12),
    Produto("Amendoim", 2.00, 3.00, "12/03/2026", "10/04/2026", 6),
    Produto("Torcida", 2.00, 3.00, "12/03/2026", "05/04/2026", 10),
    Produto("Bonbon", 1.00, 1.50, "10/03/2026", "30/05/2026", 40),
    Produto("Pão de Mel Bauduco", 2.00, 3.00, "11/03/2026", "20/04/2026", 12)
]

# Adicionando no estoque
for p in produtos:
    estoque.adicionar_produto(p)

# Mostrar produtos
print("Estoque inicial:")
estoque.mostrar_produtos()

# Criando o objeto venda
venda = Venda()

# Simular uma venda
venda.realizar_venda(
    estoque,
    "Coca 200ml",
    "João",
    "Aluno",
    "IA"
)

# Mostrar estoque após venda
print("\nApós venda:")
estoque.mostrar_produtos()