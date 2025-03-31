from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton


def load_ventas_cancelar():
    return [(1, 150250, '17:20','10/12/2025'),
            (2, 150250, '17:20','10/12/2025'),
            (3, 150250, '17:20','10/12/2025'),
            (4, 150250, '17:20','10/12/2025'),
            (5, 150250, '17:20','10/12/2025'),
            (6, 150250, '17:20','10/12/2025'),
            (7, 150250, '17:20','10/12/2025')]

def widgets_ventas_cancelar(callback):
    widgets = []
    for id, precio, hora, fecha in load_ventas_cancelar():
        widgets.append(crear_widget(id,precio, hora, fecha, callback))
    return widgets

def crear_widget(id, precio, hora, fecha, callback):
    widget = QWidget()
    boton_detalle = QPushButton()
    boton_detalle.setText('Detalle')
    boton_detalle.clicked.connect(lambda: callback(id))
    layout = QHBoxLayout(widget)
    layout.addWidget(QLabel(str(id)))
    layout.addWidget(QLabel(str(precio)))
    layout.addWidget(QLabel(hora))
    layout.addWidget(QLabel(fecha))
    layout.addWidget(boton_detalle)
    return widget
