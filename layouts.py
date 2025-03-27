from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout


class Color(QWidget):
    def __init__(self, nuevo_color):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta_colores= self.palette()
        paleta_colores.setColor(QPalette.Window, QColor(nuevo_color))

        self.setPalette(paleta_colores)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Layouts en PySide')
        #layouts anidados
        layout_horizontal = QHBoxLayout()
        #Layout Vertical
        layout_vertical = QVBoxLayout()

        layout_vertical.addWidget(Color('red'))
        layout_vertical.addWidget(Color('yellow'))
        layout_vertical.addWidget(Color('green'))

        layout_horizontal.addLayout(layout_vertical)
        layout_horizontal.addWidget(Color('blue'))
        #crear componente generico p poder pub;licar el layout
        componente = QWidget()
        componente.setLayout(layout_horizontal)


        self.setCentralWidget(componente)

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()

