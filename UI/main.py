from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QIcon, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QListWidgetItem, QWidget, QHBoxLayout, QLabel, QSpinBox, \
    QVBoxLayout, QSizePolicy, QComboBox, QPushButton, QToolButton, QListView, QListWidget

from UI.cambiar_producto import crear_items_detalle
from UI.cancelar_ventas import load_ventas_cancelar, widgets_ventas_cancelar
from UI.nueva_ventana import NuevaVentana
from UI.ventanaPrincipal3 import Ui_VentanaPrincipal




class Inicio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VentanaPrincipal()
        self.ui.setupUi(self)

        self.definir_metodos_pago()
        self.ui.btn_limpiar.clicked.connect(self.limpiar_carrito)
        self.ui.pila_menu.currentChanged.connect(self.cambio_menu_principal)
        self.productos = [
            (1, 'Camiseta de Juego', '22500', 'camiseta_cef.jpg', ['S', 'M', 'L']),
            (2, 'Camiseta de Juego', '22500', 'camiseta_cef.jpg', ['S', 'M', 'L']),
            (3, 'Camiseta de Juego', '22500', 'camiseta_cef.jpg', ['S', 'M', 'L']),
            (4, 'Camiseta de Juego', '22500', 'camiseta_cef.jpg', ['S', 'M', 'L']),
            (5, 'Camiseta de Juego', '22500', 'camiseta_cef.jpg', ['S', 'M', 'L']),
            (6, 'Camiseta de Juego', '22500', 'camiseta_cef.jpg', ['S', 'M', 'L']),
            (7, 'Camiseta de Juego', '22500', 'camiseta_cef.jpg', ['S', 'M', 'L']),
            (8, 'Camiseta de Juego', '22500', 'camiseta_cef.jpg', ['S', 'M', 'L']),
            (9, 'Camiseta de Juego', '22500', 'camiseta_cef.jpg', ['S', 'M', 'L']),
            (10, 'Camiseta de Juego', '500', 'camiseta_cef.jpg', ['S', 'M', 'L'])
        ]
        self.load_products()


    def cambio_menu_principal(self, indice):
        match indice:
            case 0:
                self.load_products()
                print('Carga productos')
            case 1:
                self.productos.pop()
                self.productos.append((107,'Camiseta de Juego', '25500', 'camiseta_cef.jpg', ['S', 'M', 'L']))
                print('Modificacion Stock')

            case 2:
                self.load_cancelar_ventas()
                print('Cancelar')
            case 3:
                print('Reportes')

    def definir_metodos_pago(self):
        metodos_pago = ['Efectivo', 'Transferencia', 'Tarjeta']
        self.ui.combo_medio_pago.addItems(metodos_pago)

    def load_cancelar_ventas(self):
        self.ui.lista_ventas_cancelar.clear()
        for widget in widgets_ventas_cancelar(self.mostrar_detalle):
            item =QListWidgetItem()
            item.setSizeHint(QSize(350,80))

            self.ui.lista_ventas_cancelar.addItem(item)
            self.ui.lista_ventas_cancelar.setItemWidget(item, widget)

    def mostrar_detalle(self, id):
        self.ventana_detalle = NuevaVentana(f'Detalle Venta {id}')
        self.lista_detalle = QListWidget()
        for widget in crear_items_detalle(id):
            item = QListWidgetItem()
            item.setSizeHint(QSize(600,80))
            self.lista_detalle.addItem(item)
            self.lista_detalle.setItemWidget(item,widget)
        self.ventana_detalle.layout.addWidget(self.lista_detalle)

        self.ventana_detalle.show()


    def load_products(self):
        self.ui.lista_productos.clear()
        #tomar produtos bd
        for id, nombre, precio, imagen, talles in self.productos:
            self.agregar_producto(id, nombre, precio, imagen, talles)

    def agregar_producto(self, id, nombre, precio, imagen, talles):
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
        precio = float(precio)
        label_efectivo = QLabel(f'Efectivo: ${precio:,}')
        label_tarjeta = QLabel(f'Tarjeta: ${precio * 1.15:,.2f}')
        layout_precios.addWidget(label_efectivo)
        layout_precios.addWidget(label_tarjeta)

        text_label = QLabel(nombre)

        cantidad = QSpinBox()
        cantidad.setMinimum(1)
        cantidad.setProperty('label_efectivo', label_efectivo)
        cantidad.setProperty('label_tarjeta', label_tarjeta)
        cantidad.setProperty('precio_base', precio)
        cantidad.valueChanged.connect(self.actualizar_precio)
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
        boton_agregar.clicked.connect(
            lambda: self.agregar_producto_al_carrito(id, nombre, self.split_precio(label_efectivo.text()), self.split_precio(label_tarjeta.text()), imagen, cbo_talle.currentText(),
                                                     cantidad.value()))


        layout_talles.setContentsMargins(0, 0, 0, 0)
        layout_precios.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(img_label)
        layout.addWidget(text_label)
        layout.addWidget(widget_precios)
        layout.addWidget(widget_talles)
        layout.addWidget(boton_agregar)



        self.ui.lista_productos.addItem(item)
        self.ui.lista_productos.setItemWidget(item, widget)



    def agregar_producto_al_carrito(self, id, nombre, precio_efec, precio_tarj, imagen, talle, cantidad):
        print(id, nombre, precio_efec, precio_tarj, imagen, talle, cantidad)
        item = QListWidgetItem()
        item.setSizeHint(QSize(305, 80))
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)
        img_label = QLabel()
        pixmap = QPixmap(f'../img/{imagen}').scaled(75, 75)
        img_label.setPixmap(pixmap)
        if self.ui.combo_medio_pago.currentText() == 'Efectivo' or self.ui.combo_medio_pago.currentText() == 'Transferencia':
            self.label_precio = QLabel(str(precio_efec))
        else:
            self.label_precio = QLabel(str(precio_tarj))
        label_nombre = QLabel(nombre)

        widget_nombre_precio = QWidget()
        layout_nombre_precio = QVBoxLayout(widget_nombre_precio)
        layout_nombre_precio.addWidget(label_nombre)
        layout_nombre_precio.addWidget(self.label_precio)

        widget_talles = QWidget()
        layout_talles = QVBoxLayout(widget_talles)
        layout_talles.addWidget(QLabel(str(talle)))
        layout_talles.addWidget(QLabel(str(cantidad)))
        layout_talles.setContentsMargins(0, 0, 0, 0)


        boton_eliminar_carrito = QToolButton()
        pixmap = QPixmap('../img/eliminar_carrito.png')
        icono = QIcon(pixmap)
        boton_eliminar_carrito.setIcon(icono)
        boton_eliminar_carrito.setIconSize(QSize(20,80))


        layout.addWidget(img_label)
        layout.addWidget(widget_nombre_precio)
        layout.addWidget(widget_talles)
        layout.addWidget(boton_eliminar_carrito)


        self.ui.lista_detalle_venta.addItem(item)
        self.ui.lista_detalle_venta.setItemWidget(item, widget)

        # Guardamos referencias para actualizar el precio más tarde
        item.setData(Qt.UserRole, (self.label_precio, precio_efec, precio_tarj, item))

        boton_eliminar_carrito.clicked.connect(lambda: self.eliminar_producto_del_carrito(item))

        # Conectar la señal para actualizar el precio cuando cambie el método de pago
        self.ui.combo_medio_pago.currentIndexChanged.connect(self.actualizar_precios_carrito)
        #ver si solo pasar precio en efec y no el de tarj y cambiarlo

        #modificar Precio total de la venta
        self.actualizar_total_venta()

    def actualizar_total_venta(self):
        total = 0.00
        for i in range(self.ui.lista_detalle_venta.count()):
            item = self.ui.lista_detalle_venta.item(i)
            widget =self.ui.lista_detalle_venta.itemWidget(item)

            if widget:
                total += float(widget.findChildren(QLabel)[2].text())

        self.ui.label_monto_total.setText(str(total))

    def eliminar_producto_del_carrito(self, item):
        row = self.ui.lista_detalle_venta.row(item)
        if row != -1: #si da -1 es pq no existe
            self.ui.lista_detalle_venta.takeItem(row)

        self.actualizar_total_venta()

    def actualizar_precios_carrito(self):
        """Actualiza los precios de todos los productos del carrito cuando cambia el método de pago."""
        for i in range(self.ui.lista_detalle_venta.count()):
            item = self.ui.lista_detalle_venta.item(i)
            if item:
                label_precio, precio_efec, precio_tarj, item = item.data(Qt.UserRole)
                if self.ui.combo_medio_pago.currentText() == 'Efectivo' or self.ui.combo_medio_pago.currentText() == 'Transferencia':
                    label_precio.setText(str(precio_efec))
                else:
                    label_precio.setText(str(precio_tarj))
        self.actualizar_total_venta()

    def actualizar_precio(self, valor):
        spinbox = self.sender() #sender obtiene el objeto que lo invoco
        label_efectivo = spinbox.property('label_efectivo')
        label_tarjeta = spinbox.property('label_tarjeta')
        precio_base = spinbox.property('precio_base')

        label_efectivo.setText(f'Efectivo: ${(precio_base * valor):,}')
        label_tarjeta.setText(f'Tarjeta: ${(precio_base * valor) * 1.15:,.2f}')

    def limpiar_carrito(self):

        self.ui.lista_detalle_venta.clear()
        self.actualizar_total_venta()

    def split_precio(self, cadena):
        precio_sin_texto = cadena[(cadena.find('$'))+1:]
        precio_sin_texto = float(precio_sin_texto.replace(',', ''))
        return precio_sin_texto




if __name__ == '__main__':
    app = QApplication([])
    ventana = Inicio()
    ventana.show()
    app.exec()