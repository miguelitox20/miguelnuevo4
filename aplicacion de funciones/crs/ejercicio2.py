
factura = []

def agregar_producto(nombre, precio, descuento=None):

    if descuento is None:
        descuento = 0.10  
    precio_final = calcular_precio_final(precio, descuento)
    producto = {
        "nombre": nombre,
        "precio": precio,
        "descuento": descuento,
        "precio_final": precio_final
    }
    factura.append(producto)

def calcular_precio_final(precio, descuento):
   
    return precio - (precio * descuento)

def mostrar_factura():
   
    total = 0
    print("Factura:")
    print("Nombre del Producto | Precio | Descuento | Precio Final")
    for producto in factura:
        print(f"{producto['nombre']} | ${producto['precio']} | {producto['descuento']*100}% | ${producto['precio_final']}")
        total += producto['precio_final']
    print(f"Total a pagar: ${total}")

def producto_mayor_valor():
    
    if not factura:
        print("La factura está vacía.")
        return
    producto_mayor = max(factura, key=lambda p: p["precio_final"])
    print(f"Producto de mayor valor: {producto_mayor['nombre']} con precio final de ${producto_mayor['precio_final']}")

# Ejemplo de uso
agregar_producto("Producto A", 100, 0.15)  # Con descuento del 15%
agregar_producto("Producto B", 200)        # Descuento por defecto del 10%
agregar_producto("Producto C", 150, 0.05)  # Con descuento del 5%

mostrar_factura()
producto_mayor_valor()
