from flask import Flask, jsonify, request
from pedido_service import PedidoService

app = Flask(__name__)
pedido_service = PedidoService()

@app.route('/pedidos', methods=['GET'])
def get_pedidos():
    pedidos = pedido_service.get_all_pedidos()
    return jsonify(pedidos)

@app.route('/pedidos', methods=['POST'])
def crear_pedido():
    data = request.json
    cliente = data.get('cliente')
    productos = data.get('productos')
    nuevo_pedido = pedido_service.crear_pedido(cliente, productos)
    return jsonify(nuevo_pedido), 201

@app.route('/pedidos/<int:id>', methods=['PUT'])
def actualizar_pedido(id):
    data = request.json
    cliente = data.get('cliente')
    productos = data.get('productos')
    pedido_actualizado = pedido_service.actualizar_pedido(id, cliente, productos)
    if not pedido_actualizado:
        return jsonify({"mensaje": "Pedido no encontrado"}), 404
    return jsonify(pedido_actualizado)

@app.route('/pedidos/<int:id>', methods=['DELETE'])
def cancelar_pedido(id):
    cancelado = pedido_service.cancelar_pedido(id)
    if not cancelado:
        return jsonify({"mensaje": "Pedido no encontrado"}), 404
    return jsonify({"mensaje": "Pedido cancelado"})

if __name__ == '__main__':
    app.run(debug=True)
