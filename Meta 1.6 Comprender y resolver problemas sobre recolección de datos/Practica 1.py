"""Este programa genera y muestra una dataframe con 
información mostrada en una tabla. Realizado con la librería de pandas.
Alexis Cruz Miros Grupo 951 Fecha: 22/03/2024"""

import pandas as pd #Importando la librería pandas.

def generar_dataFrame(datos:dict): #Metodos para generar el DataFrame.
    estructura = datos #Guardando en una variable  los datos recibidos.
    df = pd.DataFrame(estructura) #Creando el DataFrame con la librería.
    return df #Retornando el DataFrame.


if __name__ == "__main__":
    datos = {"Mes" : ["Enero", "Febrero", "Marzo", "Abril"],
             "Ventas" : [30500, 35600, 28300, 33900],
             "Gastos" : [22000, 23400, 18100, 20700]} #Construcción del diccionario para crear un DataFrame
    df = generar_dataFrame(datos) #Enviando como argumento el diccionario.
    print(df) #Impimiendo en consola el DataFrame recibido.