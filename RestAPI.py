from flask import Flask, jsonify, request
from GestionPedidos import GestionPedidos

app = Flask(__name__)
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
