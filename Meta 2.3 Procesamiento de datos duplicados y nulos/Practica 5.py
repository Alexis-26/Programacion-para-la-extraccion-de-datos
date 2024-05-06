"""Realizar una función que reciba como parámetro un DataFrame y elimine los renglones repetidos en el DataFrame Original. 
Debe retornar la cantidad de renglones eliminados.

Alexis Cruz Miros Grupo 951 Fecha: 05/05/2024"""

import pandas as pd

def renglones_repetidos(datos:pd.DataFrame):
    duplicados = datos.duplicated() # Detectando duplicados por cada fila
    total_duplicados = duplicados.sum() # Sumando los duplicados
    datos.drop_duplicates(inplace=True) # Eliminando los duplicados
    return total_duplicados

if __name__ == "__main__":
    d = {
        "nombre":["Maria", "Maria", "Maria", "Isabella "],
        "genero":["F", "F", "F", "SI"],
        "escolaridad":["Universidad", "Universidad", "Universidad", "Prepa"]
    }
    datos = pd.DataFrame(d)
    print(renglones_repetidos(datos))