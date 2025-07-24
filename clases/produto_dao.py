from multiprocessing.resource_tracker import register

from clases.combo import Combo
from clases.producto import Producto, TalleProducto
from clases.ventas import Talle
from conexion import Conexion


class ProductoDAO:
    SELECCIONAR_PRODUCTOS = """
    SELECT
        p.idProducto,
        p.nombreProducto,
        p.precio
    FROM Producto p
    ORDER BY p.idProducto;
    """

    SELECCIONAR_TALLES = """
    SELECT 
        p.idProducto,
        t.idTalle,
        t.talle,
        tp.stock
    FROM Producto p
    JOIN Talle_Producto tp ON p.idProducto = tp.idProducto
    JOIN Talle t ON tp.idTalle = t.idTalle
    WHERE p.idProducto = %s 
    AND tp.stock > 0 
    ORDER BY p.idProducto, t.idTalle
    """

    SELECCIONAR = """
    SELECT 
        p.idProducto,
        p.nombreProducto,
        t.idTalle,
        t.talle,
        tp.stock
    FROM Producto p
    JOIN Talle_Producto tp ON p.idProducto = tp.idProducto
    JOIN Talle t ON tp.idTalle = t.idTalle

    ORDER BY p.idProducto, t.idTalle
    """

    SELECCIONAR_COMBOS = """
    SELECT
        c.idCombo, 
        c.nombre, 
        c.precio 
        FROM combo c 
        ORDER BY c.idCombo;
        
        """
        

    @classmethod
    def seleccionar_productos(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR_PRODUCTOS)
            registros = cursor.fetchall()
            productos = []
            for id_producto, nombre, precio in registros:
                producto = Producto(id_producto, nombre, precio)
                productos.append(producto)
            return productos
        except Exception as e:
            return f'Ocurrio un error al seleccionar Productos {e}'
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def seleccionar_talles(cls, id_producto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (id_producto, )
            cursor.execute(cls.SELECCIONAR_TALLES, valores)
            registros = cursor.fetchall()
            talles = []
            for idProducto, id_talle, talle, stock in registros:
                talle = TalleProducto(id_talle, talle, stock)
                talles.append(talle)
            return talles
        except Exception as e:
            return f'Ocurrio un error al seleccionar Talles {e}'
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def seleccionar_productos_venta(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros= cursor.fetchall()
            productos_dict = {}
            for idProducto, nombre, id_talle, talle, stock in registros:
                if idProducto not in productos_dict:
                    productos_dict[idProducto] = Producto(idProducto, nombre)
                productos_dict[idProducto].talles.append(TalleProducto(id_talle, talle, stock))
            return list(productos_dict.values())
        except Exception as e:
            return f'Ocurrio un error al seleccionar Clientes {e}'
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def seleccionar_combos(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR_COMBOS)
            registros = cursor.fetchall()
            combos = []

            for idCombo, nombreCombo, precioCombo in registros:
                # Si el combo no existe, lo creamos

                combo = Combo(idCombo, nombreCombo, precioCombo)

                combos.append(combo)
            return combos

        except Exception as e:
            return f'Ocurrió un error al seleccionar Combos: {e}'

        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == '__main__':
    for p in ProductoDAO.seleccionar_productos_venta():
        print(p.nombre, p.id)
        for t in p.talles:
            print(t.talle, t.stock, t.precio_efectivo, t.precio_tarjeta)
        # for producto in p.productos:
        #     print(producto.nombre)
        #     for talle in producto.talles:
        #         print(talle.talle)

