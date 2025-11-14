# Classe Eletronico

from produto import Produto

class Eletronico(Produto):
    def __init__(self, nome: str, preco: float, estoque: int, garantia_meses: int):
        super().__init__(nome, preco, estoque)
        self.garantia_meses = garantia_meses

    # Sobrescreve aplicar_desconto com regra baseada na garantia
    def aplicar_desconto(self, percentual=None):
        preco = self.get_preco()
        if self.garantia_meses > 12:
            return preco - (preco * 0.05)
        else:
            return preco - (preco * 0.02)

    # Método exclusivo: estender garantia
    def estender_garantia(self, meses: int):
        if meses <= 0:
            raise ValueError("Meses deve ser positivo.")
        self.garantia_meses += meses
        print(f"Garantia estendida. Novo prazo: {self.garantia_meses} meses.")
        