# Crear un archivo de texto con 10,000,000 palabras
with open('C:/Users/Santiago/Desktop/8vo-9no/Cripto/b/TAREA04-U1-G01/Lorem10M.txt', 'w') as file:
    for _ in range(10_000_000):
        # Escribe la palabra 'hola' y un espacio
        file.write('hola ')
