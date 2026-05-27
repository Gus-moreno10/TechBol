from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Pedido, Producto, Cliente

bp_pedidos = Blueprint('pedidos', __name__)

@bp_pedidos.route('/')
def index():
    pedidos = Pedido.query.all()
    return render_template('pedidos/index.html', pedidos=pedidos)

@bp_pedidos.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        producto_id = int(request.form.get('producto_id'))
        cliente_id = int(request.form.get('cliente_id'))
        monto = int(request.form.get('monto'))
        nuevo_pedido = Pedido(producto_id=producto_id, cliente_id=cliente_id, monto=monto)
        db.session.add(nuevo_pedido)
        db.session.commit()
        return redirect(url_for('pedidos.index'))
    productos = Producto.query.all()
    clientes = Cliente.query.all()
    return render_template('pedidos/nuevo.html', productos=productos, clientes=clientes)

@bp_pedidos.route('/eliminar/<int:id>')
def eliminar(id):
    pedido = Pedido.query.get_or_404(id)
    db.session.delete(pedido)
    db.session.commit()
    return redirect(url_for('pedidos.index'))
