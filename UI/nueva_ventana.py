from PySide6.QtWidgets import QWidget, QDialog


class NuevaVentana(QDialog):
    def __init__(self, titulo_ventana):
        super().__init__()
        self.setModal(True)
        self.setWindowTitle(titulo_ventana)
