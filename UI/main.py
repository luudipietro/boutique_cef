from PySide6.QtWidgets import QMainWindow, QApplication

from UI.ventanaPrincipal3 import Ui_VentanaPrincipal


class Inicio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VentanaPrincipal()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication([])
    ventana = Inicio()
    ventana.show()
    app.exec()