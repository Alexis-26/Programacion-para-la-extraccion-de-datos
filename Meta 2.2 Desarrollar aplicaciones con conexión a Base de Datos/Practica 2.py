"""Desarrollar una clase llamada PaisMySQL que herede de  MySQLConnect. Debe agregar los atributos correspondientes de la clase padre. 
Debe agregar los siguientes métodos:
1. insertar(id, nombre): Método para insertar datos en la Tabla Pais, debe recibir como parámetro las columnas de la tabla y 
debe retornar True si se inserta el dato o False en caso contrario.

2. editar(nombre): Método para editar el nombre en la Tabla País. Validar que nombre no exista en la tabla. #update

3. eliminar(id): Método para eliminar un elemento de la Tabla País. Debe tener como parámetro la llave primaria, 
retorna True si logró eliminarse y False en caso contrario.

4. consultar(filter): Método que recibe un filtro(cadena) y retorna una lista de tuplas con los resultados del 
filtro de la Tabla País. Ejemplo: “id = 1” , “nombre like %A%” #like

Alexis Cruz Miros Grupo 951 Fecha: 20/04/2024"""

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
        
class PaisMySQL(MySQLConnect): #Creando una clase hija
    def __init__(self, host: str, user: str, password: str, database: str) -> None:
        super().__init__(host, user, password, database) #Agregando los atributos de la clase padre
    
    def insertar(self, id_pais:int, nombre:str):
        conexiondb = self.conexiondb
        cursor = conexiondb.cursor()
        validacion = "select * from Pais where id = %s;"
        cursor.execute(validacion, (id_pais, )) #id_pais lo estoy mandando como remplazo de %s (Para que se remplace se ocupa que sea una tupla)
        resultados = cursor.fetchall()

        if not resultados:
            insert = "INSERT INTO Pais(id, nombre) values(%s, %s);"
            datos_insertar = (id_pais, nombre)
            cursor.execute(insert, datos_insertar)
            conexiondb.commit() #Actualiza los cambios realizados (sirve para hacer una confirmacion)
            cursor.close()
            return True
        else:
            return False
    
    def editar(self, nombre:str):
        conexiondb = self.conexiondb
        cursor = conexiondb.cursor()
        validacion = "SELECT * FROM Pais WHERE nombre like %s;" #Realizando una consulta para validar que existe el dato
        parametro = f"%{nombre}%" #Cambiando el formato para utilizarlo en un like de SQL
        cursor.execute(validacion, (parametro, )) #Enviando la validacion y los valores que sustituyen %s para evitar inyeccion
        resultado = cursor.fetchall() #Recibiendo los resultados obtenidos de la consulta
        if resultado:
            dato = str(input("Nuevo valor: ")) #Recibiendo el nuevo valor para el dato a editar
            update = "UPDATE Pais SET nombre = %s WHERE nombre like %s;" #Realizando un update
            cursor.execute(update, (dato, parametro)) #Enviando el update y los valores que sustituyen %s
            conexiondb.commit() #Guardando los cambios
            cursor.close()
            return True
        else:
            return False
        
    def eliminar(self, id_pais:int):
        conexiondb = self.conexiondb
        cursor = conexiondb.cursor()
        validacion = "SELECT * FROM Pais WHERE id = %s;" #Validando que existe el dato
        cursor.execute(validacion, (id_pais, )) #Envando la consulta y sustituyendo %s
        resultado = cursor.fetchall() #Recibiendo los resultados de la consultando
        if resultado: #Validando si existen los datos
            delete = "DELETE FROM Pais WHERE id = %s;" #Realizando la eliminacion
            cursor.execute(delete, (id_pais, )) #Ejecutando y enviando el delete y sustituyendo %s
            conexiondb.commit() #Guardando los cambios
            cursor.close()
            return True
        else:
            return False
        
    def consultar(self, filter:str):
        conexiondb = self.conexiondb
        cursor = conexiondb.cursor()
        consulta = f"SELECT * FROM Pais WHERE {filter}" #Realizando una consulta con el filtro proporcionado
        cursor.execute(consulta) #Ejecuntando la consulta
        resultado = cursor.fetchall() #Recibiendo los resultados de la consulta
        cursor.close()
        return resultado #Retornando los resultados


if __name__ == "__main__":
    host = "127.0.0.1"
    user = "root"
    password = ""
    database = "olimpiadas"
    conexiondb = PaisMySQL(host, user, password, database)
    #conexion
    conexiondb.conectar()
    #insertar
    print(conexiondb.insertar(3, "Brasil"))
    #editar
    print(conexiondb.editar("Francia"))
    #eliminar
    print(conexiondb.eliminar(1))
    #consultar
    print(conexiondb.consultar("id = 1"))
    print(conexiondb.consultar("nombre like '%Francia%'"))
    #desconectando
    conexiondb.desconectar()