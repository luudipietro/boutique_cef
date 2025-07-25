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
                               QStackedWidget, QVBoxLayout, QWidget, QCalendarWidget)

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


        self.btn_cancelar = QPushButton(self.frame_2)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.pressed.connect(lambda: self.pila_menu.setCurrentIndex(2))

        self.horizontalLayout_2.addWidget(self.btn_cancelar)

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
#         self.lista_productos.setStyleSheet(u"QListWidget {\n"
# "        background-color: #b8b6b2; /* Color de fondo gris claro */\n"
# "        border: 1px solid #ccc; /* Borde gris */\n"
# "        padding: 0px;\n"
# "    }\n"
# "    \n"
# "    QListWidget::item {\n"
# "        background-color: white; /* Fondo de cada item */\n"
# "        border: 1px solid transparent; /* Borde invisible */\n"
# "        padding: 0px ;\n"
# "        margin-bottom: 1px;\n"
# "    }\n"
# "\n"
#
# "\n"
# "    QListWidget::item:hover {\n"
# "        background-color: #e0e0e0; /* Fondo gris claro al pasar el mouse */\n"
# "    }")
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



        self.cancelar_venta = QWidget()
        self.cancelar_venta.setObjectName(u"cancelar_venta")
        self.frame_cancelar = QFrame(self.cancelar_venta)
        self.frame_cancelar.setObjectName(u"frame_cambios")
        self.frame_cancelar.setGeometry(QRect(0, 0, 651, 641))
        self.frame_cancelar.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_cancelar.setFrameShadow(QFrame.Shadow.Raised)
        self.lista_ventas_cancelar = QListWidget(self.frame_cancelar)
        self.lista_ventas_cancelar.setObjectName(u"lista_ventas_cancelar")
        self.lista_ventas_cancelar.setGeometry(QRect(20, 10, 621, 571))
        self.btn_cancelar_venta = QPushButton(self.frame_cancelar)
        self.btn_cancelar_venta.setObjectName(u"btn_cancelar_venta")
        self.btn_cancelar_venta.setGeometry(QRect(510, 590, 131, 41))

        self.pila_menu.addWidget(self.cancelar_venta)


        self.reportes = QWidget()
        self.reportes.setObjectName(u"reportes")

        self.layout_reportes = QVBoxLayout(self.reportes)

        self.layout_fecha = QHBoxLayout()

        self.fecha_ventas_dia = QDateEdit()
        self.fecha_ventas_dia.setCalendarPopup(True)
        self.fecha_ventas_dia.setObjectName(u"fecha_ventas_dia")

        self.layout_fecha.addWidget(self.fecha_ventas_dia)


        self.total_vendido = QLabel()
        self.total_vendido.setObjectName(u"total_vendido")

        self.layout_fecha.addWidget(self.total_vendido)
        self.total_efectivo = QLabel()
        self.total_efectivo.setObjectName(u"total_efectivo")

        self.layout_fecha.addWidget(self.total_efectivo)

        self.total_tarjetas = QLabel()
        self.total_tarjetas.setObjectName(u"total_tarjetas")

        self.layout_fecha.addWidget(self.total_tarjetas)
        self.total_transferencia = QLabel()
        self.total_transferencia.setObjectName(u"total_transferencia")

        self.layout_fecha.addWidget(self.total_transferencia)

        self.layout_reportes.addLayout(self.layout_fecha)

        self.layout_lista_ventas_dia = QVBoxLayout()
        self.lista_ventas_dia = QListWidget()
        self.lista_ventas_dia.setObjectName(u"lista_ventas_dia")
        #self.lista_ventas_dia.setMaximumHeight(300)
        #self.lista_ventas_dia.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        #self.lista_ventas_dia.setGeometry(QRect(0, 0, 200, 150))
        self.layout_lista_ventas_dia.addWidget(self.lista_ventas_dia)


        self.layout_reportes.addLayout(self.layout_lista_ventas_dia)

        self.layout_stock_y_pdf = QHBoxLayout()

        self.layout_alertas_stock= QVBoxLayout()
        self.frame_alertas_stock = QFrame()

        self.label_faltante_stock = QLabel()
        self.label_faltante_stock.setObjectName(u"label_faltante_stock")
        self.layout_alertas_stock.addWidget(self.label_faltante_stock)


        self.layout_stock_y_pdf.addLayout(self.layout_alertas_stock)


        self.layout_descargar_pdfs = QVBoxLayout()

        self.label_descarga_reportes = QLabel()
        self.label_descarga_reportes.setObjectName(u"label_descarga_reportes")

        self.layout_fecha_desde_hasta = QHBoxLayout()

        self.dateEdit_desde = QDateEdit()
        self.dateEdit_desde.setCalendarPopup(True)
        self.dateEdit_desde.setObjectName(u"dateEdit_desde")

        self.label_y = QLabel()
        self.label_y.setObjectName(u"label_y")

        self.dateEdit_hasta = QDateEdit()
        self.dateEdit_hasta.setCalendarPopup(True)
        self.dateEdit_hasta.setObjectName(u"dateEdit_hasta")

        self.layout_fecha_desde_hasta.addWidget(self.dateEdit_desde)
        self.layout_fecha_desde_hasta.addWidget(self.label_y)
        self.layout_fecha_desde_hasta.addWidget(self.dateEdit_hasta)

        self.btn_ingresos_egresos = QPushButton()
        self.btn_ingresos_egresos.setObjectName(u"btn_ingresos_egresos")

        self.btn_ventas_producto = QPushButton()
        self.btn_ventas_producto.setObjectName(u"btn_ventas_producto")

        self.btn_ventas_talle = QPushButton()
        self.btn_ventas_talle.setObjectName(u"btn_ventas_talle")

        self.layout_descargar_pdfs.addWidget(self.label_descarga_reportes)
        self.layout_descargar_pdfs.addLayout(self.layout_fecha_desde_hasta)
        self.layout_descargar_pdfs.addWidget(self.btn_ingresos_egresos)
        self.layout_descargar_pdfs.addWidget(self.btn_ventas_producto)
        self.layout_descargar_pdfs.addWidget(self.btn_ventas_talle)

        self.layout_stock_y_pdf.addLayout(self.layout_descargar_pdfs)
        self.layout_reportes.addLayout(self.layout_stock_y_pdf)

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
        # self.lista_detalle_venta.setStyleSheet(u"QListWidget {\n"
        #                                    "        background-color: #b8b6b2; /* Color de fondo gris claro */\n"
        #                                    "        border: 1px solid #ccc; /* Borde gris */\n"
        #                                    "        padding: 0px;\n"
        #                                    "    }\n"
        #                                    "    \n"
        #                                    "    QListWidget::item {\n"
        #                                    "        background-color: white; /* Fondo de cada item */\n"
        #                                    "        border: 1px solid transparent; /* Borde invisible */\n"
        #                                    "        padding: 0px ;\n"
        #                                    "        margin-bottom: 1px;\n"
        #                                    "    }\n"
        #                                    "\n"
        #
        #                                    "\n"
        #                                    "    QListWidget::item:hover {\n"
        #                                    "        background-color: #e0e0e0; /* Fondo gris claro al pasar el mouse */\n"
        #                                    "    }")
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

        self.btn_cancelar.setText(QCoreApplication.translate("VentanaPrincipal", u"Cancelar", None))
        self.btn_reportes.setText(QCoreApplication.translate("VentanaPrincipal", u"Reportes", None))
        self.btn_agregar_gasto.setText(QCoreApplication.translate("VentanaPrincipal", u"Agregar un Gasto", None))
        self.btn_modificar_cantidades.setText(QCoreApplication.translate("VentanaPrincipal", u"Modificar cantidades", None))
        self.btn_agregar_producto.setText(QCoreApplication.translate("VentanaPrincipal", u"Agregar nuevo producto", None))
        self.btn_agregar_combo.setText(QCoreApplication.translate("VentanaPrincipal", u"Agregar Combo", None))
        self.btn_modificar_precios.setText(QCoreApplication.translate("VentanaPrincipal", u"Modificar precios", None))
        self.btn_cancelar_venta.setText(QCoreApplication.translate("VentanaPrincipal", u"Cancelar la venta", None))

        self.total_vendido.setText(QCoreApplication.translate("VentanaPrincipal", u"", None))

        self.total_efectivo.setText(QCoreApplication.translate("VentanaPrincipal", u"", None))

        self.total_tarjetas.setText(QCoreApplication.translate("VentanaPrincipal", u"", None))

        self.total_transferencia.setText(QCoreApplication.translate("VentanaPrincipal", u"", None))
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

