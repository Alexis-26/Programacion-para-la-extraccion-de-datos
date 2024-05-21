#Librerias
import pandas as pd

"""Crear un programa que contenga las siguientes funciones:"""

"""Crear una función que retorne un DataFrame indexado de las columnas departamento, nombre, con la siguiente Información 
(Nota: Ambas columnas no deben eliminarse, deben ser índices y columnas): (5%)"""

def generar_dataframe():
    d = {
        "Departamento":["Ventas", "Ventas", "HR", "HR", "IT", "IT"],
        "Id":["1001", "1002", "2001", "2002", "3001", "3002"],
        "Nombre":["Juan", "Ana", "Luis", "Maria", "Pedro", "Sofía"],
        "Edad":[30, 24, 29, 25, 32, 28],
        "Salario":[40000, 42000, 38000, 39000,50000,52000]
    }
    data = pd.DataFrame(d)
    data.set_index(["Departamento", "Nombre"], inplace=True, drop=False)
    return data

"""Crear una función que reciba como parámetro el departamento, y retorne un dataframe con la media, desviación estándar, 
valor mínimo, valor máximo de la edad y el salario. (5%)"""
def statistics(departamento:str):
    data = generar_dataframe()
    data = data.loc[departamento]
    media_edad = data.Edad.mean()
    std_edad = data.Edad.std()
    minimo_edad = data.Edad.min()
    maximo_edad = data.Edad.max()
    media_salario = data.Salario.mean()
    std_salario = data.Salario.std()
    minimo_salario = data.Salario.min()
    maximo_salario = data.Salario.max()
    d = {
        "media":[media_edad, media_salario],
        "std":[std_edad, std_salario],
        "minimo":[minimo_edad, minimo_salario],
        "maximo":[maximo_edad, maximo_salario]
    }
    df = pd.DataFrame(d)
    df.index = ["Edad", "Salario"]
    return df

"""Crea una función que inserte una columna de fecha de ingreso que cumpla con el formato YYYY-MM-DD. 
Dicha función debe recibir como parámetro el dataframe y la lista de valores de ingreso. Debe convertir dicha columna a tipo datetime y retornar el resultado. (5%)"""
def insert_date(data:pd.DataFrame, fechas:list):
    data["Fecha de ingreso"] = fechas
    data["Fecha de ingreso"] = pd.to_datetime(data["Fecha de ingreso"])
    return data

"""Convertir la columna fecha a un índice y retornar los datos comprendidos entre una fecha mínima y máxima. Dichas fechas deben ser parámetros de la función. (5%)"""
def range_date(data:pd.DataFrame, date_min:str, date_max:str):
    data.set_index("Fecha de ingreso", inplace=True, drop=False)
    date_min = pd.to_datetime(date_min)
    date_max = pd.to_datetime(date_max)
    data = data.loc[data["Fecha de ingreso"] >= date_min]
    data = data.loc[data["Fecha de ingreso"] <= date_max]
    return data

"""Suponer que existen  3 diferentes archivos csv con la información de nuestros empleados contratados por año, en el mismo formato presentado en el inciso a. 
Crear una función que una los 3 archivos en un solo dataframe, cada archivo es un parámetro de la función, 
guardar el resultado en un nuevo archivo csv y retornar el DataFrame resultante. 
NOTA: Para probar debe crear los archivos csv con valores a su elección. (10%)"""
def union_info(path1:str, path2:str, path3:str):
    df1 = pd.read_csv(path1)
    df2 = pd.read_csv(path2)
    df3 = pd.read_csv(path3)
    data = pd.concat([df1, df2, df3], axis="index", ignore_index=True)
    return data

"""Se cuenta con un archivo csv con la información extra de los empleados, esta información es dirección, teléfono, estado civil, correo, años de experiencia. 
Con los datos resultantes  del inciso e, se desea agregar la información de este nuevo archivo. 
Debe recibir como parámetro la ruta del archivo y retornar el DataFrame resultante. (10%) """
def info_extra(path1:str, path2:str):
    info = pd.read_csv(path1)
    info_extra = pd.read_csv(path2)
    data = pd.concat([info, info_extra], axis="column")
    return data