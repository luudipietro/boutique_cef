from clases.ventas import Venta, DetalleVentaProducto, DetalleVentaCombo, DetalleVentaProductoCombo, Talle
from conexion import Conexion


class VentasDAO:
    SELECCIONAR = """
    SELECT
        v.idVenta,
        v.total_venta,
        mp.nombre AS metodo_pago,
        cl.nombre AS cliente,
        v.nro_recibo,
        v.fecha
    FROM Venta v
    JOIN Metodo_Pago mp ON v.idMetodo_Pago = mp.idMetodo_Pago
    LEFT JOIN Cliente cl ON v.idCliente = cl.idCliente
    ORDER BY v.nro_recibo DESC;
    """
    SELECTFECHA = """
    SELECT
            v.idVenta,
            v.total_venta,
            mp.nombre AS metodo_pago,
            cl.nombre AS cliente,
            v.nro_recibo
        FROM Venta v
        JOIN Metodo_Pago mp ON v.idMetodo_Pago = mp.idMetodo_Pago
        LEFT JOIN Cliente cl ON v.idCliente = cl.idCliente
        WHERE DATE(v.fecha) = %s
        ORDER BY v.fecha DESC;
        """


    SELECTDETALLESVENTAS = """
    SELECT
        dvp.idDetalle_Venta,
        dvp.idVenta,
        dvp.idProducto,
        p.nombreProducto,
        dvp.idTalle,
        t.talle, 
        dvp.precio_unitario  
    FROM Detalle_Venta_Producto dvp
    JOIN Producto p ON dvp.idProducto = p.idProducto
    JOIN Talle t ON dvp.idTalle= t.idTalle
    WHERE dvp.idVenta = %s
    ORDER BY dvp.idProducto;
        """
    SELECTDETALLESVENTASCOMBOS = """"
    SELECT
        dvc.idDetalle_Venta_Combo, dvc.Venta_idVenta, dvc.Combo_idCombo
    FROM Detalle_Venta_Combo dvc
    WHERE dvc.Venta_idVenta = 1
    ORDER BY dvc.Combo_idCombo;
    """
    SELECTDETALLEVENTAPRODUCTOCOMBO = """
    SELECT
        dvpc.idDetalle_Venta_Producto_Combo, 
        dvpc.idDetalle_Venta_Combo, 
        dvpc.idProducto, 
        dvpc.idTalle, cantidad
    FROM Detalle_Venta_Producto_Combo dvpc
    WHERE dvpc.idDetalle_Venta_Producto_Combo = 1
    ORDER BY idProducto;  
    """
    SELECTANIDADO = """
     SELECT
        dvpc.idDetalle_Venta_Producto_Combo, 
        dvpc.idDetalle_Venta_Combo, 
        dvpc.idProducto, 
        dvpc.idTalle, cantidad
    FROM Detalle_Venta_Producto_Combo dvpc
    JOIN detalle_venta_combo dvc ON dvpc.idDetalle_Venta_Combo = dvc.idDetalle_Venta_Combo
    WHERE dvc.Venta_idVenta = %s
    ORDER BY idProducto;  
    """

    SELECTTALLESDISPOCAMBIO = """
    SELECT tp.idTalle, t.talle  FROM talle_producto AS tp JOIN talle t ON tp.idTalle = t.idTalle WHERE tp.idProducto = %s AND tp.stock >0;
    """

    @classmethod
    def seleccionar_talles_cambio(cls, id_prod):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (id_prod,)
            cursor.execute(cls.SELECTTALLESDISPOCAMBIO, valores)
            registros = cursor.fetchall()
            talles = []

            for id_talle, talle in registros:
                t = Talle(id_talle, talle)
                talles.append(t)

            return talles
        except Exception as e:
            return f'Ocurrio un error al seleccionar Talles {e}'
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def seleccionar_ventas(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            ventas = []

            for id_venta, total, metodo_pago, cliente, nro_recibo, fecha in registros:
                if cliente:
                    v = Venta(id_venta, total, metodo_pago, nro_recibo, cliente, fecha)
                else:
                    v = Venta(id_venta, total, metodo_pago, nro_recibo, 'Cliente no existe ', fecha)
                ventas.append(v)

            return ventas
        except Exception as e:
            return f'Ocurrio un error al seleccionar Ventas {e}'
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def seleccionar_ventas_fecha(cls, fecha):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (fecha,)
            cursor.execute(cls.SELECTFECHA, valores)
            registros = cursor.fetchall()
            ventas = []
            for id_venta, total, metodo_pago, cliente, nro_recibo in registros:
                if cliente:
                    v = Venta(id_venta, total, metodo_pago, nro_recibo, cliente)
                else:
                    v = Venta(id_venta, total, metodo_pago,nro_recibo, 'Cliente no existe ')
                ventas.append(v)

            return ventas
        except Exception as e:
            return f'Ocurrio un error al seleccionar Ventas {e}'
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def seleccionar_detalles_venta(cls, nro_venta):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (nro_venta, )
            cursor.execute(cls.SELECTDETALLESVENTAS, valores)#cambiar la sentencia
            registros = cursor.fetchall()
            detalles_ventas = []
            for id_detalle_venta_producto, id_venta, id_producto, nombre_producto,id_talle,talle, precio_unitario in registros:
                dv = DetalleVentaProducto(id_detalle_venta_producto, id_venta, id_producto,id_talle, precio_unitario, nombre_producto, talle)
                detalles_ventas.append(dv)

            return detalles_ventas
        except Exception as e:
            return f'Ocurrio un error al seleccionar detalles de Ventas {e}'
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def seleccionar_combo_venta(cls, nro_venta):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (nro_venta,)
            cursor.execute(cls.SELECTDETALLESVENTASCOMBOS, valores)
            registros = cursor.fetchall()
            detalles_ventas = []
            for id_detalle_venta_combo, id_venta, id_combo in registros:
                dv = DetalleVentaCombo(id_detalle_venta_combo, id_venta, id_combo)
                detalles_ventas.append(dv)

            return detalles_ventas
        except Exception as e:
            return f'Ocurrio un error al seleccionar detalles de Ventas de combos {e}'
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


    @classmethod
    def seleccionar_producto_combo(cls, nro_venta_combo):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (nro_venta_combo,)
            cursor.execute(cls.SELECTDETALLEVENTAPRODUCTOCOMBO, valores)
            registros = cursor.fetchall()
            detalles_ventas = []
            for id_detalle_venta_producto_combo, id_detalle_venta, id_producto, id_talle, cantidad in registros:
                dv = DetalleVentaProductoCombo(id_detalle_venta_producto_combo, id_detalle_venta, id_producto, id_talle, cantidad)
                detalles_ventas.append(dv)

            return detalles_ventas
        except Exception as e:
            return f'Ocurrio un error al seleccionar detalles de Ventas de productos en combos {e}'
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def seleccionar_productos_combo_anidado(cls, nro_venta):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (nro_venta, )
            cursor.execute(cls.SELECTANIDADO, valores)
            registros = cursor.fetchall()
            detalles_ventas = []
            for id_detalle_venta_producto_combo, id_detalle_venta_combo, id_producto, id_talle, cantidad in registros:
                dv = DetalleVentaProductoCombo(id_detalle_venta_producto_combo, id_detalle_venta_combo, id_producto, id_talle,
                                               cantidad)
                detalles_ventas.append(dv)

            return detalles_ventas
        except Exception as e:
            return f'Ocurrio un error al seleccionar detalles de Ventas de productos en combos {e}'
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == '__main__':
    ventas = VentasDAO.seleccionar_ventas()
    detalle_prod = VentasDAO.seleccionar_detalles_venta(8)
    detalle_combo = VentasDAO.seleccionar_combo_venta(8)
    detalle_producto_combo = VentasDAO.seleccionar_productos_combo_anidado(8)


    print(f'total: {ventas[0].total} fecha {ventas[0].fecha}')
    print(f'detalle: {detalle_producto_combo}')
