class GestionPedidos:
    def __init__(self):
        self.pedidos = []

    def obtener_pedidos(self):
        return self.pedidos

    def crear_pedido(self, nuevo_pedido):
        self.pedidos.append(nuevo_pedido)

    def obtener_pedido_por_id(self, id_pedido):
        for pedido in self.pedidos:
            if pedido['id'] == id_pedido:
                return pedido
        return None
