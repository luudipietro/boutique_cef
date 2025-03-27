import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QCheckBox, QComboBox, QListWidget


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        self.setFixedSize(500,600)

        # checkbox = QCheckBox('Este es un cbox')
        # #activamos el 3er estado
        # checkbox.setTristate(True)
        # #conectar la señal de cambio de componente
        # checkbox.stateChanged.connect(self.mostrar_estado)
        #
        # self.setCentralWidget(checkbox)
        #creamos un comp label
        # etiqueta = QLabel('Hola')
        # etiqueta.setPixmap(QPixmap('layla.jpg'))
        # etiqueta.setScaledContents(True)


        # etiqueta.setText('Texto cambiado')
        #
        # fuente = etiqueta.font()
        # fuente.setPointSize(25)
        # etiqueta.setFont(fuente)
        # #modificar la alineacion de la eiqueta
        # etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        #publicamos el componente
        # self.setCentralWidget(etiqueta)

        # #COMBO BOX
        # combobox = QComboBox()
        # lista = ['uno', 'dos', 'tres']
        # lista.sort()
        # combobox.addItems(lista)
        # #monitoreamos el cambipo de elemento seleccionado
        # combobox.currentIndexChanged.connect(self.cambio_indice)
        # combobox.currentTextChanged.connect(self.cambio_texto)
        # #hacemos editable el combo box
        # combobox.setEditable(True)
        # #especificamos la politica de insercion
        # #combobox.setInsertPolicy(QComboBox.NoInsert)
        # # combobox.setInsertPolicy(QComboBox.InsertAtTop)
        # # combobox.setInsertPolicy(QComboBox.InsertAtCurrent)
        # # combobox.setInsertPolicy(QComboBox.InsertAtBottom)
        # combobox.setInsertPolicy(QComboBox.InsertAlphabetically)
        #
        # combobox.setMaxCount(6)
        #
        # self.setCentralWidget(combobox)

        #QLIST WIDGET se parece al combobox
        lista = QListWidget()
        lista.addItems(['uno', 'dos', 'tres'])
        lista.currentItemChanged.connect(self.cambio_elemento)
        lista.currentTextChanged.connect(self.cambio_texto)
        self.setCentralWidget(lista)


    def cambio_elemento(self, nuevo_elemento):
        print(f'nuiev elem selec: {nuevo_elemento}')

    def cambio_indice(self, nuevo_indice):
        print(f'Nuevo indice seleccionado: {nuevo_indice}')
    def cambio_texto(self, nuevo_texto):
        print(f'Nuevo texto seleccionado: {nuevo_texto}')

    def mostrar_estado(self, estado):
        print(f'Estado chekbox {estado}')
if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())
