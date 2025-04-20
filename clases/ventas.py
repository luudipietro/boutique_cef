class Venta:
    def __init__(self, id_venta, total, metodo_pago,nro_recibo,id_cliente=None, fecha=None):
        self.id_venta = id_venta
        self.total = total
        self.metodo_pago = metodo_pago
        self.nro_recibo = nro_recibo
        self.fecha = fecha
        self.id_cliente = id_cliente

class DetalleVentaProducto:
    def __init__(self, id_detalle_venta_producto, id_venta, id_producto, id_talle, precio_unitario,nombre_producto=None,talle=None):
        self.id_detalle_venta_producto = id_detalle_venta_producto
        self.id_venta = id_venta
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.id_talle = id_talle
        self.talle = talle
        self.precio_unitario = precio_unitario

    def cambiar_talle(self, talle_nuevo):
        self.id_talle = talle_nuevo

class DetalleVentaCombo:
    def __init__(self, id_detalle_venta_combo, id_venta, id_combo):
        self.id_detalle_venta_combo = id_detalle_venta_combo
        self.id_venta = id_venta
        self.id_combo = id_combo

class DetalleVentaProductoCombo:
    def __init__(self, id_detalle_venta_producto_combo, id_detalle_venta, id_producto, id_talle, cantidad):
        self.id_detalle_venta_combo = id_detalle_venta_producto_combo
        self.id_detalle_venta = id_detalle_venta
        self.id_producto = id_producto
        self.id_talle = id_talle
        self.cantidad= cantidad

class Talle:
    def __init__(self, id_talle, talle):
        self.id_talle= id_talle
        self.talle= talle