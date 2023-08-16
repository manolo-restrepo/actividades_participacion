import random

def generar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = [random.randint(1, 100) for e in range(columnas)]
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

filas = int(input("ingrese el numero de filas"))
columnas = int(input("ingrese el numero de columnas"))

matriz_generada = generar_matriz(filas, columnas)
imprimir_matriz(matriz_generada)
