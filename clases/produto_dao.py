from clases.producto import Producto, TalleProducto
from conexion import Conexion


class ProductoDAO:
    SELECCIONAR = """
    SELECT 
        p.idProducto,
        p.nombreProducto,
        t.idTalle,
        t.talle,
        tp.stock,
        tp.precio_efectivo,
        tp.precio_tarjeta 
    FROM Producto p
    JOIN Talle_Producto tp ON p.idProducto = tp.idProducto
    JOIN Talle t ON tp.idTalle = t.idTalle
    WHERE tp.stock > 0
    ORDER BY p.idProducto, t.idTalle
    """


    @classmethod
    def seleccionar_productos_venta(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros= cursor.fetchall()
            productos_dict = {}
            for idProducto, nombre, idTalle, talle, stock, precio_efectivo, precio_tarjeta in registros:
                if idProducto not in productos_dict:
                    productos_dict[idProducto] = Producto(idProducto, nombre)
                productos_dict[idProducto].talles.append(TalleProducto(idTalle, talle, stock, precio_efectivo, precio_tarjeta))
            return list(productos_dict.values())
        except Exception as e:
            return f'Ocurrio un error al seleccionar Clientes {e}'
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


if __name__ == '__main__':
    for p in ProductoDAO.seleccionar_productos_venta():
        print(p.obtener_datos())
        for t in p.talles:
            print(f"  - Talle: {t.talle}, Stock: {t.stock}, Precio: ${t.precio}")
