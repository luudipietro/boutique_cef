from datetime import  datetime

from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton

from clases.ventas_dao import VentasDAO


def load_ventas_del_dia(fecha):
    ventas = VentasDAO.seleccionar_ventas_fecha(fecha)
    return ventas

def widgets_ventas_del_dia(fecha):
    widgets = []
    total = 0
    efectivo = 0
    transferencia = 0
    tarjeta = 0

    ventas = load_ventas_del_dia(fecha)
    if len(ventas) == 0:
        return False
    else:
        for venta in ventas :
            total += venta.total
            if venta.metodo_pago == 'Efectivo':
                efectivo += venta.total
            elif venta.metodo_pago == 'Transferencia':
                transferencia += venta.total
            else:
                tarjeta += venta.total
            widget = crear_widget(venta.id_venta, venta.total, venta.metodo_pago, venta.nro_recibo, venta.id_cliente)
            widgets.append(widget)

        return widgets, total, efectivo,tarjeta,transferencia

def crear_widget(id, monto, metodo_pago, nro_recibo, cliente):
    widget = QWidget()
    monto = f'${monto}'
    layout = QHBoxLayout(widget)
    layout.addWidget(QLabel(str(nro_recibo)))
    layout.addWidget(QLabel(monto))
    layout.addWidget(QLabel(str(metodo_pago)))
    layout.addWidget(QLabel(cliente))

    return widget

if __name__ == '__main__':
    widgets_ventas_del_dia()