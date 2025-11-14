# Classe Livro

from produto import Produto

class Livro(Produto):
    def __init__(self, nome: str, preco: float, estoque: int, autor: str):
        # Chamando o construtor da classe pai (Produto)
        super().__init__(nome, preco, estoque)
        self.autor = autor

    # Sobrescreve aplicar_desconto para ter regra própria
    def aplicar_desconto(self, percentual=None):
        preco = self.get_preco()
        return preco - (preco * 0.10)  # sempre 10% de desconto

    # Método exclusivo de Livro
    def resumo(self):
        print(f"Resumo de {self.nome} por {self.autor}.")