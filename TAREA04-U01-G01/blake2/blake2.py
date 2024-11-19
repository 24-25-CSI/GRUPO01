from hashlib import blake2b
import time

tiempoInicialTotal = time.time()
# Crear una instancia de blake2b
hasher = blake2b()
tiempoInicialLeerA = time.time()

# Leer el archivo y actualizar el hash
with open('C:/Users/Santiago/Desktop/8vo-9no/Cripto/b/TAREA04-U1-G01/Lorem10M.txt', 'rb') as file:
    while chunk := file.read(8192):
        hasher.update(chunk)

tiempoFinalLeerA = time.time()
tiempoMiliL = (tiempoFinalLeerA - tiempoInicialLeerA) * 1000
print(f"tiempo de lectura: {tiempoMiliL:.3f}")

# Obtener el hash final
tiempoInicialHash = time.time()
digest = hasher.hexdigest()
tiempoFinalHash = time.time()
tiempoMiliH = (tiempoFinalHash - tiempoInicialHash) * 1000
print(f"tiempo de hash: {tiempoMiliH:.3f}")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
# por defecto la salida es en 512 bits
print(digest)
timeFinalTotal = time.time()
tiempoTotal = (timeFinalTotal - tiempoInicialTotal) * 1000
print(f"tiempo total: {tiempoTotal:.3f}")
