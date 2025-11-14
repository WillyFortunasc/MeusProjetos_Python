from database import Database
from models import Pedido, ItemPedido
from control import PedidoControl

if __name__ == "__main__":
    db = Database(host='localhost', user='root', password='', database='db_pedidos')
    control = PedidoControl(db)

    # 1. Inserção
    pedido = Pedido(cliente="Claudio Ulisse")
    item1 = ItemPedido(produto="Teclado", quantidade=2, preco=150.00, categoria="Periféricos")
    item2 = ItemPedido(produto="Mouse", quantidade=1, preco=80.00, categoria="Periféricos")
    pedido.add_item(item1)
    pedido.add_item(item2)
    control.salvar_pedido(pedido)
    print(f"Pedido inserido com ID: {pedido.id}")

    # 2. Atualização
    pedido.cliente = "Claudio U."
    control.atualizar_pedido(pedido)
    print(f"Pedido atualizado com ID: {pedido.id}")

    # 3. Listagem
    pedidos = control.listar_pedidos_com_itens()
    for p in pedidos:
        print(f"Pedido {p.id} - Cliente: {p.cliente}")
        for i in p.itens:
            print(f"  Produto: {i.produto}, Quantidade: {i.quantidade}, Preço: {i.preco}, Categoria: {i.categoria}")

    # 4. Deleção
    control.deletar_pedido(pedido.id)
    print(f"Pedido deletado com ID: {pedido.id}")

    db.close()
