# -*- coding: utf-8 -*-
"""Welcome To Colab

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

def cifrar_mensaje(mensaje):
    try:
        # Reemplazar espacios con "-"
        mensaje = mensaje.replace(" ", "-")

        # Determinar el número de columnas necesarias
        filas = 5
        longitud_mensaje = len(mensaje)
        columnas = (longitud_mensaje + filas - 1) // filas

        # Asegurar al menos 3 columnas (no es estrictamente necesario en este caso)
        columnas = max(columnas, 3)

        # Crear la matriz de cifrado
        matriz = [['*' for _ in range(columnas)] for _ in range(filas)]

        # Llenar la matriz con el mensaje
        index = 0
        for j in range(columnas): # Recorrer primero las columnas
            for i in range(filas): # Luego las filas
                if index < longitud_mensaje:
                    matriz[i][j] = mensaje[index]
                    index += 1

        # Leer la matriz por filas para obtener el mensaje cifrado
        mensaje_cifrado = ''
        for i in range(filas):
            for j in range(columnas):
                mensaje_cifrado += matriz[i][j]

        # Mostrar resultados
        print("Mensaje original:", mensaje)
        print("Matriz de cifrado:")
        for fila in matriz:
            print(' '.join(fila))
        print("Mensaje cifrado:", mensaje_cifrado)

    except Exception as e:
        print("Error:", str(e))

# Ejemplo de uso
mensaje = "ejercicio uno"
cifrar_mensaje(mensaje)