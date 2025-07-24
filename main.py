import math
from datetime import datetime

from PySide6.QtCore import QSize, QDate
from PySide6.QtGui import QPixmap, QIcon, Qt, QFont, QCloseEvent
from PySide6.QtWidgets import QMainWindow, QApplication, QListWidgetItem, QWidget, QHBoxLayout, QLabel, QSpinBox, \
    QVBoxLayout, QSizePolicy, QComboBox, QPushButton, QToolButton, QListWidget, QLineEdit, QMessageBox

from cambiar_producto import crear_items_detalle
from cancelar_ventas import widgets_ventas_cancelar
from clases.agregar_stock_dao import AgregarStockDAO
from clases.produto_dao import ProductoDAO
from clases.realizar_venta_dao import RealizarVentaDAO
from clases.ventas_dao import VentasDAO
from modificar_cantidades import crear_items_modificar_cantidades
from nueva_ventana import NuevaVentana
from ventanaPrincipal3 import Ui_VentanaPrincipal
from ventas_del_dia import widgets_ventas_del_dia


class Inicio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VentanaPrincipal()
        self.setWindowIcon(QIcon('img/logo.png'))
        self.ui.setupUi(self)
        self.definir_metodos_pago()
        self.ui.btn_limpiar.clicked.connect(self.limpiar_carrito)
        self.ui.pila_menu.currentChanged.connect(self.cambio_menu_principal)
        self.ui.btn_vender.clicked.connect(self.finalizar_venta)
        self.ui.fecha_ventas_dia.setDate(QDate.currentDate())
        self.ui.dateEdit_desde.setDate(QDate.currentDate().addDays(-30))
        self.ui.dateEdit_hasta.setDate(QDate.currentDate())
        self.ui.fecha_ventas_dia.dateChanged.connect(self.caja_diaria)
        self.ui.btn_modificar_cantidades.clicked.connect(self.crear_ventana_modificar_cantidades)
        self.setStyleSheet('QLabel, QPushButton, QComboBox, QWidget, QLineEdit {font-size: 18px; font-family: Arial; }')
        self.load_products()

    def closeEvent(self, event: QCloseEvent):
        self.limpiar_carrito()

    def cambio_menu_principal(self, indice):
        match indice:
            case 0:
                self.load_products()
                print('Carga productos')
            case 1:
                print('Modificacion Stock')

            case 2:
                self.load_cancelar_ventas()
                print('Cancelar')
            case 3:

                self.caja_diaria()
                print('Reportes')

    def crear_ventana_modificar_cantidades(self):
        self.ventana_modificar_cantidades = NuevaVentana('Modificar cantidades')
        self.lista_modificar_cantidades = QListWidget()
        item_titulo = QListWidgetItem()
        item_titulo.setSizeHint(QSize(600, 80))

        widget_titulo = QWidget()
        layout = QHBoxLayout(widget_titulo)
        for texto in ["Imagen", "Nombre", "Talle", "Cantidad", "Unidades", "Boton"]:
            label = QLabel(texto)
            label.setAlignment(Qt.AlignCenter)
            layout.addWidget(label)

        self.lista_modificar_cantidades.addItem(item_titulo)
        self.lista_modificar_cantidades.setItemWidget(item_titulo, widget_titulo)

        for item, widget in crear_items_modificar_cantidades():
            boton = widget.layout().itemAt(5).widget()
            spn_cantidad = widget.layout().itemAt(4).widget()
            boton.clicked.connect(
                lambda _, i=item, s=spn_cantidad: self.modificar_cantidad(
                    i.data(Qt.UserRole)[0],
                    i.data(Qt.UserRole)[1],
                    s.value(),
                    widget.layout().itemAt(1).widget().text(),
                    widget.layout().itemAt(2).widget().text()

                )
            )

            self.lista_modificar_cantidades.addItem(item)
            self.lista_modificar_cantidades.setItemWidget(item, widget)
        self.ventana_modificar_cantidades.layout.addWidget(self.lista_modificar_cantidades)

        self.ventana_modificar_cantidades.show()

    def modificar_cantidad(self, id_prod, id_talle, cantidad, prod, talle):
        #print(f'Agregar {cantidad}, al talle {id_talle} del prod {id_prod}')
        respuesta = QMessageBox.question(self, "Guardar Cambios", f'Confirma agregar {cantidad} unidad/es, de {prod} talle {talle}?', QMessageBox.Yes | QMessageBox.No)
        #mensaje.setIcon(QMessageBox.Question)
        #mensaje.setWindowTitle('Guardar Cambios')
        #mensaje.setText(f'Confirma agregar {cantidad}, al talle {talle} del prod {prod}?')
        #mensaje.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        #mensaje.exec()
        if respuesta == QMessageBox.Yes:
            AgregarStockDAO.agregar_stock(id_prod, id_talle, cantidad)
            self.ventana_modificar_cantidades.destroy()
            self.crear_ventana_modificar_cantidades()
    def finalizar_venta(self):
        if self.ui.label_monto_total.text() != '' and self.ui.label_monto_total.text() != '0.0':
            self.ventana_factura = NuevaVentana('Finalizar Venta')
            componente = QWidget()
            vertica_layout = QVBoxLayout(componente)

            horizontal_layout = QHBoxLayout()
            horizontal_layout.setAlignment(Qt.AlignCenter)
            horizontal_layout.setSpacing(250)
            #fuente = QFont("Arial",18)
            total = QLabel(f'Total: ${self.ui.label_monto_total.text()}')
            #total.setFont(fuente)
            medio_pago = QLabel(f'Medio de Pago: {self.ui.combo_medio_pago.currentText().upper()}')
            #medio_pago.setFont(fuente)
            horizontal_layout.addWidget(total)
            horizontal_layout.addWidget(medio_pago)
            vertica_layout.addLayout(horizontal_layout)
            self.nro_recibo = QLineEdit()
            self.nro_recibo.setPlaceholderText('Numero de Recibo')
            vertica_layout.addWidget(self.nro_recibo)


            self.nombre_cliente = QLineEdit()
            self.correo_cliente = QLineEdit()
            self.celular_cliente = QLineEdit()
            self.nombre_cliente.setPlaceholderText('Nombre y Apellido')
            #self.nombre_cliente.setFont(fuente)
            self.correo_cliente.setPlaceholderText('Correo ')
            #self.correo_cliente.setFont(fuente)
            self.celular_cliente.setPlaceholderText('Celular')
            #self.celular_cliente.setFont(fuente)
            vertica_layout.addWidget(self.nombre_cliente)
            vertica_layout.addWidget(self.correo_cliente)
            vertica_layout.addWidget(self.celular_cliente)

            boton_cancelar = QPushButton()
            boton_cancelar.setText('Cancelar')
            boton_cancelar.clicked.connect(self.ventana_factura.destroy)

            boton_aceptar = QPushButton()
            boton_aceptar.setText('Aceptar')
            boton_aceptar.clicked.connect(self.cargar_venta)

            #boton_aceptar.setFont(fuente)
            #boton_cancelar.setFont(fuente)

            vertica_layout.addWidget(boton_cancelar)
            vertica_layout.addWidget(boton_aceptar)
            self.ventana_factura.layout.addWidget(componente)
            self.ventana_factura.show()
        else:
            mensaje = QMessageBox()
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setWindowTitle('Advertencia')
            mensaje.setText('El carrito esta vacio')
            mensaje.setStandardButtons(QMessageBox.Ok)
            mensaje.exec()

    def listar_productos_carrito(self, metodo_pago):
        productos = []
        for i in range(self.ui.lista_detalle_venta.count()):
            item = self.ui.lista_detalle_venta.item(i)

            if item:
                label_precio, precio_efec, precio_tarj, cantidad, id_talle, id_prod, item = item.data(Qt.UserRole)
                if metodo_pago == 1 or metodo_pago == 2:
                    productos.append((id_prod , id_talle, precio_efec, cantidad))
                else:
                    productos.append((id_prod, id_talle, precio_tarj, cantidad))
        return productos


    def cargar_venta(self):
        id_cliente = 1
        if self.nro_recibo.text() != '':
            # if hasattr(self, 'nombre_cliente'):
            #     id_cliente=2
            #     if self.nombre_cliente.text() == '' or self.celular_cliente.text() == '' or self.correo_cliente.text() == '':
            #         mensaje = QMessageBox()
            #         mensaje.setIcon(QMessageBox.Warning)
            #         mensaje.setWindowTitle('Advertencia')
            #         mensaje.setText('Completar los datos de la factura')
            #         mensaje.setStandardButtons(QMessageBox.Ok)
            #         mensaje.exec()
            #         return
            RealizarVentaDAO.realizar_venta(float(self.ui.label_monto_total.text()), self.ui.combo_medio_pago.currentIndex()+1, id_cliente, self.nro_recibo.text(), self.listar_productos_carrito(self.ui.combo_medio_pago.currentIndex()+1))
            print(f'Total Venta {float(self.ui.label_monto_total.text())}  '
                  f'Id Metodo de Pago: {self.ui.combo_medio_pago.currentIndex()+1}  '
                  f'Id Cliente {id_cliente}  '
                  f'Detalle Venta Producto  '
                  f'Productos{self.listar_productos_carrito(self.ui.combo_medio_pago.currentIndex()+1)}' #paso el id del metodo de pago
                  )
            self.ui.lista_detalle_venta.clear()
            self.actualizar_total_venta()
            self.ventana_factura.close()
            #return float(self.ui.label_monto_total.text()),self.ui.combo_medio_pago.currentIndex()+1,self.listar_productos_carrito()
        else:
            mensaje = QMessageBox()
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setWindowTitle('Advertencia')
            mensaje.setText('Completar Numero de recibo')
            mensaje.setStandardButtons(QMessageBox.Ok)
            mensaje.exec()
            return




    def caja_diaria(self):
        self.ui.lista_ventas_dia.clear()
        fecha = self.ui.fecha_ventas_dia.date().toPython()
        if not widgets_ventas_del_dia(fecha):
            mensaje = QMessageBox()
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setWindowTitle('Advertencia')
            mensaje.setText('No hay ventas en esta fecha')
            mensaje.setStandardButtons(QMessageBox.Ok)
            mensaje.exec()
        else:
            widgets, total, efectivo, tarjeta, transferencia = widgets_ventas_del_dia(fecha)
            for widget in widgets:
                item = QListWidgetItem()
                item.setSizeHint(QSize(350, 80))

                self.ui.lista_ventas_dia.addItem(item)
                self.ui.lista_ventas_dia.setItemWidget(item, widget)
            self.ui.total_vendido.setText(f'Total: \n${total:,.2f}')
            self.ui.total_efectivo.setText(f'Efectivo: \n${efectivo:,.2f}')
            self.ui.total_tarjetas.setText(f'Tarjeta: \n${tarjeta:,.2f}')
            self.ui.total_transferencia.setText(f'Transferencia: \n${transferencia:,.2f}')

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
        for widget in crear_items_detalle(id, self.cambio_talle):
            item = QListWidgetItem()
            item.setSizeHint(QSize(600,80))
            self.lista_detalle.addItem(item)
            self.lista_detalle.setItemWidget(item,widget)
        self.ventana_detalle.layout.addWidget(self.lista_detalle)

        self.ventana_detalle.show()


    def cambio_talle(self, id_prod, id_talle, detalle):
        #buscar los prod que tienen ese talle
        talles = VentasDAO.seleccionar_talles_cambio(id_prod)
        self.ventana_cambio_talle = NuevaVentana('Cambio de Talle')
        componente = QWidget()
        layout = QVBoxLayout(componente)
        layout.setAlignment(Qt.AlignCenter)

        lbl_talle_actual = QLabel(f'Talle Actual: {detalle.talle}')


        layout.addWidget(lbl_talle_actual)

        self.ventana_cambio_talle.layout.addWidget(componente)
        self.ventana_cambio_talle.show()

    def load_products(self):
        self.ui.lista_productos.clear()
        productos = ProductoDAO.seleccionar_productos()
        #tomar produtos bd
        for p in productos:
            self.agregar_producto(p.id, p.nombre, p.precio,True)
        combos = ProductoDAO.seleccionar_combos()
        for c in combos:
            self.agregar_producto(c.id_combo,c.nombre, c.precio,False)



    def agregar_producto(self, id, nombre, precio, producto):
        item = QListWidgetItem()
        item.setSizeHint(QSize(350,80))

        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)
        img_label = QLabel()
        pixmap = QPixmap(f'img/{nombre}.png').scaled(75,75)
        img_label.setPixmap(pixmap)

        widget_precios = QWidget()
        layout_precios = QVBoxLayout(widget_precios)
        precio_efectivo = float(precio)
        precio_tarjeta = float(precio * 1.15)
        label_efectivo = QLabel(f'Efectivo: ${precio_efectivo:,.2f}')
        label_tarjeta = QLabel(f'Tarjeta: ${precio_tarjeta:,.2f}')
        layout_precios.addWidget(label_efectivo)
        layout_precios.addWidget(label_tarjeta)

        text_label = QLabel(nombre.upper())

        # cantidad = QSpinBox()
        # cantidad.setMinimum(1)
        # cantidad.setProperty('label_efectivo', label_efectivo)
        # cantidad.setProperty('label_tarjeta', label_tarjeta)
        # cantidad.setProperty('precio_efectivo', precio_efectivo)
        # cantidad.setProperty('precio_tarjeta', precio_tarjeta)
        # cantidad.resize(100,20)
        # cantidad.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # cantidad.setValue(1)
        # cantidad.setMinimum(1)
        #
        # widget_talles =QWidget()
        # layout_talles =QVBoxLayout(widget_talles)
        # cbo_talle = QComboBox()
        # for t in talles:
        #     data = {
        #         'idTalle': t.idTalle,
        #         't_precio_efectivo': t.precio_efectivo,
        #         't_precio_tarjeta': t.precio_tarjeta,
        #     }
        #     cbo_talle.addItem(t.talle, data)
        # cbo_talle.setProperty('precio_efectivo', precio_efectivo)
        # cbo_talle.setProperty('precio_tarjeta', precio_tarjeta)
        # cbo_talle.setProperty('label_efectivo', label_efectivo)
        # cbo_talle.setProperty('label_tarjeta', label_tarjeta)
        # cbo_talle.resize(150,20)
        # cbo_talle.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # cbo_talle.currentIndexChanged.connect(self.actualizar_precio)
        # layout_talles.addWidget(cbo_talle)
        # layout_talles.addWidget(cantidad)

        boton_agregar = QToolButton()
        pixmap = QPixmap('img/agregar_carrito.png')
        icono = QIcon(pixmap)
        boton_agregar.setIcon(icono)
        boton_agregar.setText('Agregar')
        boton_agregar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        if producto: #para ver si es prod o combo
            boton_agregar.clicked.connect(
                lambda: self.elegir_talle_cantidad(id, nombre, precio))
        else:
            boton_agregar.clicked.connect(
                lambda: self.elegir_talle_prod_combo(id, nombre, precio))


        # layout_talles.setContentsMargins(0, 0, 0, 0)
        layout_precios.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(img_label)
        layout.addWidget(text_label)
        layout.addWidget(widget_precios)
        #layout.addWidget(widget_talles)
        layout.addWidget(boton_agregar)



        self.ui.lista_productos.addItem(item)
        self.ui.lista_productos.setItemWidget(item, widget)

    def elegir_talle_prod_combo(self, id_producto, nombre, precio):
        self.ventana_talle_cantidad= NuevaVentana('Elegir Talle')
        componente = QWidget()
        horizontal_layout = QHBoxLayout(componente)
        horizontal_layout.setAlignment(Qt.AlignCenter)
        horizontal_layout.setSpacing(100)
        talles = ProductoDAO.seleccionar_talles(id_producto)



        cbo_talle = QComboBox()
        for t in talles:
            data = {
                'id_talle': t.id_talle,
                'cantidad': t.stock
            }
            cbo_talle.addItem(t.talle, data)
        cbo_talle.resize(150,20)
        cbo_talle.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        cbo_talle.setEditable(False)
        cbo_talle.currentIndexChanged.connect(self.actualizar_stock_disponible)

        self.cantidad_stock = QSpinBox()
        self.cantidad_stock.setMinimum(1)
        self.cantidad_stock.setMaximum(talles[0].stock)
        self.cantidad_stock.resize(100, 20)
        self.cantidad_stock.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.cantidad_stock.setValue(1)

        boton_agregar = QToolButton()
        pixmap = QPixmap('img/agregar_carrito.png')
        icono = QIcon(pixmap)
        boton_agregar.setIcon(icono)
        boton_agregar.setText('Agregar')
        boton_agregar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        boton_agregar.clicked.connect(
            lambda: self.agregar_producto_al_carrito(id_producto,nombre, precio, math.trunc(precio * 1.15 *100) /100 ,cbo_talle.currentText(), self.cantidad_stock.value(),cbo_talle.currentData()['id_talle']))

        img_label = QLabel()
        pixmap = QPixmap(f'img/{nombre}.png').scaled(75, 75)
        img_label.setPixmap(pixmap)



        horizontal_layout.addWidget(img_label)
        horizontal_layout.addWidget(QLabel(str(nombre)))
        horizontal_layout.addWidget(cbo_talle)
        horizontal_layout.addWidget(self.cantidad_stock)
        horizontal_layout.addWidget(boton_agregar)

        self.ventana_talle_cantidad.layout.addWidget(componente)
        self.ventana_talle_cantidad.show()


    def elegir_talle_cantidad(self, id_producto, nombre, precio):
        self.ventana_talle_cantidad= NuevaVentana('Elegir Talle')
        componente = QWidget()
        horizontal_layout = QHBoxLayout(componente)
        horizontal_layout.setAlignment(Qt.AlignCenter)
        horizontal_layout.setSpacing(100)
        talles = ProductoDAO.seleccionar_talles(id_producto)



        cbo_talle = QComboBox()
        for t in talles:
            data = {
                'id_talle': t.id_talle,
                'cantidad': t.stock
            }
            cbo_talle.addItem(t.talle, data)
        cbo_talle.resize(150,20)
        cbo_talle.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        cbo_talle.setEditable(False)
        cbo_talle.currentIndexChanged.connect(self.actualizar_stock_disponible)

        self.cantidad_stock = QSpinBox()
        self.cantidad_stock.setMinimum(1)
        self.cantidad_stock.setMaximum(talles[0].stock)
        self.cantidad_stock.resize(100, 20)
        self.cantidad_stock.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.cantidad_stock.setValue(1)

        boton_agregar = QToolButton()
        pixmap = QPixmap('img/agregar_carrito.png')
        icono = QIcon(pixmap)
        boton_agregar.setIcon(icono)
        boton_agregar.setText('Agregar')
        boton_agregar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        boton_agregar.clicked.connect(
            lambda: self.agregar_producto_al_carrito(id_producto,nombre, precio, math.trunc(precio * 1.15 *100) /100 ,cbo_talle.currentText(), self.cantidad_stock.value(),cbo_talle.currentData()['id_talle']))

        img_label = QLabel()
        pixmap = QPixmap(f'img/{nombre}.png').scaled(75, 75)
        img_label.setPixmap(pixmap)



        horizontal_layout.addWidget(img_label)
        horizontal_layout.addWidget(QLabel(str(nombre)))
        horizontal_layout.addWidget(cbo_talle)
        horizontal_layout.addWidget(self.cantidad_stock)
        horizontal_layout.addWidget(boton_agregar)

        self.ventana_talle_cantidad.layout.addWidget(componente)
        self.ventana_talle_cantidad.show()

    def actualizar_stock_disponible(self):
        combo = self.sender()
        stock = combo.currentData()['cantidad']
        self.cantidad_stock.setMaximum(stock)


    def agregar_producto_al_carrito(self, id_producto, nombre, precio_efec, precio_tarj, talle, cantidad, id_talle):
        self.ventana_talle_cantidad.close()
        RealizarVentaDAO.descontar_stock(id_producto,id_talle, cantidad)
        item = QListWidgetItem()
        item.setSizeHint(QSize(305, 80))
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)
        img_label = QLabel()
        pixmap = QPixmap(f'img/{nombre}.png').scaled(75, 75)
        img_label.setPixmap(pixmap)
        if self.ui.combo_medio_pago.currentText() == 'Efectivo' or self.ui.combo_medio_pago.currentText() == 'Transferencia':
            self.label_precio = QLabel(str(precio_efec * cantidad))
        else:
            self.label_precio = QLabel(str(precio_tarj * cantidad))
        label_nombre = QLabel(nombre)

        widget_nombre_precio = QWidget()
        layout_nombre_precio = QVBoxLayout(widget_nombre_precio)
        layout_nombre_precio.addWidget(label_nombre)
        layout_nombre_precio.addWidget(self.label_precio)

        widget_talles = QWidget()
        layout_talles = QVBoxLayout(widget_talles)
        layout_talles.addWidget(QLabel(f'T:{talle}'))
        layout_talles.addWidget(QLabel(str(cantidad)))
        layout_talles.setContentsMargins(0, 0, 0, 0)


        boton_eliminar_carrito = QToolButton()
        pixmap = QPixmap('img/eliminar_carrito.png')
        icono = QIcon(pixmap)
        boton_eliminar_carrito.setIcon(icono)
        boton_eliminar_carrito.setIconSize(QSize(20,80))

        #layout.addWidget(QLabel(str(id)))
        layout.addWidget(img_label)
        layout.addWidget(widget_nombre_precio)
        layout.addWidget(widget_talles)
        layout.addWidget(boton_eliminar_carrito)


        self.ui.lista_detalle_venta.addItem(item)
        self.ui.lista_detalle_venta.setItemWidget(item, widget)

        # Guardamos referencias para actualizar el precio más tarde
        item.setData(Qt.UserRole, (self.label_precio, precio_efec, precio_tarj, cantidad, id_talle, id_producto))

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
            RealizarVentaDAO.regresar_stock(item.data(Qt.UserRole)[5],item.data(Qt.UserRole)[4],item.data(Qt.UserRole)[3])
            self.ui.lista_detalle_venta.takeItem(row)

        self.actualizar_total_venta()

    def actualizar_precios_carrito(self):
        """Actualiza los precios de todos los productos del carrito cuando cambia el método de pago."""
        for i in range(self.ui.lista_detalle_venta.count()):
            item = self.ui.lista_detalle_venta.item(i)
            if item:
                label_precio, precio_efec, precio_tarj, cantidad, id_talle, id_prod, item = item.data(Qt.UserRole)

                if self.ui.combo_medio_pago.currentText() == 'Efectivo' or self.ui.combo_medio_pago.currentText() == 'Transferencia':
                    label_precio.setText(str(precio_efec * cantidad))
                else:
                    label_precio.setText(str(precio_tarj * cantidad))
        self.actualizar_total_venta()

    def actualizar_precio(self, valor):
        combobox = self.sender() #sender obtiene el objeto que lo invoco
        label_efectivo = combobox.property('label_efectivo')
        label_tarjeta = combobox.property('label_tarjeta')
        precio_efectivo = combobox.property('precio_efectivo')
        precio_tarjeta = combobox.property('precio_tarjeta')
        precio_efectivo = combobox.currentData()['t_precio_efectivo']
        precio_tarjeta = combobox.currentData()['t_precio_tarjeta']
        label_efectivo.setText(f'Efectivo: ${(precio_efectivo):,}')
        label_tarjeta.setText(f'Tarjeta: ${(precio_tarjeta):,.2f}')

    def limpiar_carrito(self):
        if self.ui.lista_detalle_venta.count() < 1:
            return
        for i in range(self.ui.lista_detalle_venta.count()):
            item = self.ui.lista_detalle_venta.item((i))
            RealizarVentaDAO.regresar_stock(item.data(Qt.UserRole)[5],item.data(Qt.UserRole)[4],item.data(Qt.UserRole)[3])
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