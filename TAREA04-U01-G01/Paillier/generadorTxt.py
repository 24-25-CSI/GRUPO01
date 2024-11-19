# Crear un archivo de texto con 10,000,000 palabras
with open('C:/Users/User/Desktop/Pasantias/generador/Lorem10000000.txt', 'w') as file:
    for _ in range(10000000):
        # Escribe la palabra 'hola' y un espacio
        file.write('hola ')
