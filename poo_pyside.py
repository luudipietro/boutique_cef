import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton


class VentanaPySide(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('POO con PySide')
        #self.resize(600,400)
        self.setFixedSize(QSize(600,400))

        self._agregar_componentes()

    def _agregar_componentes(self):
        menu = self.menuBar()
        menu_archivo = menu.addMenu('Archivo')
        accion_nuevo = QAction('Nuevo', self)
        menu_archivo.addAction(accion_nuevo)
        accion_nuevo.setStatusTip('Nuevo Archivo')
        self.statusBar().showMessage('Informacion de la barra de estado...')
        boton = QPushButton('Nuevo Boton')
        self.setCentralWidget(boton)

if __name__ =='__main__':
    app = QApplication([])
    ventana = VentanaPySide()
    ventana.show()
    sys.exit(app.exec())