

def update(datos_antes, datos_actual):
    conjunto_antes = datos_antes.difference(datos_actual)
    conjunto_actual = datos_actual.difference(datos_antes)
    d_update = {}
    points = []
    for i, item in enumerate(conjunto_antes):
        d_update[item] = 0
        points.append(i)

                
    return d_update

conjunto_antes = {1, 2, 3, 4, 5}
conjunto_actual = {8, 2, 3, 10, 5}
print(update(conjunto_antes, conjunto_actual))