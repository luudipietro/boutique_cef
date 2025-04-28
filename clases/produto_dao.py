from clases.combo import Combo
from clases.producto import Producto, TalleProducto
from clases.ventas import Talle
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

    SELECCIONAR_COMBOS = """
    SELECT
        c.idCombo, 
        c.nombre, 
        c.precio, 
        p.idProducto,
        p.nombreProducto,
        t.idTalle,
        t.Talle  
        FROM combo c 
        JOIN producto_combo pc ON c.idCombo = pc.idCombo 
        JOIN producto p ON pc.idProducto = p.idProducto 
        JOIN talle_producto tp ON p.idProducto = tp.idProducto 
        JOIN talle t ON tp.idTalle = t.idTalle 
        WHERE tp.stock >0
        ORDER BY c.idCombo;
        
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

    @classmethod
    def seleccionar_combos(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR_COMBOS)
            registros = cursor.fetchall()
            combos_dict = {}

            for idCombo, nombreCombo, precioCombo, idProducto, nombreProducto, idTalle, talle in registros:
                # Si el combo no existe, lo creamos
                if idCombo not in combos_dict:
                    combos_dict[idCombo] = Combo(idCombo, nombreCombo, precioCombo)

                # Buscamos el producto en los productos del combo
                combo = combos_dict[idCombo]
                producto_existente = next((p for p in combo.productos if p.id == idProducto), None)

                if not producto_existente:
                    # Si no existe, lo creamos y lo agregamos al combo
                    producto_existente = Producto(idProducto, nombreProducto)
                    combo.productos.append(producto_existente)

                # Agregamos el talle al producto
                producto_existente.talles.append(Talle(idTalle, talle))

            return list(combos_dict.values())

        except Exception as e:
            return f'Ocurrió un error al seleccionar Combos: {e}'

        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == '__main__':
    for p in ProductoDAO.seleccionar_combos():
        print(p.nombre, p.precio)
        for producto in p.productos:
            print(producto.nombre)
            for talle in producto.talles:
                print(talle.talle)

