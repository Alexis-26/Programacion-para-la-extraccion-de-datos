"""Alexis Cruz Miros 951 13/02/2024
Realizar una función con una lista de números enteros, 
retorna True si al menos un valor aparece dos veces, y Falso si todos los elementos son distintos.
"""
def dups(nums):
    return list(set(nums)) != nums

lista_1 = [1,2,3,4,5]
print(dups(lista_1))

lista_2 = [1,2,3,4,5,1]
print(dups(lista_2))