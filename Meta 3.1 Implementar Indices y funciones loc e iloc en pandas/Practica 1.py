"""
Alexis Cruz Miros Grupo 951 Fecha: 31/05/2024
"""

import pandas as pd

"""
Crea un DataFrame llamado ventas que contenga la información de las ventas mensuales de tres productos (A, B y C) 
durante los primeros tres meses del año. Cada fila debe representar un mes y cada columna debe representar un producto. 
Llena el DataFrame con datos aleatorios entre 100 y 1000.
"""
def generar_dataframe(): #Generando el dataframe a utilizar.
    d = {"Mes":["Enero", "Febrero", "Marzo"],
         "A":[100, 500, 700],
         "B":[400, 900, 200],
         "C":[500, 300, 100]}
    df = pd.DataFrame(d)
    return df

"""
Realiza una función para seleccionar datos del DataFrame usando loc e índices, proponga que parámetros debería llevar y pruebe los siguientes escenarios:
Las ventas del producto A en el mes de enero.
Las ventas de todos los productos en el mes de febrero.
Las ventas de todos los productos en el primer y tercer mes.
"""
def consulta_ventas(df:pd.DataFrame, mes:list, producto:list=None):
    df.set_index("Mes", inplace=True, drop= False) #Estableciendo la columna Mes como index.
    data = df.loc[mes] #Realizando la busqueda.
    if producto is not None: #Por si hay especificación del producto, realiza la busqueda por mes y producto.
        data = data[producto]
    return data

"""
Realiza una función para seleccionar datos del DataFrame usando iloc, proponga que parámetros debería llevar y pruebe los siguientes escenarios:
Las ventas del primer mes para todos los productos.
Las ventas del segundo producto en todos los meses.
Las ventas del segundo y tercer mes para el primer producto.
"""
def seleccion_ventas(df:pd.DataFrame, mes:list=None, producto:list=None):
    if mes is not None and producto is None: #Validación de los parametros para realizar la busqueda especificada.
        res = df.iloc[mes, :]
    elif producto is not None and mes is None:
        res = df.iloc[:, producto]
    elif producto is not None and mes is not None:
        res = df.iloc[mes, producto]
    return res 

"""
Realiza una función que permita realizar cambios de un producto determinado en un mes específico, pruebe el siguiente escenario:
Cambia el valor de las ventas del producto B en el mes de marzo a 1200.
"""
def modificacion(df:pd.DataFrame, mes:str, producto:str, cantidad:int):
    df.set_index("Mes", inplace=True, drop= True) #Estableciendo la columna Mes como index y eliminando la columna temporalmente.
    df.loc[mes, producto] = cantidad #Realizando la busqueda y agregando la nueva cantidad.
    df.reset_index(names="Mes", inplace=True) #Restableciendo el dataframe por medio del nombre de la columna.
    return df

if __name__ == "__main__":
    df = generar_dataframe()

    """Las ventas del producto A en el mes de enero."""
    df1 = consulta_ventas(df, ["Enero"], ["A"])
    print(df1)

    """Las ventas de todos los productos en el mes de febrero."""
    df2 = consulta_ventas(df, ["Febrero"])
    print(df2)

    """Las ventas de todos los productos en el primer y tercer mes."""
    df3 = consulta_ventas(df, ["Enero", "Marzo"])
    print(df3)

    """Las ventas del primer mes para todos los productos."""
    df4 = seleccion_ventas(df, mes=[0])
    print(df4)

    """Las ventas del segundo producto en todos los meses."""
    df5 = seleccion_ventas(df, producto=[2])
    print(df5)

    """Las ventas del segundo y tercer mes para el primer producto."""
    df6 = seleccion_ventas(df, mes=[1, 2], producto=[1])
    print(df6)

    """Cambia el valor de las ventas del producto B en el mes de marzo a 1200."""
    df7 = modificacion(df, "Marzo", "B", 1200)
    print(df7)