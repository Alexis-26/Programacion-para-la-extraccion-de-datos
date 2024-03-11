"""Generación de capturas de pantalla de un producto en diferentes paginas de Amazon.
Alexis Cruz Miros Grupo 951 Fecha: 10/03/2024"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
#Solo los que tienen la extensión
from webdriver_manager.chrome import ChromeDriverManager

def bot_loging(busqueda:str, cant_paginas:int):
    servicio = Service(ChromeDriverManager().install()) #Obteniendo los servicios
    opciones = Options() #Opciones para enviar parametros de comportamiento.
    opciones.add_argument("--window-size = 1020, 1200") #Tamaño de la ventana.
    navegador = webdriver.Chrome(service=servicio, options=opciones) #Creando el navegador con las configuraciones correspondientes.
    navegador.get("https://www.amazon.com/") #Obteniendo la pagina del navegador para navegar en esta misma.
    time.sleep(10) #Tiempo de espera para llenar el capchat.
    
    barra_busqueda = navegador.find_element(By.ID, "twotabsearchtextbox") #Buscando la "Barra de busqueda".
    time.sleep(3) #Tiempo de espera
    barra_busqueda.send_keys(busqueda) #Insertando el texto de la busqueda.
    time.sleep(5) #Tiempo de espera.

    btn_busqueda = navegador.find_element(By.ID, "nav-search-submit-text") #Buscando el boton de "Buscar".
    btn_busqueda.click() #Haciendo click.
    time.sleep(10) #Tiempo de espera.

    for pagina in range(cant_paginas):
        navegador.save_screenshot("SRC/Imagenes/test" + str(pagina) + ".png") #Guardando la captura.
        btn_siguiente = navegador.find_element(By.LINK_TEXT, "Siguiente") #Buscando el boton "Siguiente".
        btn_siguiente.click() #Funcion clic en el boton "Siguiente".
        time.sleep(8) #Timepo de espera.
        if pagina == cant_paginas: #Condición si se cumple la cantidad de capturas por paginas.
            navegador.close() #Función para cerrar el navegador.

if __name__ == "__main__":
    busqueda = input("Que deseas buscar: ")
    paginas = int(input("Cuantas paginas deseas capturar: "))
    bot_loging(busqueda, paginas)