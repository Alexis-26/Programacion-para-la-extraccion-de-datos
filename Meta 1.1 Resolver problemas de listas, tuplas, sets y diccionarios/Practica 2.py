"""Alexis Cruz Miros 951 13/02/2024

"""
def dosnum(nums, target):
    dato = {}
    for index, item in enumerate(nums):
        resultado = target - item
        print(f"Resultado es {resultado}")

        if item in dato:
            return (dato[item], index)
        dato[resultado] = index
        
lista_3 = [2, 7, 11, 15]
target = 22
print(dosnum(lista_3, target))

#if resultado in dato:
            #return (resultado[resultado], index)
        #dato[index]= item 