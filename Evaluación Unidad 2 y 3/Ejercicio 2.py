#Librerias
import pandas as pd

"""Se tiene un archivo llamado bank-loans.csv, el cual contiene información sobre los préstamos de los clientes de un banco. 
Utilizando la librería Pandas se pide, las siguientes funciones una por cada inciso, debe probar su funcionamiento en un main:"""

"""Generar un dataframe con los datos del archivo. (3%)"""
def generar_dataframe():
    path = "SRC/Dataset/bank-loans.csv"
    data = pd.read_csv(path)
    return data

"""Mostrar por pantalla las filas del DataFrame múltiplos de 10. (2%)"""
def multiple_ten():
    data = generar_dataframe()
    condition = data["age"] % 10 == 0
    data = data[condition]
    return data

"""Realizar una función que reciba como parámetro una edad mínima y una edad máxima. 
Retorna un DataFrame con la información de los clientes entre dicho rango. (5%)"""
def range_age(age_min:int, age_max:int):
    data = generar_dataframe()
    data = data.loc[data["age"] >= age_min]
    data = data.loc[data["age"] <= age_max]
    return data

"""Agregar al DataFrame una columna nueva con la edad en meses.(2%)"""
def year_to_month():
    data = generar_dataframe()
    data["age_month"] = data["age"] * 12
    return data

"""Mostrar por pantalla las frecuencias de los oficios ordenados de mayor a menor. (5%)"""
def frecuency_job():
    data = generar_dataframe()
    frecuency = data["job"].value_counts(ascending=False)
    return frecuency

"""Mostrar por pantalla las edades medias según el nivel de estudios. (3%)"""
def years_mean():
    data = generar_dataframe()
    result = data.groupby("education").agg({
        "age":["mean"]
    })
    return result

"""Mostrar por pantalla el porcentaje de préstamos hipotecarios(housing) según el estado civil (marital). (5%)"""
def percentage_housing():
    data = generar_dataframe()
    data = data.loc[data["housing"] == "yes"]
    result = data.groupby("marital").agg({
        "housing":["count"]
    })
    result.columns = ["housing percentage"]
    total = len(data)
    result = (result["housing percentage"] / total) * 100
    return result

"""Calcular el porcentaje de valores unknown de las columnas. Retornar una Serie con los resultados ordenados de mayor a menor. (5%)"""
def percentage_unknown():
    data = generar_dataframe()
    result = (data == "unknown").sum()
    total = result.sum()
    percentage = (result / total) * 100
    return percentage