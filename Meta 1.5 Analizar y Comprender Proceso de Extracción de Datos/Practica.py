"""Extracción de datos de la pagina de Amazon (Nombre del producto, rating, precio y fecha de entrega),
utilizando Selenium y BeautifulSoup.
Alexis Cruz Miros Grupo 951 Fecha: 17/03/2024"""

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
#Solo los que tienen la extensión
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def bot_extraccion(busqueda:str, cant_paginas:int):
    servicio = Service(ChromeDriverManager().install()) #Obteniendo los servicios
    opciones = Options() #Opciones para enviar parametros de comportamiento.
    opciones.add_argument("--window-size = 1020, 1200") #Tamaño de la ventana.
    navegador = webdriver.Chrome(service=servicio, options=opciones) #Creando el navegador con las configuraciones correspondientes.
    navegador.get("https://www.amazon.com/") #Obteniendo la pagina del navegador para navegar en esta misma.
    time.sleep(15) #Tiempo de espera para llenar el capchat.
    
    barra_busqueda = navegador.find_element(By.ID, "twotabsearchtextbox") #Buscando la "Barra de busqueda".
    time.sleep(3) #Tiempo de espera
    barra_busqueda.send_keys(busqueda) #Insertando el texto de la busqueda.
    time.sleep(5) #Tiempo de espera.

    btn_busqueda = navegador.find_element(By.ID, "nav-search-submit-text") #Buscando el boton de "Buscar".
    btn_busqueda.click() #Haciendo click.
    time.sleep(10) #Tiempo de espera.

    datos = {"nombre":[],
             "rating":[],
             "precio":[],
             "fecha_de_entrega":[]}
    
    for pagina in range(cant_paginas):
        if pagina == cant_paginas: #Condición si se cumple la cantidad de capturas por paginas.
            navegador.close() #Función para cerrar el navegador.

        soup = BeautifulSoup(navegador.page_source, "html5lib") #Construyendo la estructura del codigo html y en su formato correspondiente
        bloques_informacion = soup.findAll("div", attrs={"class":"a-section a-spacing-small puis-padding-left-small puis-padding-right-small"})
        for bloque in bloques_informacion:
            nombre = bloque.find("span", attrs={"class":"a-size-base-plus a-color-base a-text-normal"})
            raiting = bloque.find("span", attrs={"class":"a-icon-alt"})
            precio = bloque.find("span", attrs={"class":"a-price"})
            fecha_entrega = bloque.find("span", attrs={"class":"a-color-base a-text-bold"})
            
            #Guardando los datos
            datos["nombre"].append(nombre.text)

            if raiting is not None:
                datos["rating"].append(raiting.text)
            else:
                datos["rating"].append("0 de 5 estrellas")

            if precio is not None:
                datos["precio"].append(precio.span.text)
            else:
                datos["precio"].append("No se encontró")

            if fecha_entrega is not None:
                datos["fecha_de_entrega"].append(fecha_entrega.text)
            else:
                datos["fecha_de_entrega"].append("Sin fecha de entrega")
        
        if cant_paginas > 1:
            btn_siguiente = navegador.find_element(By.LINK_TEXT, "Siguiente") #Buscando el boton "Siguiente".
            btn_siguiente.click() #Funcion clic en el boton "Siguiente".
            time.sleep(8) #Timepo de espera.

    df = pd.DataFrame(datos)
    return df

if __name__ == "__main__":
    busqueda = input("Que deseas buscar: ")
    paginas = int(input("Cuantas paginas deseas capturar: "))
    df = bot_extraccion(busqueda, paginas)
    df.to_csv("SRC/Dataset/Amazon.csv")