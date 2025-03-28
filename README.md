# project python

# Panaderia

Este proyecto consiste en el desarrollo de un sistema de gestión para una panadería que permita el manejo eficiente de productos, pedidos y detalles asociados. El objetivo es optimizar el control de inventario, asegurar la correcta gestión de los precios y mejorar la experiencia del cliente.

## Tabla de Contenidos

- [Características](características)
- [Estructura de Datos](estructura-de-datos)
  - [Productos](productos)
  - [Pedidos](pedidos)
- [Tecnologías](#tecnologías)
- [Módulos (Archivos) del Proyecto](módulos-archivos-del-proyecto)
- [Instalación](instalación)
- [Contribuciones](contribuciones)

## Características

- **Gestión de Productos**: Registro de productos de panadería (panes, pasteles, postres), incluyendo detalles como nombre, categoría, descripción, proveedor, stock, y precios.
- **Gestión de Pedidos**: Permite la creación y gestión de pedidos, con opción de editar y eliminar.
- **Inventario Automatizado**: El inventario se actualiza automáticamente al registrar pedidos, con alertas cuando los productos están por agotarse.
- **Consultas y Búsquedas**: Búsqueda por nombre, categoría o código, y filtrado de pedidos.
- **Persistencia de Datos**: Los datos se almacenan en archivos JSON para garantizar la persistencia entre sesiones.

## Estructura de Datos

### Productos
Cada producto tiene propiedades como código, nombre, categoría, descripción, proveedor, cantidad en stock, y precios de venta y compra.

### Pedidos
Cada pedido incluye detalles sobre productos, cantidad, precio por unidad.

## Tecnologías

- Python
- Archivos JSON para persistencia de datos
- GitHub para gestión de versiones

## Módulos (Archivos) del Proyecto

El proyecto tiene la siguiente estructura de archivos:


- **`panaderia.py`**: Es el script principal donde se inicia la ejecución del sistema.
Contiene las funciones y clases relacionadas con la gestión de productos (registro, actualización, eliminación).
Gestiona los pedidos, incluyendo la creación, actualización y seguimiento de los mismos.
Se encarga de las operaciones relacionadas con el inventario de productos.
Contiene funciones auxiliares que son utilizadas en varias partes del sistema.
Carpeta que contiene los archivos JSON donde se almacenan los datos de productos y pedidos. Es posible que contenga otros archivos según sea necesario.
  - **`productos.json`**: Almacena la información sobre los productos disponibles en la panadería.
  - **`pedidos.json`**: Guarda los detalles de los pedidos realizados.
- **`requirements.txt`**: Archivo que lista las dependencias de Python necesarias para el funcionamiento del proyecto.

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/cristian20252025/proyecto-panaderia
   ```
2. Ejecutar el script principal:
   ```bash
   python panaderia.py
   ```