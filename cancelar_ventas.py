from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton

from clases.ventas_dao import VentasDAO


def load_ventas_cancelar():
    return VentasDAO.seleccionar_ventas()

def widgets_ventas_cancelar(callback):
    widgets = []
    for venta in load_ventas_cancelar():
        widgets.append(crear_widget(venta.id_venta, venta.total, venta.fecha, venta.nro_recibo ,callback))
    return widgets

def crear_widget(id, precio, fecha, recibo, callback):
    widget = QWidget()
    boton_detalle = QPushButton()
    boton_detalle.setText('Detalle')
    boton_detalle.clicked.connect(lambda: callback(id))
    layout = QHBoxLayout(widget)
    layout.addWidget(QLabel(str(recibo)))
    layout.addWidget(QLabel(f'${precio:,.2f}'))
    layout.addWidget(QLabel(str(fecha)))
    layout.addWidget(boton_detalle)
    return widget

if __name__ == '__main__':
    widgets_ventas_cancelar(1)
