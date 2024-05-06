"""Realizar una función que reciba como parámetro un DataFrame y  retorne el porcentaje de valores nulos de cada columna.

Alexis Cruz Miros Grupo 951 Fecha: 05/05/2024"""

import pandas as pd

def porcentajes_nulos(datos:pd.DataFrame):
    nulos = datos.isnull() # Validar que datos son nulos
    total_nulos = nulos.sum() # Total de nulos por cada columna
    total_datos = len(datos)# Total de renglones
    porcentaje = total_nulos / total_datos # Calculando el porcentaje de datos nulos por columna
    return porcentaje

if __name__ == "__main__":
    datos = pd.read_csv("SRC/Dataset/titanic.csv")
    print(porcentajes_nulos(datos))