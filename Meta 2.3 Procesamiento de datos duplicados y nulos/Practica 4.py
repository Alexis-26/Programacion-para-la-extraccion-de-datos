"""Realizar una función que reciba como parámetro un DataFrame, una lista con los nombres de las columnas a verificar y una cadena. 
La cadena solo puede ser mean, bfill o ffill, en caso contrario lanzar una excepción. 
Debe sustituir los valores nulos por el método especificado y retornar el DataFrame modificado.

Alexis Cruz Miros Grupo 951 Fecha: 05/05/2024"""

import pandas as pd

def modificacion_metodos(datos:pd.DataFrame, columnas:list, metodo:str):
    columnas_df = list(datos.columns) # Extrayendo las columnas del dataframe
    d = {} # Creando un diccionario vacio para ser usado mas adelante
    for i in columnas_df:
        if i in columnas: # Validad que los nombres coinicidan para aplicar el metodo
            try:
                if metodo == "mean": # Verificando el metodo
                    prom = datos[i].mean(numeric_only=True)
                    d[i] = [prom] # Utilizando el diccionario para almacenar la informarcion y despues convertir a dataframe con la columna y sus valores

                elif metodo == "bfill":
                    datos[i].bfill(inplace=True) # Utilizando el metodo bfill en el dataframe original
                    

                elif metodo == "ffill":
                    datos[i].ffill(inplace=True)# Utilizando el metodo ffill en el dataframe original

            except Exception as e:
                return e
    
    if metodo == "mean":
        datos_modificados = pd.DataFrame(d) # Convertiendo el diccionario anterior en un dataframe
        return datos_modificados
    
    elif metodo == "bfill" or metodo == "ffill":
        return datos # Retornando las modificaciones realizadas

if __name__ == "__main__":
    datos = pd.read_csv("SRC/Dataset/titanic.csv")
    columnas = ["Age", "Cabin"]
    metodo = "ffill"
    print(modificacion_metodos(datos, columnas, metodo))