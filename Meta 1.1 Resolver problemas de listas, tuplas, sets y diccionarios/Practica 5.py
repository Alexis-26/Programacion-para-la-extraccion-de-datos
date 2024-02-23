"""Alexis Cruz Miros 951 20/02/2024
Detección de Cambios en Datos. Imagina tener dos conjuntos de datos que representan 
el estado actual y el estado anterior de un sistema. 
Crea una función que identifique los elementos que han cambiado entre los dos conjuntos. 
Retorna un diccionario usando como la llave el estado anterior y como valor el estado actual. 
Para este ejercicio pueden asumir que los datos son numéricos y/o cadenas.
"""
def update(datos_antes, datos_actual):
    conjunto_antes = datos_antes.difference(datos_actual)
    conjunto_actual = datos_actual.difference(datos_antes)
    d_update = {}
    for value_1, value_2 in zip(conjunto_antes, conjunto_actual):
        d_update[value_1] = value_2 
    return d_update

conjunto_antes = {1, 2, 3, 4, 5}
conjunto_actual = {8, 2, 3, 10, 5}
print(update(conjunto_antes, conjunto_actual))