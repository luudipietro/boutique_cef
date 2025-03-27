from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QMainWindow, QGridLayout, QApplication, QWidget, QStackedLayout


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
        self.setWindowTitle('Layout en grid')
        self.setFixedSize(800,600)

        # layout_grid = QGridLayout()
        # layout_grid.addWidget(Color('red'),0,0)
        # layout_grid.addWidget(Color('red'), 0, 2)
        # layout_grid.addWidget(Color('red'), 1, 1)
        #qStacked layout
        layout = QStackedLayout()
        #por default solo se visualiza el primer widget agregado
        # layout.addWidget(Color('red'))
        # layout.addWidget(Color('blue'))
        # layout.addWidget(Color('green'))
        # layout.setCurrentIndex(1)

        

        componente = QWidget()
        componente.setLayout(layout)
        self.setCentralWidget(componente)



if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()