from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QComboBox, QSpinBox

from clases.produto_dao import ProductoDAO


def productos_modificar_cantidades():

    detalle = ProductoDAO.seleccionar_productos_venta()

    return detalle

def crear_items_modificar_cantidades():
    widgets = []
    for p in productos_modificar_cantidades():
        for t in p.talles:
            widgets.append(crear_widget_modificar_cantidades(p.id, p.nombre, t))
    return widgets

def crear_widget_modificar_cantidades(id, nombre, talle):
    widget = QWidget()
    layout = QHBoxLayout(widget)
    img_label = QLabel()
    pixmap = QPixmap(f'img/{nombre}.png').scaled(75, 75)
    img_label.setPixmap(pixmap)
    label_talle = QLabel(str(talle.talle))
    spn_cantidad_agregar = QSpinBox()
    spn_cantidad_agregar.setMinimum(1)
    boton_cambiar = QPushButton()
    boton_cambiar.setText('Agregar')
    #boton_cambiar.clicked.connect(pass)
    layout.addWidget(QLabel(str(id)))

    layout.addWidget(img_label)
    layout.addWidget(QLabel(str(nombre)))
    layout.addWidget(label_talle)
    layout.addWidget(QLabel(str(talle.stock)))
    layout.addWidget(spn_cantidad_agregar)
    layout.addWidget(boton_cambiar)
    return widget

