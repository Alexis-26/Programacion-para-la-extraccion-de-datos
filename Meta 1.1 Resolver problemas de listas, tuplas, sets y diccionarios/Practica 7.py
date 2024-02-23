"""Alexis Cruz Miros 951 22/02/2024
Encriptación y Desencriptación de Mensajes Secretos. 
Tú y tu mejor amigo están creando un sistema secreto para enviar mensajes entre ustedes 
sin que nadie más pueda entenderlos. 
Deciden utilizar un método de encriptación y desencriptación basado en listas o diccionarios.
"""

"""Encriptación. Crear una función llamada encriptar_mensaje que tome como entrada un mensaje de texto 
y utilice un diccionario para reemplazar cada letra por un código secreto. 
El diccionario de encriptación debe asignar a cada letra una cadena de caracteres 
alfanuméricos aleatorios."""
def encriptar_mensaje(mensaje):
    dict_encriptado = {'a':'!','b':'@','c':'"','d':'#',
                       'e':'$','f':'%','g':'&','h':'/',
                       'i':'(','j':')','k':'=','l':'?',
                       'm':'¿','n':'¡','o':'|','p':'°',
                       'q':'+','r':'*','s':'-','t':'_',
                       'u':',','v':'.','w':';','x':':',
                       'y':'[','z':']',' ':'¨'}
    resultado = ""
    for letra in mensaje:
        for k, v in dict_encriptado.items():
            if letra == k:
                resultado += v
    return resultado

"""Desencriptación. Crear una función llamada desencriptar_mensaje que tome como entrada 
un mensaje encriptado y utilice el mismo diccionario para revertir el proceso 
y obtener el mensaje original."""
def desencriptar_mensaje(mensaje):
    dict_encriptado = {'a':'!','b':'@','c':'"','d':'#',
                       'e':'$','f':'%','g':'&','h':'/',
                       'i':'(','j':')','k':'=','l':'?',
                       'm':'¿','n':'¡','o':'|','p':'°',
                       'q':'+','r':'*','s':'-','t':'_',
                       'u':',','v':'.','w':';','x':':',
                       'y':'[','z':']',' ':'¨'}
    resultado = ""
    for character in mensaje:
        for k, v in dict_encriptado.items():
            if character == v:
                resultado += k
    return resultado

mensaje = input()
print(encriptar_mensaje(mensaje))

mensaje = input()
print(desencriptar_mensaje(mensaje))
