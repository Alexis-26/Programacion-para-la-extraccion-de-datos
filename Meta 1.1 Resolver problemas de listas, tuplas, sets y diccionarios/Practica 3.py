"""Alexis Cruz Miros 951 13/02/2024

"""
def calcular_densidad(lista):
    d_aux = {}
    d_resultados = {}
    #Ciclo for para hacer las funciones, ademas tomar en cuenta que se debe de guardar en un diccionario la ciudad y el resultado de la densidad
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

    for index in d_densidades.items():
        densidad = lista[index]
        if mayor == densidad:
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