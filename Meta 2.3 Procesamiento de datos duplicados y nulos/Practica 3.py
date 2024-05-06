"""Realizar una función que reciba como parámetro un DataFrame y un máximo porcentaje. 
Este debe eliminar todas las columnas que superen o igualen el máximo porcentaje de valores nulos establecidos en el DataFrame Original. 
Retornar la lista nombres de columnas eliminadas.  
Validar que el porcentaje máximo esté entre 0 y 1.

Alexis Cruz Miros Grupo 951 Fecha: 05/05/2024"""

import pandas as pd

def columnas_eliminadas(datos:pd.DataFrame, porcentaje_max:float):
    if porcentaje_max > 0 and porcentaje_max < 1:
        nulos = datos.isnull() # Validar que datos son nulos
        total_nulos = nulos.sum() # Total de nulos por cada columna
        total_datos = len(datos)# Total de renglones
        porcentaje_nulos = total_nulos / total_datos # Calculando el porcentaje de datos nulos por columna
        columnas = [] # Creando una lista para guardar el nombre de las columnas a eliminar
        for k, v in porcentaje_nulos.items(): # Recorriendo la serie
            if v >= porcentaje_max:
                columnas.append(k) # Guardando el nombre de la columna
        datos.drop(columnas, axis="columns", inplace=True) # Eliminando las columnas correspondientes con la lista antes creada
        return columnas # Retornando las columnas eliminadas
    
    else:
        return "El porcentaje debe de estar en el rango de 0 a 1"

if __name__ == "__main__":
    datos = pd.read_csv("SRC/Dataset/titanic.csv")
    porcentaje_max = 0.18
    print(columnas_eliminadas(datos, porcentaje_max))