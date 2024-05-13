"""Realizar una función que normalice los datos usando min-max que reciba como parámetro un DataFrame 
y otro parámetro que sea una lista de columnas a normalizar. 
Retornar el DataFrame con los datos normalizados.

Alexis Cruz Miros Grupo 951 Fecha: 12/05/2024"""

import pandas as pd

def normalizacion_min_max(data:pd.DataFrame, columnas:list):
    for i in data: # Ciclo en el dataframe para ubicar cada columna
        for j in columnas: # Ciclo en la lista de columnas recibida por medio del parametro
            if j == i: # Comparando la lista de columnas recibida con las del dataframe
                data_max = data[i].max() # Obteniendo el mayor de la columna indicada
                data_min = data[i].min() # Obteniendo el menor de la columna indicada
                data[i] = (data[i] - data_min) / (data_max - data_min) # Calculando la normalizacion de los datos y actualizando la columna
    return data

if __name__ == "__main__":
    d = {
        "nombre":["Maria", "Jose", "Mateo", "Roberto"],
        "salario":[6000, 30000, 27000, 50000],
        "edad":[18, 27, 40, 33],
        "antiguedad":[6, 4, 2, 5]
    }
    data = pd.DataFrame(d)
    columnas = ["salario", "edad"]
    print(normalizacion_min_max(data, columnas))