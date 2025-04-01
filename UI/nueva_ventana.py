from PySide6.QtWidgets import QWidget, QDialog, QListView, QVBoxLayout


class NuevaVentana(QDialog):
    def __init__(self, titulo_ventana):
        super().__init__()
        self.setModal(True)
        self.resize(1000,700)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.setWindowTitle(titulo_ventana)
