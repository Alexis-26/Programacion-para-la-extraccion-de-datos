"""Ejemplos de como hacer un diccionario"""
"Formas de crear un diccionario"
d1 = {}

d2 = dict()

d3 = {"nombre":"Josue",
      "edad":20}

lista = [("nombre", "Miguel"), ("edad", 21)]

d4 = dict(lista)

d5 = dict(nombre = "Maria", edad = 20)

"Forma para agregar o modificar un valor"
d3["dire"] = "Avenida"

d3["carrera"] = "LIN"

"Extraer valores"
print(d3["nombre"])

print(d3.get("nombre"))

print(d3.get("nombre", "no existe"))

print("========================================")

"Acceder a la clave - valor"
for key in d3:
    print(key, d3[key])

for key, value in d3.items():
    print(key, value)

print("========================================")
"Funciones"
x = d3.pop("dire") #Retorna el valor que contiene la clave
print(d3)
print(x)

y = d3.popitem() #Retorna una tupla con la clave y el valor
print(d3)
print(y)

llaves = list(d3.keys()) #Obtiene todas las llaves en una lista ya que si es sin list retorna un objeto no necesario

valores = list(d3.values()) #Obtiene los valores del diccionario y al igual sin el list retorna un objeto no necesario

todo = list(d3.items()) #Obtienes todo el diccionario con claves y valores sin list retorna un objeto no necesario
print("========================================")

"leetcode para hacer pruebas y neetcode es youtuber que resuelve problemas de leetcode"
dorigninal = {"a":1, "b":2}
dupdate = {"a":0, "d":4}
dorigninal.update(d2)
print(d1)