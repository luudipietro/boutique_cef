import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

#clase base de QT(PySide)
#se encarga de procesar los eventos (event loop)
app = QApplication()

#creamos un objeto ventana
#cualq componente puede ser una ventana en PYside
#ventana = QPushButton('Boton Pyside')
ventana = QMainWindow()
#mostrar la ventana
ventana.setWindowTitle('Hola mundo')
ventana.resize(1300,700)
ventana.show()
#Se ejecuta la aplicacion
sys.exit(app.exec())


