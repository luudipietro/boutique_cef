from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton


def load_ventas_del_dia():
    return [(1, 150250, '17:20','Efectivo'),
            (2, 150250, '17:20','Efectivo'),
            (3, 150250, '17:20','Efectivo'),
            (4, 150250, '17:20','Efectivo'),
            (5, 150250, '17:20','Efectivo'),
            (6, 150250, '17:20','Efectivo'),
            (7, 150250, '17:20','Efectivo')]

def widgets_ventas_del_dia():
    widgets = []
    total = 0
    efectivo = 0
    transferencia = 0
    tarjeta = 0
    for id, monto, hora, metodo_pago in load_ventas_del_dia():

        total += monto
        if metodo_pago == 'Efectivo':
            efectivo += monto
        elif metodo_pago == 'Transferencia':
            transferencia += monto
        else:
            tarjeta += monto

        widgets.append(crear_widget(id,monto, hora, metodo_pago))

    return widgets, total, efectivo,tarjeta,transferencia

def crear_widget(id, monto, hora, metodo_pago):
    widget = QWidget()
    monto = f'${monto}'
    layout = QHBoxLayout(widget)
    layout.addWidget(QLabel(str(id)))
    layout.addWidget(QLabel(monto))
    layout.addWidget(QLabel(hora))
    layout.addWidget(QLabel(metodo_pago))
    return widget
