class Producto:
    def __init__(self,id=None, nombre=None, precio=None, descripcion=None):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.talles = []

    def obtener_datos(self):
        return self.__id, self.__nombre, self.__descripcion

class TalleProducto:
    def __init__(self, idTalle, talle, stock=None):
        self.idTalle= idTalle
        self.talle = talle
        self.stock = stock


