from conexion import Conexion


class RealizarVentaDAO:

    INSERTAR_VENTA = """
    INSERT INTO venta (total_venta, idMetodo_Pago, fecha, idCliente, nro_recibo) 
    VALUES (%s, %s, NOW(), %s, %s);"""

    INSERTAR_DETALLE_PRODUCTO = """
    INSERT INTO detalle_venta_producto (idVenta, idProducto, idTalle, precio_unitario) 
    VALUES (%s, %s, %s, %s);
    """

    INSERTAR_VENTA_COMBO = """
    INSERT INTO detalle_venta_combo (Venta_idVenta, Combo_idCombo, precio) 
    VALUES (%s, %s, %s);
    """

    INSERTAR_DETALLE_COMBO = """
    INSERT INTO detalle_venta_producto_combo (idDetalle_Venta_Combo, idProducto, idTalle) 
    VALUES (%s, %s, %s);
    """

    DESCONTAR_STOCK = """
    UPDATE talle_producto 
    SET stock = stock - 1 
    WHERE idProducto = %s AND idTalle = %s;
    """

    ULTIMO_ID = 'SELECT LAST_INSERT_ID();'

    @classmethod
    def realizar_venta(cls, total_venta, id_metodo_pago, id_cliente, nro_recibo, productos = None, combos = None):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores_venta = (total_venta, id_metodo_pago, id_cliente, nro_recibo)
            cursor.execute(cls.INSERTAR_VENTA, valores_venta)


            cursor.execute(cls.ULTIMO_ID)
            id_venta = cursor.fetchall()[0][0]
            if productos is not None:
                for producto in productos:
                    valores_producto = (id_venta, producto[0], producto[1], producto[2])
                    cursor.execute(cls.INSERTAR_DETALLE_PRODUCTO, valores_producto)
                    cursor.execute(cls.DESCONTAR_STOCK, (producto[0], producto[1]))

            if combos is not None:
                for combo in combos:
                    valores_combo = (id_venta, combo[0], combo[1])
                    cursor.execute(cls.INSERTAR_VENTA_COMBO, valores_combo)

                    cursor.execute(cls.ULTIMO_ID)
                    id_combo = cursor.fetchall()[0][0]
                    for producto in combo[2]:
                        valores_producto_combo = (id_combo, producto[0], producto[1])
                        cursor.execute(cls.INSERTAR_DETALLE_COMBO, valores_producto_combo)
                        cursor.execute(cls.DESCONTAR_STOCK, (producto[0], producto[1]))






            conexion.commit()
        except Exception as e:
            return f'Ocurrio un error al insertar Venta {e}'

        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == '__main__':
    ventas = RealizarVentaDAO.realizar_venta(10,1,0,147, [(1,2,22500),(2,1,21500)],[(1,50000,[(1,1),(2,1),(3,11)]), (1,50000,[(1,3),(2,4),(3,13)])])




