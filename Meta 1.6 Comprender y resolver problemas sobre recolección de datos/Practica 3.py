"""Este programa importa un archivo CSV convirtido en un dataframe, utilizando una función
y por consola se muestra lo siguiente:
- Mostrar el número de datos que contiene y los nombres de sus columnas.
- Mostrar las 10 primeras filas.
- Mostrar las 10 últimas filas.
- Mostrar 10 filas de manera aleatoria.
Realizado con la librería de pandas.

Alexis Cruz Miros Grupo 951 Fecha: 25/03/2024"""

import pandas as pd #Importando la librería pandas.

def generar_dataframe_CSV(path, separador=",", decimal=".", miles=None): #Función para importar un archivo CSV.
    df = pd.read_csv(path, sep=separador, decimal=decimal, thousands=miles)
    return df

if __name__ == "__main__":
    df = generar_dataframe_CSV("SRC/Dataset/titanic.csv") #Enviando datos a la función.
    cant_elements = df.size #Guardando la cantidad de elementos en el dataframe.
    nom_columns = list(df.columns) #Guardando los nombres de las columnas.
    filas_inicio = df.head(10) #Guardando los primeros 10 registros del dataframe.
    filas_final = df.tail(10) #Guardando los últimos 10 registros del dataframe.
    filas_aleatorias = df.sample(10) #Guardando de manera aleatoria 10 registros del dataframe.

    #Área de impresiones de los requisitos de la práctica.
    print(f"Número de datos: {cant_elements}\n"
          f"Nombre de Columnas: {nom_columns}")
    
    print(f"Primeras 10 filas: \n {filas_inicio}")

    print(f"Últimas 10 filas: \n {filas_final}")

    print(f"10 filas aleatorias: \n {filas_aleatorias}")