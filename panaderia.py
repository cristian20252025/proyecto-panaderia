import json
import os
from datetime import datetime

def cargar_productos():
    try:
        with open("productos.json","r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return[]
    
productos = []

def guardar_productos():
    with open("productos.json","w") as file:
            return json.dump(productos,file, indent=4)
        
productos = cargar_productos()

def mostrar_productos():
    print(productos)
    
def crear_productos():
    codigo_producto=input("ingrese el codigo del producto")
    nombre=input("ingrese el nombre del producto")
    categoria=input("ingrese la categoria del producto")
    proveedor=input("proveedor del producto")
    cantidad_de_stock=float(input("ingrese cantidad para el stock"))
    precio_venta=float(input("ingrese precio del producto en venta"))
    precio_de_proveedor=float(input("ingrese precio del proveedor"))
    
    producto = {
        "codigo_producto" : codigo_producto,
        "nombre_producto" : nombre,
        "categoria_producto" : categoria,
        "proveedor_producto" : proveedor,
        "cantidad_de_stock" : cantidad_de_stock,
        "precio_venta" : precio_venta,
        "precio_de_proveedor" : precio_de_proveedor,
        }
    
    productos.append(producto)
    guardar_productos()
    print("el producto se ha agregado correctamente")

def cargar_pedidos():
    try:
        with open("pedidos.json","r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return[]
    
pedidos = []

def guardar_pedidos():
    with open("pedidos.json","w") as file:
            return json.dump(pedidos,file, indent=4)
        
pedidos = cargar_pedidos()

def mostrar_pedidos():
    print(crear_pedidos)
    
def crear_pedidos():
    codigo_producto=input("ingrese el codigo del producto")
    nombre=input("ingrese el nombre del producto")
    categoria=input("ingrese la categoria del producto")
    proveedor=input("proveedor del producto")
    cantidad_de_stock=float(input("ingrese cantidad para el stock"))
    precio_venta=float(input("ingrese precio del producto en venta"))
    precio_de_proveedor=float(input("ingrese precio del proveedor"))
    
    pedido = {
        "codigo_producto" : codigo_producto,
        "nombre_producto" : nombre,
        "categoria_producto" : categoria,
        "proveedor_producto" : proveedor,
        "cantidad_de_stock" : cantidad_de_stock,
        "precio_venta" : precio_venta,
        "precio_de_proveedor" : precio_de_proveedor,
        }
    
    pedidos.append(pedido)
    guardar_pedidos()
    print("el pedido se ha agregado correctamente")
    
# Archivos de datos
PRODUCTOS_FILE = "productos.json"
PEDIDOS_FILE = "pedidos.json"

# Cargar datos desde archivos JSON
def cargar_datos(archivo):
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# Guardar datos en archivos JSON
def guardar_datos(archivo, datos):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

# Módulo de Gestión de Productos
def agregar_producto(codigo, nombre, categoria, proveedor, stock, precio_compra, precio_venta):
    productos = cargar_datos(PRODUCTOS_FILE)
    if codigo in productos:
        print("Error: Código de producto ya existe.")
        return
    productos[codigo] = {
        "nombre": nombre,
        "categoria": categoria,
        "proveedor": proveedor,
        "stock": stock,
        "precio_compra": precio_compra,
        "precio_venta": precio_venta
    }
    guardar_datos(PRODUCTOS_FILE, productos)
    print("Producto agregado correctamente.")

def editar_producto(codigo, nombre=None, categoria=None, proveedor=None, stock=None, precio_compra=None, precio_venta=None):
    productos = cargar_datos(PRODUCTOS_FILE)
    if codigo not in productos:
        print("Error: Producto no encontrado.")
        return
    if nombre:
        productos[codigo]["nombre"] = nombre
    if categoria:
        productos[codigo]["categoria"] = categoria
    if proveedor:
        productos[codigo]["proveedor"] = proveedor
    if stock is not None:
        productos[codigo]["stock"] = stock
    if precio_compra is not None:
        productos[codigo]["precio_compra"] = precio_compra
    if precio_venta is not None:
        productos[codigo]["precio_venta"] = precio_venta
    guardar_datos(PRODUCTOS_FILE, productos)
    print("Producto actualizado correctamente.")

def eliminar_producto(codigo):
    productos = cargar_datos(PRODUCTOS_FILE)
    if codigo not in productos:
        print("Error: Producto no encontrado.")
        return
    del productos[codigo]
    guardar_datos(PRODUCTOS_FILE, productos)
    print("Producto eliminado correctamente.")

# Módulo de Gestión de Pedidos
def crear_pedido(codigo_pedido, codigo_cliente, detalles):
    pedidos = cargar_datos(PEDIDOS_FILE)
    productos = cargar_datos(PRODUCTOS_FILE)
    if codigo_pedido in pedidos:
        print("Error: Código de pedido ya existe.")
        return
    total = 0
    for detalle in detalles:
        codigo_producto, cantidad = detalle["codigo_producto"], detalle["cantidad"]
        if codigo_producto not in productos or productos[codigo_producto]["stock"] < cantidad:
            print(f"Error: Stock insuficiente para {codigo_producto}.")
            return
        productos[codigo_producto]["stock"] -= cantidad
        total += cantidad * productos[codigo_producto]["precio_venta"]
    pedidos[codigo_pedido] = {
        "codigo_cliente": codigo_cliente,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "detalles": detalles,
        "total": total
    }
    guardar_datos(PEDIDOS_FILE, pedidos)
    guardar_datos(PRODUCTOS_FILE, productos)
    print("Pedido registrado correctamente.")

def eliminar_pedido(codigo_pedido):
    pedidos = cargar_datos(PEDIDOS_FILE)
    if codigo_pedido not in pedidos:
        print("Error: Pedido no encontrado.")
        return
    del pedidos[codigo_pedido]
    guardar_datos(PEDIDOS_FILE, pedidos)
    print("Pedido eliminado correctamente.")

# Función principal con menú interactivo
def menu():
    while True:
        print("1. Agregar Producto")
        print("2. Editar Producto")
        print("3. Eliminar Producto")
        print("4. Crear Pedido")
        print("5. Eliminar Pedido")
        print("6. Consultar productos")
        print("7. Consultar pedidos")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            codigo = input("Código del producto: ")
            nombre = input("Nombre: ")
            categoria = input("Categoría: ")
            proveedor = input("Proveedor: ")
            stock = int(input("Cantidad en stock: "))
            precio_compra = float(input("Precio de compra: "))
            precio_venta = float(input("Precio de venta: "))
            agregar_producto(codigo, nombre, categoria, proveedor, stock, precio_compra, precio_venta)
        elif opcion == "2":
            codigo = input("Código del producto a editar: ")
            nombre = input("Nuevo nombre: ") or None
            categoria = input("Nueva categoría: ") or None
            proveedor = input("Nuevo proveedor: ") or None
            stock = input("Nueva cantidad en stock: ")
            stock = int(stock) if stock else None
            precio_compra = input("Nuevo precio de compra: ")
            precio_compra = float(precio_compra) if precio_compra else None
            precio_venta = input("Nuevo precio de venta: ")
            precio_venta = float(precio_venta) if precio_venta else None
            editar_producto(codigo, nombre, categoria, proveedor, stock, precio_compra, precio_venta)
        elif opcion == "3":
            codigo = input("Código del producto a eliminar: ")
            eliminar_producto(codigo)
        elif opcion == "4":
            codigo_pedido = input("Código del pedido: ")
            codigo_cliente = input("Código del cliente: ")
            detalles = []
            while True:
                codigo_producto = input("Código del producto (0 'fin' para terminar): ")
                if codigo_producto == "0":
                    break
                cantidad = int(input("Cantidad: "))
                detalles.append({"codigo_producto": codigo_producto, "cantidad": cantidad})
            crear_pedido(codigo_pedido, codigo_cliente, detalles)
        elif opcion == "5":
            codigo_pedido = input("Código del pedido a eliminar: ")
            eliminar_pedido(codigo_pedido)
        elif opcion == "6":
            print(productos)
        elif opcion == "7":
            print(pedidos)
        elif opcion == "8":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

# Ejecutar menú
if __name__ == "__main__":
    menu()
