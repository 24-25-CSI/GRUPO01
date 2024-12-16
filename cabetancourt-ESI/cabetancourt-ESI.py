def cifrar_mensaje(mensaje):
    # Reemplazar espacios con "-"
    # Con la funcion .replace() se reemplaza un caracter por otro en una cadena de texto
    mensaje = mensaje.replace(" ", "-")
    
    # Definir el número de filas y calcular el número de columnas
    # Define por defecto 5 filas y calcula el número de columnas como el máximo entre 3 y 
    # la cantidad de caracteres del mensaje dividido entre 5 esto para garantizar que la 
    # clave sea de 5 fila y almenos 3 columnas
    filas = 5
    columnas = max(3, (len(mensaje) + filas - 1) // filas)
    
    # Crear la matriz de cifrado con el tamaño calculado
    matriz = [['*' for _ in range(columnas)] for _ in range(filas)]
    
    # Llenar la matriz con el mensaje original
    index = 0
    for i in range(filas):
        for j in range(columnas):
            if index < len(mensaje):
                matriz[i][j] = mensaje[index]
                index += 1
    
    # Mostrar el mensaje original
    print("Mensaje original:", mensaje)
    
    # Mostrar la matriz de cifrado
    print("Matriz de cifrado:")
    for fila in matriz:
        print(" ".join(fila))
    
    # Crear el mensaje cifrado leyendo por columnas
    mensaje_cifrado = ""
    for j in range(columnas):
        for i in range(filas):
            mensaje_cifrado += matriz[i][j]
    
    # Mostrar el mensaje cifrado
    print("Mensaje cifrado:", mensaje_cifrado)

# Ejemplo de uso
mensaje = input("Ingrese el mensaje a cifrar: ")
cifrar_mensaje(mensaje)