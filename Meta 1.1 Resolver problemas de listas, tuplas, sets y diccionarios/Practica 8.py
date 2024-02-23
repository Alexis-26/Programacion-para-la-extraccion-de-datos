"""Alexis Cruz Miros 951 22/02/2024
Inventario de Productos. Gestiona un inventario de productos en una tienda utilizando diccionarios. 
Las claves pueden ser los códigos de producto y los valores pueden ser diccionarios con 
información como el nombre, precio y cantidad en stock. 
Debe tener funciones para agregar, editar, eliminar producto, además de funciones para realizar 
venta e imprimir inventario.
"""
#inventario = {1:["playera", 5, 50],
              #2:["pantalon", 10, 50],
              #3:["chamarra", 20, 50],
              #4:["sudadera", 20, 50]}

inventario = {}

def agregar(codigo, nombre, precio, cantidadStock):
    infoProducto = []
    infoProducto.append(nombre)
    infoProducto.append(precio)
    infoProducto.append(cantidadStock)
    inventario[codigo] = infoProducto
    print(infoProducto)

def editar(codigo, nombre, precio, cantidadStock):
    infoProducto = []
    infoProducto.append(nombre)
    infoProducto.append(precio)
    infoProducto.append(cantidadStock)
    for key in inventario:
        if key == codigo:
            inventario[key] = infoProducto

def eliminar(codigo):
    inventario.pop(codigo)

def venta(codigo, cantidad):
    for key, value in inventario.items():
        if key == codigo:
            infoProducto = value
            if infoProducto[2] > 0 and cantidad <= infoProducto[2]:
                infoProducto[2] = infoProducto[2] - cantidad
                inventario[key] = infoProducto
            else:
                return print("Stock insuficiente")

def imprimir_inventario():
    return print(inventario)

agregar(1, 'playera', 5, 50)
agregar(2, 'pantalon', 10, 50)
agregar(3, 'chamarra', 20, 50)
agregar(4, 'sudadera', 20, 50)
imprimir_inventario()

editar(1, 'calcetas', 5, 20)
imprimir_inventario()

eliminar(3)
imprimir_inventario()

venta(2, 30)
imprimir_inventario()