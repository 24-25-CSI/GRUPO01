def cifrado_permutacion_filas(mensaje, clave):
    print("Mensaje original:", mensaje)
    mensaje = mensaje.replace(" ", "-")

    filas = len(clave)  
    columnas = -(-len(mensaje) // filas)  

    
    mensaje += "*" * (filas * columnas - len(mensaje))

    matriz = []
    for i in range(filas):
        inicio = i * columnas
        fin = inicio + columnas
        matriz.append(list(mensaje[inicio:fin]))

    print("Matriz de cifrado:")
    for fila in matriz:
        print(" ".join(fila))
    
    
    matriz_permutada = [matriz[i] for i in clave]

    mensaje_cifrado = "".join(
        matriz_permutada[fila][columna]
        for columna in range(columnas)
        for fila in range(filas)
    )
    # print("Matriz permutada:")
    # for fila in matriz_permutada:
    #     print(" ".join(fila))

    print("Mensaje cifrado:", mensaje_cifrado)

    return mensaje_cifrado

mensaje = input("ingrese el mensaje a cifrar: ")
clave = [4, 2, 0, 3, 1]  

cifrado = cifrado_permutacion_filas(mensaje, clave)


   