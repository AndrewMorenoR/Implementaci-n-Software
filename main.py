from flask import Flask
from GestionPedidos import GestionPedidos
from RestAPI import app as rest_app

app = Flask(__name__)
gestion_pedidos = GestionPedidos()

# Agregamos las rutas de la API REST
app.register_blueprint(rest_app)

from flask import Flask, jsonify, request

app = Flask(__name__)

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

gestion_pedidos = GestionPedidos()

@app.route('/pedidos', methods=['GET'])
def get_pedidos():
    return jsonify(gestion_pedidos.obtener_pedidos())

@app.route('/pedidos', methods=['POST'])
def crear_pedido():
    nuevo_pedido = request.json
    gestion_pedidos.crear_pedido(nuevo_pedido)
    return jsonify({"mensaje": "Pedido creado exitosamente"})

@app.route('/pedidos/<int:id_pedido>', methods=['GET'])
def get_pedido(id_pedido):
    pedido = gestion_pedidos.obtener_pedido_por_id(id_pedido)
    if pedido:
        return jsonify(pedido)
    else:
        return jsonify({"mensaje": "Pedido no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
