"""Desarrollar una clase llamada MySQLConnect que tenga como atributos: host, user, password, database. 
Debe tener los siguientes métodos:
1. conectar() : Debe conectarse a la base de datos usando los atributos, debe retornar el objeto de conexión.
2. desconectar(): Debe desconectar la base de datos. No debe retornar nada. Investigar método close().

Alexis Cruz Miros Grupo 951 Fecha: 20/04/2024"""

from mysql.connector import connect, Error

class MySQLConnect: #Creando la clase y sus atributos
    def __init__(self, host:str, user:str, password:str, database:str) -> None: #Recibiendo atributos
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    
    def conectar(self) -> object:
        host = self.host
        user = self.user
        password = self.password
        database = self.database
        try:
            self.conexiondb = connect(host=host, user=user, password=password, database=database) #Realizando la conexion
            return self.conexiondb #Retornando el objeto de la conexion

        except Error as e: #Capturando errores
            return e #Retornando excepcion
        
    def desconectar(self) -> None:
        try:
            self.conexiondb.close() #Cerrando la conexion que se realizo con anterioridad

        except Error as e:
            return e

if __name__ == "__main__":
    host = "127.0.0.1"
    user = "root"
    password = ""
    database = "olimpiadas"
    conexiondb = MySQLConnect(host, user, password, database)
    print(conexiondb.conectar())
    conexiondb.desconectar()

