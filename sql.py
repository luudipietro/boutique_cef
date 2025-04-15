import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="tu_base"
)

cursor = conn.cursor()

# Insertar venta
cursor.execute("""
    INSERT INTO Venta (total_venta, idMetodo_Pago, fecha, idCliente)
    VALUES (%s, %s, NOW(), %s)
""", (1000.00, 1, 2))

venta_id = cursor.lastrowid

# Insertar detalle producto
cursor.execute("""
    INSERT INTO Detalle_Venta_Producto (idVenta, idProducto, idTalle, cantidad, precio_unitario)
    VALUES (%s, %s, %s, %s, %s)
""", (venta_id, 3, 1, 2, 500.00))

conn.commit()
cursor.close()
conn.close()
-- Insertar en la tabla Venta
INSERT INTO Venta (total_venta, idMetodo_Pago, fecha, idCliente)
VALUES (%s, %s, NOW(), %s);

-- Insertar en Detalle_Venta_Combo
INSERT INTO Detalle_Venta_Combo (idVenta, idCombo)
VALUES (%s, %s);

-- Luego insertar en Detalle_Venta_Producto_Combo
INSERT INTO Detalle_Venta_Producto_Combo (
    idDetalle_Venta_Combo,
    Talle_Producto_idProducto,
    idTalle,
    cantidad
) VALUES (%s, %s, %s, %s);



-- Insertar en la tabla Venta
INSERT INTO Venta (total_venta, idMetodo_Pago, fecha, idCliente)
VALUES (%s, %s, NOW(), %s);

-- Luego insertás los detalles:
INSERT INTO Detalle_Venta_Producto (idVenta, idProducto, idTalle, cantidad, precio_unitario)
VALUES (%s, %s, %s, %s, %s);


SELECT
    p.idProducto,
    p.nombreProducto,
    t.idTalle,
    t.talle,
    tp.stock
FROM Producto p
JOIN Talle_Producto tp ON p.idProducto = tp.idProducto
JOIN Talle t ON tp.idTalle = t.idTalle
ORDER BY p.idProducto, t.idTalle;


SELECT
    v.idVenta,
    v.fecha,
    v.total_venta,
    mp.nombre AS metodo_pago,
    cl.nombre AS cliente
FROM Venta v
JOIN Metodo_Pago mp ON v.idMetodo_Pago = mp.idMetodo_Pago
LEFT JOIN Cliente cl ON v.idCliente = cl.idCliente
WHERE v.idCliente <> 0
ORDER BY v.fecha DESC;


SELECT
    c.idCombo,
    c.nombre AS nombreCombo,
    p.idProducto,
    p.nombreProducto,
    t.idTalle,
    t.talle,
    tp.stock
FROM Combo c
JOIN Producto_Combo pc ON c.idCombo = pc.idCombo
JOIN Producto p ON pc.idProducto = p.idProducto
JOIN Talle_Producto tp ON p.idProducto = tp.idProducto
JOIN Talle t ON tp.idTalle = t.idTalle;


SELECT
    p.idProducto,
    p.nombreProducto,
    t.idTalle,
    t.talle,
    tp.stock
FROM Producto p
JOIN Talle_Producto tp ON p.idProducto = tp.idProducto
JOIN Talle t ON tp.idTalle = t.idTalle;
