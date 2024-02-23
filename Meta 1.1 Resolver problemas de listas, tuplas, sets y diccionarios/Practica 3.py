"""Alexis Cruz Miros 951 18/02/2024
Análisis de Población. 
Tienes datos sobre población de diferentes ciudades representados como tuplas (ciudad, población, área). 
Crea funciones para:
a. Calcular la densidad de población (población dividida por la cantidad total de población por área) 
para cada ciudad.
b. Identificar la ciudad con la mayor densidad de población
"""
def calcular_densidad(lista):
    d_aux = {}
    d_resultados = {}
    for c, p, z in lista:
        d_aux[z] = d_aux.get(z, 0) + p
    
    for index in d_aux:
        for c, p, z in lista:
            if z == index:
                resultado = p / d_aux[index]
                d_resultados[c] = round(resultado, 2)

            if p == d_aux[index]:
                d_resultados[c] = p

    return d_resultados

def mayor_densidad(lista):
    d_densidades = calcular_densidad(lista)
    lista_numeros = []

    for k, v in d_densidades.items():
        lista_numeros.append(v)

    mayor = max(lista_numeros)

    for index, value in d_densidades.items():
        if value == mayor:
            return index

#Lista de tuplas con ciudad, poblacion y área
ciudades = [
("Tijuana", 5, "NoroEste"), 
("Ciudad de Mexico", 8, "Centro"), 
("Ensenada", 3, "NoroEste"), 
("Puebla", 3, "Centro"), 
("Cancun", 4, "Sur")
]

densidades = calcular_densidad(ciudades)
print(densidades)

mayor = mayor_densidad(ciudades)
print(mayor)