from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QComboBox


def productos_modificar_cantidades(id):

    detalle = [(1, 'Camiseta de Juego', 'camiseta_cef.jpg', 'S', 1),
               (1, 'Camiseta de Juego', 'camiseta_cef.jpg', 'L', 1),
               (1, 'Camiseta de Juego', 'camiseta_cef.jpg', 'M', 1)]
    return detalle

def crear_items_modificar_cantidades(id):
    widgets = []
    for id, nombre, imagen, talle, cantidad in productos_modificar_cantidades(id):
        widgets.append(crear_widget_modificar_cantidades(id, nombre, imagen, talle, cantidad))
    return widgets

def crear_widget_modificar_cantidades(id, nombre, imagen, talle, cantidad):
    widget = QWidget()
    layout = QHBoxLayout(widget)
    img_label = QLabel()
    pixmap = QPixmap(f'../img/{imagen}').scaled(75, 75)
    img_label.setPixmap(pixmap)
    combo_talle = QComboBox()
    combo_talle.addItems(['S','M','L'])
    combo_talle.setCurrentText(talle)

    boton_cambiar = QPushButton()
    boton_cambiar.setText('Cambiar')
    #boton_cambiar.clicked.connect(pass)
    layout.addWidget(QLabel(str(id)))
    layout.addWidget(QLabel(str(nombre)))
    layout.addWidget(img_label)
    layout.addWidget(combo_talle)
    layout.addWidget(QLabel(str(cantidad)))
    layout.addWidget(boton_cambiar)
    return widget

