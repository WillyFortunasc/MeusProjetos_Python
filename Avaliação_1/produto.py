# Classe base Produto

class Produto:
    def __init__(self, nome: str, preco: float, estoque: int):
        self.nome = nome  # atributo público
        self.__preco = None   # atributo privado (encapsulamento)
        self.__estoque = None
        # Uso dos setters para validar os valores
        self.set_preco(preco)
        self.set_estoque(estoque)

    # Getter e setter de preco (acessam o atributo privado __preco)
    def get_preco(self):
        return self.__preco

    def set_preco(self, novo_preco):
        if not isinstance(novo_preco, (int, float)):
            raise ValueError("Preço deve ser numérico.")
        if novo_preco < 0:
            raise ValueError("Preço não pode ser negativo.")
        self.__preco = float(novo_preco)

    # Getter e setter de estoque (acessam o atributo privado __estoque)
    def get_estoque(self):
        return self.__estoque

    def set_estoque(self, novo_estoque):
        if not isinstance(novo_estoque, int):
            raise ValueError("Estoque deve ser inteiro.")
        if novo_estoque < 0:
            raise ValueError("Estoque não pode ser negativo.")
        self.__estoque = novo_estoque

    # Exibir informações básicas do produto
    def exibir_info(self):
        print(f"Produto: {self.nome}, Preço: R${self.get_preco():.2f}, Estoque: {self.get_estoque()}")

    # Método para aplicar desconto genérico
    def aplicar_desconto(self, percentual=0.0):
        if percentual < 0 or percentual > 100:
            raise ValueError("Percentual inválido.")
        desconto = self.get_preco() * (percentual / 100.0)
        return self.get_preco() - desconto