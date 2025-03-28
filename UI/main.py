from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QIcon, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QListWidgetItem, QWidget, QHBoxLayout, QLabel, QSpinBox, \
    QVBoxLayout, QSizePolicy, QComboBox, QPushButton, QToolButton

from UI.ventanaPrincipal3 import Ui_VentanaPrincipal




class Inicio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VentanaPrincipal()
        self.ui.setupUi(self)
        self.load_products()

    def load_products(self):
        productos = [
            ('Camiseta de Juego', '22500', 'camiseta_cef.jpg', ['S', 'M', 'L']),
            ('Camiseta de Juego', '22500', 'camiseta_cef.jpg', ['S', 'M', 'L'])
        ]
        for nombre, precio, imagen, talles in productos:
            self.agregar_producto(nombre, precio, imagen, talles)

    def agregar_producto(self, nombre, precio, imagen, talles):
        item = QListWidgetItem()
        item.setSizeHint(QSize(350,80))


        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(40)
        img_label = QLabel()
        pixmap = QPixmap(f'../img/{imagen}').scaled(75,75)
        img_label.setPixmap(pixmap)

        widget_precios = QWidget()
        layout_precios = QVBoxLayout(widget_precios)
        layout_precios.addWidget(QLabel(f'Efectivo: ${int(precio):,}'))
        layout_precios.addWidget(QLabel(f'Tarjeta: ${float(precio) * 1.15:,.2f}'))

        text_label = QLabel(nombre)

        cantidad = QSpinBox()
        cantidad.resize(100,20)
        cantidad.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        cantidad.setValue(1)
        cantidad.setMinimum(1)

        widget_talles =QWidget()
        layout_talles =QVBoxLayout(widget_talles)
        cbo_talle = QComboBox()
        cbo_talle.addItems(talles)
        cbo_talle.resize(150,20)
        cbo_talle.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout_talles.addWidget(cbo_talle)
        layout_talles.addWidget(cantidad)

        boton_agregar = QToolButton()
        pixmap = QPixmap('../img/agregar_carrito.png')
        icono = QIcon(pixmap)
        boton_agregar.setIcon(icono)
        boton_agregar.setText('Agregar')
        boton_agregar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)



        layout_talles.setContentsMargins(0, 0, 0, 0)
        layout_precios.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(img_label)
        layout.addWidget(text_label)
        layout.addWidget(widget_precios)
        layout.addWidget(widget_talles)
        layout.addWidget(boton_agregar)

        self.ui.lista_productos.addItem(item)
        self.ui.lista_productos.setItemWidget(item, widget)




if __name__ == '__main__':
    app = QApplication([])
    ventana = Inicio()
    ventana.show()
    app.exec()