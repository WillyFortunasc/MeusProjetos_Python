# Classe CarrinhoCompras

from produto import Produto

class CarrinhoCompras:
    def __init__(self):
        self.itens = []  # lista de dicionários {"produto": Produto, "qtd": int}

    def adicionar_item(self, produto: Produto, qtd: int):
        if qtd <= 0:
            raise ValueError("Quantidade inválida.")
        if qtd > produto.get_estoque():
            raise ValueError("Quantidade maior que o estoque.")
        # reduz estoque do produto
        produto.set_estoque(produto.get_estoque() - qtd)
        # verifica se já existe no carrinho
        for item in self.itens:
            if item["produto"] is produto:
                item["qtd"] += qtd
                return
        # senão, adiciona novo
        self.itens.append({"produto": produto, "qtd": qtd})

    def remover_item(self, produto: Produto):
        for i, item in enumerate(self.itens):
            if item["produto"] is produto:
                # devolve estoque
                produto.set_estoque(produto.get_estoque() + item["qtd"])
                del self.itens[i]
                return
        raise ValueError("Produto não encontrado no carrinho.")

    def calcular_total(self, percentual_genérico=0.0, detalhado=False):
        total = 0
        for item in self.itens:
            preco = item["produto"].aplicar_desconto(percentual_genérico)
            subtotal = preco * item["qtd"]
            total += subtotal
            if detalhado:
                print(f"{item['produto'].nome}: {item['qtd']} x R${preco:.2f} = R${subtotal:.2f}")
        if detalhado:
            print(f"Total: R${total:.2f}")
        return total

    def listar_itens(self):
        if not self.itens:
            print("Carrinho vazio.")
        for item in self.itens:
            item["produto"].exibir_info()
            print(f"Quantidade: {item['qtd']}\n")
