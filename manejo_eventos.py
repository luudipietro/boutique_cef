import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        self.boton = QPushButton('Click Aqui')

        self.boton.clicked.connect(self.evento_click)

        self.setCentralWidget(self.boton)

    def evento_click(self):
        self.boton.setText('Nuevo Texto')
        self.setEnabled(False)
        self.setWindowTitle('Nuevo Titulo de nuestra app')

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
