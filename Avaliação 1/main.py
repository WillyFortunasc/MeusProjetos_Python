# Arquivo principal

from livro import Livro
from eletronico import Eletronico
from carrinho import CarrinhoCompras

print("=== Teste da Avaliação ===")

# Criando produtos
livro1 = Livro("Pedagogia do oprimido", 80.0, 3, "Paulo Freire")
ele1 = Eletronico("Caixa de som Pro", 199.90, 2, 6)
ele2 = Eletronico("Laptop Ultra", 4500.0, 1, 24)

# Criando carrinho
carrinho = CarrinhoCompras()

# Adicionando itens (o estoque do produto é atualizado automaticamente)
carrinho.adicionar_item(livro1, 2)
carrinho.adicionar_item(ele1, 1)
carrinho.adicionar_item(ele2, 1)

# Listando itens do carrinho
print("\nItens no carrinho:")
carrinho.listar_itens()

# Calculando total detalhado
print("\nTotal detalhado com descontos aplicados:")
carrinho.calcular_total(detalhado=True)

# Testando métodos extras
print("\nResumo do livro:")
livro1.resumo()

print("\nEstendendo garantia do eletrônico:")
ele1.estender_garantia(12)