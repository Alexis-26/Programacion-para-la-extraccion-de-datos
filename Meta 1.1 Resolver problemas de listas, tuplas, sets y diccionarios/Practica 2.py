"""Alexis Cruz Miros 951 13/02/2024
Suma de dos números. Dado una lista de números enteros y un valor entero (target),
retorna el índice de los dos números que sumados sean igual al target. 
Debe asumir que existe siempre una única solución, y que un mismo elemento no se puede usar dos veces. 
Debes retornar una tupla con los índices.
"""
def dosnum(nums, target):
    dato = {}
    for index, item in enumerate(nums):
        resultado = target - item

        if item in dato:
            return (dato[item], index)
        dato[resultado] = index
        
lista_3 = [2, 7, 11, 15]
target = 9
print(dosnum(lista_3, target))