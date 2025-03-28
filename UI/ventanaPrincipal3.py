# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mockupFinal2.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        if not VentanaPrincipal.objectName():
            VentanaPrincipal.setObjectName(u"VentanaPrincipal")
        VentanaPrincipal.setEnabled(True)
        VentanaPrincipal.resize(1000, 700)
        VentanaPrincipal.setStyleSheet("font-size: 16px;")
        VentanaPrincipal.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.centralwidget = QWidget(VentanaPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frameFondo = QFrame(self.centralwidget)
        self.frameFondo.setObjectName(u"frameFondo")
        self.frameFondo.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameFondo.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameFondo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_izquierda = QFrame(self.frameFondo)
        self.frame_izquierda.setObjectName(u"frame_izquierda")
        self.frame_izquierda.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_izquierda.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_izquierda)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_izquierda)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.btn_venta_productos = QPushButton(self.frame_2)
        self.btn_venta_productos.setObjectName(u"btn_venta_productos")
        self.btn_venta_productos.pressed.connect(lambda: self.pila_menu.setCurrentIndex(0))

        self.horizontalLayout_2.addWidget(self.btn_venta_productos)

        self.btn_stock = QPushButton(self.frame_2)
        self.btn_stock.setObjectName(u"btn_stock")
        self.btn_stock.pressed.connect(lambda: self.pila_menu.setCurrentIndex(1))
        self.horizontalLayout_2.addWidget(self.btn_stock)

        self.btn_cambios = QPushButton(self.frame_2)
        self.btn_cambios.setObjectName(u"btn_cambios")
        self.btn_cambios.pressed.connect(lambda: self.pila_menu.setCurrentIndex(2))

        self.horizontalLayout_2.addWidget(self.btn_cambios)

        self.btn_reportes = QPushButton(self.frame_2)
        self.btn_reportes.setObjectName(u"btn_reportes")
        self.btn_reportes.pressed.connect(lambda: self.pila_menu.setCurrentIndex(3))

        self.horizontalLayout_2.addWidget(self.btn_reportes)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.pila_menu = QStackedWidget(self.frame_izquierda)
        self.pila_menu.setObjectName(u"pila_menu")

        self.venta_productos = QWidget()
        self.venta_productos.setObjectName(u"venta_productos")
        self.lista_productos = QListWidget(self.venta_productos)
        self.lista_productos.setObjectName(u"lista_productos")
        #self.lista_productos.setContentsMargins(0,0,0,0)
        self.lista_productos.setGeometry(QRect(20, 30, 631, 511))
        self.lista_productos.setStyleSheet(u"QListWidget {\n"
"        background-color: #b8b6b2; /* Color de fondo gris claro */\n"                                          
"        border: 1px solid #ccc; /* Borde gris */\n"
"        padding: 0px;\n"
"    }\n"
"    \n"
"    QListWidget::item {\n"
"        background-color: white; /* Fondo de cada item */\n"
"        border: 1px solid transparent; /* Borde invisible */\n"
"        padding: 0px ;\n"
"        margin-bottom: 1px;\n"                                           
"    }\n"
"\n"

"\n"
"    QListWidget::item:hover {\n"
"        background-color: #e0e0e0; /* Fondo gris claro al pasar el mouse */\n"
"    }")
        self.btn_agregar_gasto = QPushButton(self.venta_productos)
        self.btn_agregar_gasto.setObjectName(u"btn_agregar_gasto")
        self.btn_agregar_gasto.setGeometry(QRect(20, 570, 111, 41))
        self.pila_menu.addWidget(self.venta_productos)
        self.stock = QWidget()
        self.stock.setObjectName(u"stock")
        self.frame_stock = QFrame(self.stock)
        self.frame_stock.setObjectName(u"frame_stock")
        self.frame_stock.setGeometry(QRect(10, 10, 651, 611))
        self.frame_stock.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_stock.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_stock)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_modificar_cantidades = QPushButton(self.frame_stock)
        self.btn_modificar_cantidades.setObjectName(u"btn_modificar_cantidades")

        self.verticalLayout_2.addWidget(self.btn_modificar_cantidades)

        self.btn_agregar_producto = QPushButton(self.frame_stock)
        self.btn_agregar_producto.setObjectName(u"btn_agregar_producto")

        self.verticalLayout_2.addWidget(self.btn_agregar_producto)

        self.btn_agregar_combo = QPushButton(self.frame_stock)
        self.btn_agregar_combo.setObjectName(u"btn_agregar_combo")

        self.verticalLayout_2.addWidget(self.btn_agregar_combo)

        self.btn_modificar_precios = QPushButton(self.frame_stock)
        self.btn_modificar_precios.setObjectName(u"btn_modificar_precios")

        self.verticalLayout_2.addWidget(self.btn_modificar_precios)

        self.pila_menu.addWidget(self.stock)
        self.cambios = QWidget()
        self.cambios.setObjectName(u"cambios")
        self.frame_cambios = QFrame(self.cambios)
        self.frame_cambios.setObjectName(u"frame_cambios")
        self.frame_cambios.setGeometry(QRect(0, 0, 651, 641))
        self.frame_cambios.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_cambios.setFrameShadow(QFrame.Shadow.Raised)
        self.lista_ventas_cambios = QListWidget(self.frame_cambios)
        self.lista_ventas_cambios.setObjectName(u"lista_ventas_cambios")
        self.lista_ventas_cambios.setGeometry(QRect(20, 10, 621, 571))
        self.btn_cancelar_venta = QPushButton(self.frame_cambios)
        self.btn_cancelar_venta.setObjectName(u"btn_cancelar_venta")
        self.btn_cancelar_venta.setGeometry(QRect(370, 590, 131, 41))
        self.btn_cambiar_producto = QPushButton(self.frame_cambios)
        self.btn_cambiar_producto.setObjectName(u"btn_cambiar_producto")
        self.btn_cambiar_producto.setGeometry(QRect(510, 590, 131, 41))
        self.pila_menu.addWidget(self.cambios)
        self.reportes = QWidget()
        self.reportes.setObjectName(u"reportes")
        self.frame_reportes = QFrame(self.reportes)
        self.frame_reportes.setObjectName(u"frame_reportes")
        self.frame_reportes.setGeometry(QRect(0, 0, 661, 641))
        self.frame_reportes.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_reportes.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_fecha = QFrame(self.frame_reportes)
        self.frame_fecha.setObjectName(u"frame_fecha")
        self.frame_fecha.setGeometry(QRect(10, 0, 661, 421))
        self.frame_fecha.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_fecha.setFrameShadow(QFrame.Shadow.Raised)
        self.fecha_ventas_dia = QDateEdit(self.frame_fecha)
        self.fecha_ventas_dia.setObjectName(u"fecha_ventas_dia")
        self.fecha_ventas_dia.setGeometry(QRect(30, 20, 110, 31))
        self.lista_ventas_dia = QListWidget(self.frame_fecha)
        self.lista_ventas_dia.setObjectName(u"lista_ventas_dia")
        self.lista_ventas_dia.setGeometry(QRect(10, 70, 621, 331))
        self.total_vendido = QLabel(self.frame_fecha)
        self.total_vendido.setObjectName(u"total_vendido")
        self.total_vendido.setGeometry(QRect(180, 10, 81, 31))
        self.lbl_total_vendido = QLabel(self.frame_fecha)
        self.lbl_total_vendido.setObjectName(u"lbl_total_vendido")
        self.lbl_total_vendido.setGeometry(QRect(170, 30, 81, 31))
        self.lbl_total_efectivo = QLabel(self.frame_fecha)
        self.lbl_total_efectivo.setObjectName(u"lbl_total_efectivo")
        self.lbl_total_efectivo.setGeometry(QRect(280, 30, 81, 31))
        self.total_efectivo = QLabel(self.frame_fecha)
        self.total_efectivo.setObjectName(u"total_efectivo")
        self.total_efectivo.setGeometry(QRect(290, 10, 81, 31))
        self.lbl_total_tarjetas = QLabel(self.frame_fecha)
        self.lbl_total_tarjetas.setObjectName(u"lbl_total_tarjetas")
        self.lbl_total_tarjetas.setGeometry(QRect(370, 30, 81, 31))
        self.total_tarjetas = QLabel(self.frame_fecha)
        self.total_tarjetas.setObjectName(u"total_tarjetas")
        self.total_tarjetas.setGeometry(QRect(380, 10, 81, 31))
        self.lbl_total_transferencia = QLabel(self.frame_fecha)
        self.lbl_total_transferencia.setObjectName(u"lbl_total_transferencia")
        self.lbl_total_transferencia.setGeometry(QRect(450, 30, 101, 31))
        self.total_transferencia = QLabel(self.frame_fecha)
        self.total_transferencia.setObjectName(u"total_transferencia")
        self.total_transferencia.setGeometry(QRect(480, 10, 81, 31))
        self.frame_alertas_stock = QFrame(self.frame_reportes)
        self.frame_alertas_stock.setObjectName(u"frame_alertas_stock")
        self.frame_alertas_stock.setGeometry(QRect(10, 430, 321, 191))
        self.frame_alertas_stock.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_alertas_stock.setFrameShadow(QFrame.Shadow.Raised)
        self.label_faltante_stock = QLabel(self.frame_alertas_stock)
        self.label_faltante_stock.setObjectName(u"label_faltante_stock")
        self.label_faltante_stock.setGeometry(QRect(90, 10, 101, 21))
        self.frame_descargar_pdfs = QFrame(self.frame_reportes)
        self.frame_descargar_pdfs.setObjectName(u"frame_descargar_pdfs")
        self.frame_descargar_pdfs.setGeometry(QRect(340, 430, 311, 201))
        self.frame_descargar_pdfs.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_descargar_pdfs.setFrameShadow(QFrame.Shadow.Raised)
        self.label_descarga_reportes = QLabel(self.frame_descargar_pdfs)
        self.label_descarga_reportes.setObjectName(u"label_descarga_reportes")
        self.label_descarga_reportes.setGeometry(QRect(90, 10, 121, 20))
        self.dateEdit_desde = QDateEdit(self.frame_descargar_pdfs)
        self.dateEdit_desde.setObjectName(u"dateEdit_desde")
        self.dateEdit_desde.setGeometry(QRect(10, 40, 110, 22))
        self.label_y = QLabel(self.frame_descargar_pdfs)
        self.label_y.setObjectName(u"label_y")
        self.label_y.setGeometry(QRect(140, 40, 21, 20))
        self.dateEdit_hasta = QDateEdit(self.frame_descargar_pdfs)
        self.dateEdit_hasta.setObjectName(u"dateEdit_hasta")
        self.dateEdit_hasta.setGeometry(QRect(170, 40, 110, 22))
        self.btn_ingresos_egresos = QPushButton(self.frame_descargar_pdfs)
        self.btn_ingresos_egresos.setObjectName(u"btn_ingresos_egresos")
        self.btn_ingresos_egresos.setGeometry(QRect(20, 80, 281, 24))
        self.btn_ventas_producto = QPushButton(self.frame_descargar_pdfs)
        self.btn_ventas_producto.setObjectName(u"btn_ventas_producto")
        self.btn_ventas_producto.setGeometry(QRect(20, 110, 281, 24))
        self.btn_ventas_talle = QPushButton(self.frame_descargar_pdfs)
        self.btn_ventas_talle.setObjectName(u"btn_ventas_talle")
        self.btn_ventas_talle.setGeometry(QRect(20, 140, 281, 24))
        self.pila_menu.addWidget(self.reportes)

        self.verticalLayout_3.addWidget(self.pila_menu)




        self.horizontalLayout.addWidget(self.frame_izquierda)

        self.carrito = QFrame(self.frameFondo)
        self.carrito.setObjectName(u"carrito")
        self.carrito.setFrameShape(QFrame.Shape.StyledPanel)
        self.carrito.setFrameShadow(QFrame.Shadow.Raised)
        self.label_titulo_venta = QLabel(self.carrito)
        self.label_titulo_venta.setObjectName(u"label_titulo_venta")
        self.label_titulo_venta.setGeometry(QRect(70, 0, 201, 41))
        self.label_titulo_venta.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_total = QLabel(self.carrito)
        self.label_total.setObjectName(u"label_total")
        self.label_total.setGeometry(QRect(60, 550, 91, 41))
        self.combo_medio_pago = QComboBox(self.carrito)
        self.combo_medio_pago.setObjectName(u"combo_medio_pago")
        self.combo_medio_pago.setGeometry(QRect(80, 600, 191, 22))
        self.label_monto_total = QLabel(self.carrito)
        self.label_monto_total.setObjectName(u"label_monto_total")
        self.label_monto_total.setGeometry(QRect(170, 560, 121, 31))
        self.lista_detalle_venta = QListWidget(self.carrito)
        self.lista_detalle_venta.setObjectName(u"lista_detalle_venta")
        self.lista_detalle_venta.setGeometry(QRect(10, 50, 311, 491))
        self.lista_detalle_venta.setStyleSheet(u"QListWidget {\n"
                                           "        background-color: #b8b6b2; /* Color de fondo gris claro */\n"
                                           "        border: 1px solid #ccc; /* Borde gris */\n"
                                           "        padding: 0px;\n"
                                           "    }\n"
                                           "    \n"
                                           "    QListWidget::item {\n"
                                           "        background-color: white; /* Fondo de cada item */\n"
                                           "        border: 1px solid transparent; /* Borde invisible */\n"
                                           "        padding: 0px ;\n"
                                           "        margin-bottom: 1px;\n"
                                           "    }\n"
                                           "\n"

                                           "\n"
                                           "    QListWidget::item:hover {\n"
                                           "        background-color: #e0e0e0; /* Fondo gris claro al pasar el mouse */\n"
                                           "    }")
        self.btn_limpiar = QPushButton(self.carrito)
        self.btn_limpiar.setObjectName(u"btn_limpiar")
        self.btn_limpiar.setGeometry(QRect(30, 640, 121, 51))
        self.btn_vender = QPushButton(self.carrito)
        self.btn_vender.setObjectName(u"btn_vender")
        self.btn_vender.setGeometry(QRect(180, 640, 121, 51))

        self.horizontalLayout.addWidget(self.carrito)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)

        self.horizontalLayout_3.addWidget(self.frameFondo)

        VentanaPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaPrincipal)




        QMetaObject.connectSlotsByName(VentanaPrincipal)
    # setupUi

    def retranslateUi(self, VentanaPrincipal):
        VentanaPrincipal.setWindowTitle(QCoreApplication.translate("VentanaPrincipal", u"Boutique sue\u00f1o amarillo", None))
        self.btn_venta_productos.setText(QCoreApplication.translate("VentanaPrincipal", u"Venta Productos", None))
        self.btn_stock.setText(QCoreApplication.translate("VentanaPrincipal", u"Modificaciones Stock", None))
        self.btn_cambios.setText(QCoreApplication.translate("VentanaPrincipal", u"Cambiar o Cancelar", None))
        self.btn_reportes.setText(QCoreApplication.translate("VentanaPrincipal", u"Reportes", None))
        self.btn_agregar_gasto.setText(QCoreApplication.translate("VentanaPrincipal", u"Agregar un Gasto", None))
        self.btn_modificar_cantidades.setText(QCoreApplication.translate("VentanaPrincipal", u"Modificar cantidades", None))
        self.btn_agregar_producto.setText(QCoreApplication.translate("VentanaPrincipal", u"Agregar nuevo producto", None))
        self.btn_agregar_combo.setText(QCoreApplication.translate("VentanaPrincipal", u"Agregar Combo", None))
        self.btn_modificar_precios.setText(QCoreApplication.translate("VentanaPrincipal", u"Modificar precios", None))
        self.btn_cancelar_venta.setText(QCoreApplication.translate("VentanaPrincipal", u"Cancelar la venta", None))
        self.btn_cambiar_producto.setText(QCoreApplication.translate("VentanaPrincipal", u"Cambiar un producto", None))
        self.total_vendido.setText(QCoreApplication.translate("VentanaPrincipal", u"$120.000", None))
        self.lbl_total_vendido.setText(QCoreApplication.translate("VentanaPrincipal", u"Total Vendido", None))
        self.lbl_total_efectivo.setText(QCoreApplication.translate("VentanaPrincipal", u"Total Efectivo", None))
        self.total_efectivo.setText(QCoreApplication.translate("VentanaPrincipal", u"$120.000", None))
        self.lbl_total_tarjetas.setText(QCoreApplication.translate("VentanaPrincipal", u"Total PosNet", None))
        self.total_tarjetas.setText(QCoreApplication.translate("VentanaPrincipal", u"$120.000", None))
        self.lbl_total_transferencia.setText(QCoreApplication.translate("VentanaPrincipal", u"Total Transferencia", None))
        self.total_transferencia.setText(QCoreApplication.translate("VentanaPrincipal", u"$120.000", None))
        self.label_faltante_stock.setText(QCoreApplication.translate("VentanaPrincipal", u"Faltantes de Stock", None))
        self.label_descarga_reportes.setText(QCoreApplication.translate("VentanaPrincipal", u"Descarga de Reportes", None))
        self.label_y.setText(QCoreApplication.translate("VentanaPrincipal", u"Y", None))
        self.btn_ingresos_egresos.setText(QCoreApplication.translate("VentanaPrincipal", u"Ingresos y Egresos", None))
        self.btn_ventas_producto.setText(QCoreApplication.translate("VentanaPrincipal", u"Ventas por producto", None))
        self.btn_ventas_talle.setText(QCoreApplication.translate("VentanaPrincipal", u"Ventas por talle", None))
        self.label_titulo_venta.setText(QCoreApplication.translate("VentanaPrincipal", u"Resumen de Venta", None))
        self.label_total.setText(QCoreApplication.translate("VentanaPrincipal", u"Total", None))
        self.combo_medio_pago.setCurrentText("")
        self.combo_medio_pago.setPlaceholderText(QCoreApplication.translate("VentanaPrincipal", u"", None))
        self.label_monto_total.setText(QCoreApplication.translate("VentanaPrincipal", u"", None))
        self.btn_limpiar.setText(QCoreApplication.translate("VentanaPrincipal", u"Limpiar", None))
        self.btn_vender.setText(QCoreApplication.translate("VentanaPrincipal", u"Vender", None))
    # retranslateUi

