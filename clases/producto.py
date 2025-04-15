class Producto:
    def __init__(self,id=None, nombre=None, descripcion=None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.talles = []

    def obtener_datos(self):
        return self.__id, self.__nombre, self.__descripcion

class TalleProducto:
    def __init__(self, idTalle, talle, stock, precio_efectivo, precio_tarjeta):
        self.idTalle= idTalle
        self.talle = talle
        self.stock = stock
        self.precio_efectivo = precio_efectivo
        self.precio_tarjeta = precio_tarjeta

