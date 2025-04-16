class Venta:
    def __init__(self, id_venta, total, metodo_pago, id_cliente=None):
        self.id_venta = id_venta
        self.total = total
        self.metodo_pago = metodo_pago
        self.id_cliente = id_cliente

class DetalleVentaProducto:
    def __init__(self, id_detalle_venta_producto, id_venta, id_producto,id_talle, cantidad, precio_unitario, precio_total):
        self.id_detalle_venta_producto = id_detalle_venta_producto
        self.id_venta = id_venta
        self.id_producto = id_producto
        self.id_talle = id_talle
        self.cantidad = cantidad
        self.precio_total = precio_total
        self.precio_unitario = precio_unitario

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