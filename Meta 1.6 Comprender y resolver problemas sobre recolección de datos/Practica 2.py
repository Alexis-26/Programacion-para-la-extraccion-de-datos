"""Este programa contiene una función que importa el archivo CSV de cotizaciones y 
realiza los cálculos de mínimo, máximo y media de cada columna del archivo importado. 
Realizado con la librería de pandas.

Alexis Cruz Miros Grupo 951 Fecha: 24/03/2024"""

import pandas as pd #Importando la librería pandas.

def operaciones_datos_CSV(path, separador=",", decimal=".", miles=None): #Función para importar un archivo CSV y realizar los cálculos.
    estructura = {"Datos":["Minimo", "Maximo", "Media"]} #Creando un diccionario base.
    datos = pd.read_csv(path, sep=separador, decimal=decimal, thousands=miles) #Guardando los datos convertidos en dataframe.
    encabezados = list(datos.columns) #Guardando el nombre de las columnas.

    for index in encabezados[1:6]: #Ciclo para los nombres guardados en "encabezados".
        columna = datos[index] #Guardando los registros de la columna que le pertenece al ecabezado obtenido por el "index".
        minimo = columna.min() #Guardando y cálculando el valor mínimo a partir de los registros de la columna.
        maximo = columna.max() #Guardando y cálculando el valor máximo a partir de los registros de la columna.
        media = columna.mean() #Guardando y cálculando la media a partir de los registros de la columna.
        estructura[index] = [minimo, maximo, media] #Guardando en el diccionario base el "encabezado" como llave y como valor una lista con los resultado obtenidos.

    df = pd.DataFrame(estructura) #Convirtiendo el diccionario base en un dataframe una vez que terminó el ciclo.
    return df

if __name__ == "__main__":
    df = operaciones_datos_CSV("SRC/Dataset/cotizacion.csv", ";", ",", ".") #Enviando el path del archivo y especificando las características del archivo.
    print(df)