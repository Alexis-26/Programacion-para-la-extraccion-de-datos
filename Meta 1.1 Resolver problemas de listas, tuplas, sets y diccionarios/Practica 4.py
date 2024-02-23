"""Alexis Cruz Miros 951 19/02/2024
Estadística Básica. 
Cree una clase llamada Estadística que contiene como atributo una lista de números naturales 
la cual puede contener repetidos. Debe contener los siguientes métodos:
a. Frecuencia de Números. Dada la lista, devuelve un diccionario con el número de veces que 
aparece cada número en la lista.
b. Moda. Dada la lista, devuelva la moda de la lista (el valor más repetido). 
Puedes usar la función anterior como ayuda.
c. Histograma. Dada la lista, muestra el histograma de la lista. 
Puedes reusar los métodos anteriores. 
"""
class Estadistica:
    def __init__(self, lista):
        self.listaNumeros = lista
    
    def frecuencia(self):
        lista = self.listaNumeros
        d_frecuencia = {}

        for i in lista:
            count = 0
            for j in lista:
                if i == j:
                    count += 1
            d_frecuencia[i] = count

        return d_frecuencia 
    
    def moda(self):
        lista = self.listaNumeros
        d_frecuencia = {}
        lista_aux = []

        for i in lista:
            count = 0
            for j in lista:
                if i == j:
                    count += 1
            d_frecuencia[i] = count
        
        for k, v in d_frecuencia.items():
            lista_aux.append(v)
        
        resultadoModa = max(lista_aux)

        for k, v in d_frecuencia.items():
            if resultadoModa == v:
                return k

        
    def histograma(self):
        lista = self.listaNumeros
        d_frecuencia = {}

        for i in lista:
            count = 0
            for j in lista:
                if i == j:
                    count += 1
            d_frecuencia[i] = count
            
        barra = []
        num = []
        for index in d_frecuencia:
            num.append(index)
            largo_barra = "*" * d_frecuencia[index]
            barra.append(largo_barra)
        
        hist = ""
        for index in num:
            hist = hist + str(index) + " " + barra.pop(0) + "\n"
        return hist
    
lista = Estadistica([1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1])

print(lista.frecuencia())
print(lista.moda())
print(lista.histograma())
