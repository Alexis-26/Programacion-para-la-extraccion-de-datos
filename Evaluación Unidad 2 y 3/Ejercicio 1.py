#librerias
import pandas as pd
from sqlalchemy import create_engine

"""El archivo coches.csv, contiene la información sobre los modelos de coches vendidos en USA en un determinado año. Se pide lo siguiente:"""

"""Crear una función que permita guardar el contenido del archivo en una sola tabla de una Base de Datos. 
Debe asumir que existe una Base de Datos llamada Ventas Coches, la cual contiene una tabla llamada Ventas, NOTA: Puede utilizar MYSQL o MONGODB. (10%)"""

def save_database(path:str, separador=",", decimal=".", miles=None):
    string_conection = "mysql+mysqlconnector://root:26097278@127.0.0.1/Ventas_Coches"
    engine = create_engine(string_conection)
    conection = engine.connect()
    data = pd.read_csv(path, sep=separador, decimal=decimal, thousands=miles)
    data.to_sql("ventas", conection, if_exists="append", index=False)
    conection.close()

"""Crear una función que se conecte a la base de datos y retorna un DataFrame con el número de autos vendidos por Marca, 
y el total de ganancia (suma de precios), debe recibir como parámetro la marca que se desea calcular, 
además de incluir un valor default por si se requiere que retorne la información de todas las marcas. 
NOTA: Los cálculos debe hacerlos con PANDAS no con la consulta SQL, la consulta solo puede usar select, from, o sus equivalentes en MONGODB. (10%)"""

def consult_autosVendidos(marca:str = None):
    string_conection = "mysql+mysqlconnector://root:26097278@127.0.0.1/Ventas_Coches"
    engine = create_engine(string_conection)
    conection = engine.connect()
    if marca == None:
        consult = "SELECT Marca, Precio FROM Ventas"
        data = pd.read_sql(consult, conection)
        conection.close()
    else:
        consult = "SELECT Marca, Precio FROM Ventas WHERE Marca = %(marca)s"
        data = pd.read_sql(consult, conection, params={"marca":marca})
        conection.close()
    result = data.groupby("Marca").agg({
        "Marca":["count"],
        "Precio":["sum"]
    })
    result.columns = ["Autos Vendidos", "Total de Ganancia"]
    return result

"""Crear una función que retorne un DataFrame con los carros con mayor precio. La función debe de tener como parámetro la cantidad de carros a retornar. 
Si el parámetro es un 3 debe retornar los tres con mayor precio. 
Si es un 5 debe retornar los cinco con mayor precio. Validar que el número no sea mayor a la cantidad de datos o un valor menor a cero. 
NOTA: Los cálculos debe hacerlos con PANDAS, su consulta de sql solo puede usar select, from, sort  o sus equivalentes en MONGODB. (10%)"""

def consult_carrosMayorPrecio(cant:int):
    string_conection = "mysql+mysqlconnector://root:26097278@127.0.0.1/Ventas_Coches"
    engine = create_engine(string_conection)
    conection = engine.connect()
    consult = "SELECT * FROM Ventas;"
    data = pd.read_sql(consult, conection)
    cant_data = len(data)
    if cant > 0 and cant < cant_data:
        data.sort_values(by="Precio", ascending=False, ignore_index=True, inplace=True)
        return data.head(cant)
    else:
        return f"La cantidad ingresada es erronea o sobrepasa el limite de datos de {cant_data}"