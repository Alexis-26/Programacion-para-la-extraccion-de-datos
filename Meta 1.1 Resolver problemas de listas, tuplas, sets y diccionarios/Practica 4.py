"""Alexis Cruz Miros 951 13/02/2024

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
        pass

lista = Estadistica([1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1])

print(lista.frecuencia())
print(lista.moda())

