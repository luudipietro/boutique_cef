from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QComboBox

from clases.ventas import DetalleVentaProducto
from clases.ventas_dao import VentasDAO


def detalle_venta(id):
    return VentasDAO.seleccionar_detalles_venta(id), VentasDAO.seleccionar_productos_combo_anidado(id)

def crear_items_detalle(id, callback):
    widgets = []
    detalle = detalle_venta(id)
    for venta in detalle[0]:
        widgets.append(crear_widget(venta.id_venta, venta.id_detalle_venta_producto, venta.id_producto, venta.nombre_producto, venta.id_talle,venta.talle, venta.precio_unitario, callback))
    return widgets

def crear_widget(id_venta, id_detalle_venta_prod,id_prod, nombre_prod, id_talle, talle, precio, callback):
    widget = QWidget()
    layout = QHBoxLayout(widget)
    img_label = QLabel()
    pixmap = QPixmap(f'img/{nombre_prod}.png').scaled(75, 75)
    img_label.setPixmap(pixmap)
    #combo_talle = QComboBox()
    #combo_talle.addItem(talle)
    #combo_talle.setCurrentText(talle)

    boton_cambiar = QPushButton()
    boton_cambiar.setText('Cambiar')
    boton_cambiar.clicked.connect(lambda: callback(id_prod, id_talle, DetalleVentaProducto(id_detalle_venta_prod, id_venta, id_prod, id_talle, precio, nombre_prod, talle)))
    #layout.addWidget(QLabel(str(id)))

    layout.addWidget(img_label)
    layout.addWidget(QLabel(str(nombre_prod)))
    layout.addWidget(QLabel(f'Talle: {talle}'))
    layout.addWidget(QLabel(str(precio)))
    layout.addWidget(boton_cambiar)

    return widget

