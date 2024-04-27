"""Desarrollar una clase llamada ResultadosMySQL que herede de  MySQLConnect. Debe agregar los atributos correspondientes de la clase padre. 
Debe agregar los siguientes métodos:
1. insertar(idOlimpiada, idPais, idGenero, oro, plata, bronce): Método para insertar datos en la Tabla Resultados, 
debe recibir como parámetro las columnas de la tabla y debe retornar True si se inserta el dato o False en caso contrario.

2. editar(oro, plata, bronce): Método para editar oro, plata, bronce en la Tabla Resultados. Validar que sean valores enteros positivos.

3. eliminar(idOlimpiada, idPais, idGenero): Método para eliminar un elemento de la Tabla Resultados. 
Debe tener como parámetro la llave primaria compuesta, retorna True si logró eliminarse y False en caso contrario.

4. consultar(filter): Método que recibe un filtro(cadena) y retorna una lista de tuplas con los resultados del filtro de la Tabla Resultados. 
Ejemplo: “idPais = 1” , “idPais = 1 and idOlimpiada=2”

Alexis Cruz Miros Grupo 951 Fecha: 26/04/2024"""

from mysql.connector import connect, Error

class MySQLConnect: #Creando la clase padre con sus atributos
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
    
class ResultadosMySQL(MySQLConnect): #Creando una clase hija
    def __init__(self, host: str, user: str, password: str, database: str) -> None:
        super().__init__(host, user, password, database) #Agregando los atributos de la clase padre
    
    def insertar(self, idOlimpiada:int, idPais:int, idGenero:int, oro:int, plata:int, bronce:int):
        conexiondb = self.conexiondb
        cursor = conexiondb.cursor()
        validacion = "select * from Resultados where idOlimpiada = %s;"
        cursor.execute(validacion, (idOlimpiada, )) #idOlipiada lo estoy mandando como remplazo de %s (Para que se remplace se ocupa que sea una tupla)
        resultados = cursor.fetchall()

        if not resultados:
            insert = "INSERT INTO Resultados(idOlimpiada, idPais, idGenero, oro, plata, bronce) values(%s, %s, %s, %s, %s, %s);"
            datos_insertar = (idOlimpiada, idPais, idGenero, oro, plata, bronce)
            cursor.execute(insert, datos_insertar)
            conexiondb.commit() #Actualiza los cambios realizados (sirve para hacer una confirmacion)
            cursor.close()
            return True
        else:
            return False
        
    def editar(self, oro:int, plata:int, bronce:int):
        conexiondb = self.conexiondb
        cursor = conexiondb.cursor()
        validacion = "SELECT * FROM Resultados WHERE oro like %s AND plata like %s AND bronce like %s;" #Realizando una consulta para validar que existe el dato
        parametro_oro = f"%{oro}%" #Cambiando el formato para utilizarlo en un like de SQL
        parametro_plata = f"%{plata}%"
        parametro_bronce = f"%{bronce}%"
        cursor.execute(validacion, (parametro_oro, parametro_plata, parametro_bronce)) #Enviando la validacion y los valores que sustituyen %s para evitar inyeccion
        resultado = cursor.fetchall() #Recibiendo los resultados obtenidos de la consulta
        if resultado:
            dato_oro = int(input("Nuevo valor para oro: ")) #Recibiendo el nuevo valor para el dato a editar
            dato_plata = int(input("Nuevo valor para plata: ")) #Recibiendo el nuevo valor para el dato a editar
            dato_bronce = int(input("Nuevo valor para bronce: ")) #Recibiendo el nuevo valor para el dato a editar
            if dato_oro >= 0 and dato_plata >= 0 and dato_bronce >= 0:
                update = "UPDATE Resultados SET oro = %s, plata = %s, bronce = %s WHERE oro like %s AND plata like %s AND bronce like %s;" #Realizando un update
                cursor.execute(update, (dato_oro, dato_plata, dato_bronce, parametro_oro, parametro_plata, parametro_bronce)) #Enviando el update y los valores que sustituyen %s
                conexiondb.commit() #Guardando los cambios
                cursor.close()
                return True
            else:
                return "Los valores deben ser positivos"
        else:
            return False
        
    def eliminar(self, idOlimpiada:int, idPais:int, idGenero:int):
        conexiondb = self.conexiondb
        cursor = conexiondb.cursor()
        validacion = "SELECT * FROM Resultados WHERE idOlimpiada = %s AND idPais = %s AND idGenero = %s;" #Validando que existe el dato
        cursor.execute(validacion, (idOlimpiada, idPais, idGenero)) #Envando la consulta y sustituyendo %s
        resultado = cursor.fetchall() #Recibiendo los resultados de la consultando
        if resultado: #Validando si existen los datos
            delete = "DELETE FROM Resultados WHERE idOlimpiada = %s AND idPais = %s AND idGenero = %s;" #Realizando la eliminacion
            cursor.execute(delete, (idOlimpiada, idPais, idGenero)) #Ejecutando y enviando el delete y sustituyendo %s
            conexiondb.commit() #Guardando los cambios
            cursor.close()
            return True
        else:
            return False
    
    def consultar(self, filter:str):
        conexiondb = self.conexiondb
        cursor = conexiondb.cursor()
        consulta = f"SELECT * FROM Resultados WHERE {filter}" #Realizando una consulta con el filtro proporcionado
        cursor.execute(consulta) #Ejecuntando la consulta
        resultado = cursor.fetchall() #Recibiendo los resultados de la consulta
        cursor.close()
        return resultado #Retornando los resultados

if __name__ == "__main__":
    host = "127.0.0.1"
    user = "root"
    password = ""
    database = "olimpiadas"
    conexiondb = ResultadosMySQL(host, user, password, database)
    #conexion
    conexiondb.conectar()
    #insertar
    print(conexiondb.insertar(1, 1, 1, 3, 4, 6))
    #editar
    print(conexiondb.editar(5, 10, 15))
    #eliminar
    print(conexiondb.eliminar(1, 1, 1))
    #consultar
    print(conexiondb.consultar("idPais = 1"))
    print(conexiondb.consultar("idPais = 1 and idOlimpiada = 2"))
    #desconectando
    conexiondb.desconectar()