from typing import List
from sqlalchemy.orm import Session
from pedidoEntity import PedidoEntity
from sqlalchemy import create_engine

class PedidoService:
    def __init__(self, db_connection_string: str):
        self.engine = create_engine(db_connection_string)
        self.session = Session(self.engine)

    def get_all_pedidos(self) -> List[PedidoEntity]:
        return self.session.query(PedidoEntity).all()

    def get_pedido_by_id(self, id: int) -> PedidoEntity:
        return self.session.query(PedidoEntity).filter_by(id=id).first()

    def crear_pedido(self, cliente: str, productos: List[dict]) -> PedidoEntity:
        nuevo_pedido = PedidoEntity(cliente=cliente, productos=productos)
        self.session.add(nuevo_pedido)
        self.session.commit()
        return nuevo_pedido

    def actualizar_pedido(self, id: int, cliente: str, productos: List[dict]) -> PedidoEntity:
        pedido = self.get_pedido_by_id(id)
        if pedido:
            pedido.cliente = cliente
            pedido.productos = productos
            self.session.commit()
            return pedido
        return None

    def cancelar_pedido(self, id: int) -> bool:
        pedido = self.get_pedido_by_id(id)
        if pedido:
            self.session.delete(pedido)
            self.session.commit()
            return True
        return False
