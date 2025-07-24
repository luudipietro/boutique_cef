from conexion import Conexion


class AgregarStockDAO:
    AGREGAR_STOCK = """
    UPDATE talle_producto
    SET stock = stock + %s 
    WHERE idProducto = %s AND idTalle = %s
    """

    @classmethod
    def agregar_stock(cls, id_producto, id_talle, cantidad):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cantidad, id_producto, id_talle)
            cursor.execute(cls.AGREGAR_STOCK, valores)
            conexion.commit()
        except Exception as e:
            return f'Ocurrio un error al agregar Stock {e}'

        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
