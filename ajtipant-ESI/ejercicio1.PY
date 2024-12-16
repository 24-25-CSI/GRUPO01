def cifrado_permutacion_filas(mensaje, filas=5):

    mensaje = mensaje.replace(" ", "-") # remplazo los espacios por "-"
    
    longitud = len(mensaje)
    columnas = (longitud + filas - 1) // filas  # Calcular el número de columnas necesarias
    if columnas < 3:
        columnas = 3  # Garantizar al menos 3 columnas

    # Matriz
    matriz = []
    indice = 0
    for i in range(filas):
        fila = []
        for j in range(columnas):
            if indice < longitud:
                fila.append(mensaje[indice])
                indice += 1
            else:
                fila.append("*")  
        matriz.append(fila)
    
    # Mostrar la matriz en pantalla
    print("\nMatriz generada:")
    for fila in matriz:
        print(" ".join(fila))
    
    # Leer la matriz por columnas
    mensaje_cifrado = ""
    for j in range(columnas):
        for i in range(filas):
            mensaje_cifrado += matriz[i][j]
    
    return mensaje_cifrado


# Implementacion 
mensaje_original = input("Ingrese el mensaje a cifrar: ")
mensaje_cifrado = cifrado_permutacion_filas(mensaje_original)
print(f"\nMensaje original: {mensaje_original}")
print(f"Mensaje cifrado: {mensaje_cifrado}")
