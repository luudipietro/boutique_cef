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
        ORDER BY v.fecha DESC;
        """