from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QToolBar, QStatusBar


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Barra de Herramientas')
        self.setFixedSize(800, 600)

        #publicar un label
        etiqueta = QLabel('Hola')
        etiqueta.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(etiqueta)


        barra = QToolBar('Mi barra de herramientas')
        barra.setIconSize(QSize(16,16))
        self.addToolBar(barra)

        #agregamos un elemento a ntra barra
        boton_nuevo = QAction(QIcon('nuevo.png'),'Nuevo', self)
        barra.addAction(boton_nuevo)

        #creamos barra de estad
        self.setStatusBar(QStatusBar(self))
        boton_nuevo.setStatusTip('Nuevo Archivo')

        boton_nuevo.triggered.connect(self.click_boton_nuevo)
        #hacemos checable el boton
        #boton_nuevo.setCheckable(True)

    def click_boton_nuevo(self, s):
        print(f'Recibiendo Click {s}')



if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()