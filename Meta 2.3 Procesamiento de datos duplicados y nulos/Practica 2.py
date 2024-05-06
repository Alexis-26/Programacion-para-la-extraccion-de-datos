"""Realizar una función que reciba como parámetro un DataFrame y retorne el número de renglones duplicados.

Alexis Cruz Miros Grupo 951 Fecha: 05/05/2024"""

import pandas as pd

def cant_duplicados(datos:pd.DataFrame):
    duplicados = datos.duplicated() # Detectando duplicados por cada fila
    total_duplicados = duplicados.sum() # Sumando todos los duplicados
    return total_duplicados

if __name__ == "__main__":
    d = {
        "nombre":["Maria", "Maria", "Maria", "Isabella "],
        "genero":["F", "F", "F", "SI"],
        "escolaridad":["Universidad", "Universidad", "Universidad", "Prepa"]
    }
    datos = pd.DataFrame(d)
    print(cant_duplicados(datos))