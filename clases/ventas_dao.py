from clases.ventas import Venta, DetalleVentaProducto, DetalleVentaCombo, DetalleVentaProductoCombo
from conexion import Conexion


class ventasDAO:
    SELECCIONAR = """
    SELECT
        v.idVenta,
        v.total_venta,
        v.fecha,
        mp.nombre AS metodo_pago,
        cl.nombre AS cliente
    FROM Venta v
    JOIN Metodo_Pago mp ON v.idMetodo_Pago = mp.idMetodo_Pago
    LEFT JOIN Cliente cl ON v.idCliente = cl.idCliente
    ORDER BY v.fecha DESC;
    """
    SELECTFECHA = """"
    SELECT
            v.idVenta,
            v.total_venta,
            v.fecha,
            mp.nombre AS metodo_pago,
            cl.nombre AS cliente
        FROM Venta v
        JOIN Metodo_Pago mp ON v.idMetodo_Pago = mp.idMetodo_Pago
        LEFT JOIN Cliente cl ON v.idCliente = cl.idCliente
        WHERE v.fecha == %s
        ORDER BY v.fecha DESC;
        """

    SELECTDETALLESVENTAS = """
    SELECT
        dvp.idDetalle_Venta_Producto,
        dvp.idVenta,dvp.id_producto,dvp.id_talle, dvp.cantidad, dvp.precio_unitario, dvp.precio_total 
    FROM Detalle_Venta_Producto dvp
    WHERE dvp.idVenta == %s
    ORDER BY dvp.idProducto;
        """
    SELECTDETALLESVENTASCOMBOS = """"
    SELECT
        dvc.id_detalle_venta_combo, dvc.id_venta, dvc.id_combo
    FROM Detalle_Venta_Combo dvc
    WHERE dvc.idVenta == %s
    ORDER BY dvc.id_combo;
    """
    SELECTDETALLEVENTAPRODUCTOCOMBO = """
    SELECT
        dvpc.id_detalle_venta_producto_combo, dvpc.id_detalle_venta, dvpc.id_producto, dvpc.id_talle, cantidad
    FROM Detalle_Venta_Producto_Combo dvpc
    WHERE dvpc.id_detalle_venta_producto == %s
    ORDER BY dvpc.id_producto;    
    """
    
        

    @classmethod
    def seleccionar_ventas(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            ventas = []
            for id_venta, total, fecha,metodo_pago, id_cliente in registros:
                if id_cliente:
                    v = Venta(id_venta, total, metodo_pago, id_cliente)
                else:
                    v = Venta(id_venta, total, metodo_pago)
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
            for id_venta, total, metodo_pago, id_cliente in registros:
                if id_cliente:
                    v = Venta(id_venta, total, metodo_pago, id_cliente)
                else:
                    v = Venta(id_venta, total, metodo_pago)
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
            valores = (nro_venta)
            cursor.execute(cls.SELECCIONAR, valores)#cambiar la sentencia
            registros = cursor.fetchall()
            detalles_ventas = []
            for id_detalle_venta_producto, id_venta, id_producto,id_talle, cantidad, precio_unitario, precio_total in registros:
                dv = DetalleVentaProducto(id_detalle_venta_producto, id_venta, id_producto,id_talle, cantidad, precio_unitario, precio_total)
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
            valores = (nro_venta)
            cursor.execute(cls.SELECCIONAR, valores)
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
            valores = (nro_venta_combo)
            cursor.execute(cls.SELECCIONAR, valores)
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

if __name__ == '__main__':
   pass