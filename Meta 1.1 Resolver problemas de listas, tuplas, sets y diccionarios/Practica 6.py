"""Alexis Cruz Miros 951 22/02/2024
Sistema de Reserva. Desarrolla un sistema de reservas utilizando sets. 
Crea conjuntos para representar habitaciones disponibles y habitaciones reservadas en un hotel. 
Permite a los usuarios realizar reservas, liberar habitaciones y mostrar la disponibilidad actual. 
NOTA: No utilizar menú,  solo las funciones , realizar las pruebas necesarias para verificar 
funcionamiento adecuado.
"""
habitacionesDisp = {1, 2, 3, 4, 5, 6}
habitacionesRes = set()

def reservar(num):
    if num in habitacionesRes:
        return print("Esta habitación se encuentra reservada")
    else:
        habitacionesRes.add(num)
        return print("Habitación reservada correctamente")

def liberar(num):
    habitacionesRes.remove(num)
    return print("Habitación liberada correctamente")

def consulta():
    resultado = habitacionesDisp.difference(habitacionesRes)
    return f"Habitaciones diponibles: {resultado}"

reservar(1)
reservar(2)
reservar(4)
reservar(6)
reservar(6)
consulta()

liberar(1)
liberar(4)
consulta()





