import time
import random
import string
import os

# Función para generar una palabra aleatoria
def generar_palabra_aleatoria(longitud_palabra=4):
    """Genera una palabra aleatoria con una longitud dada."""
    return ''.join(random.choices(string.ascii_lowercase, k=longitud_palabra))

# Función para generar un archivo con n palabras aleatorias
def generar_texto_aleatorio(n, longitud_palabra=4):
    """Genera un texto con n palabras aleatorias de longitud longitud_palabra."""
    texto_aleatorio = ' '.join(generar_palabra_aleatoria(longitud_palabra) for _ in range(n))
    return texto_aleatorio

# Función de encriptación usando el algoritmo de Vigenère
def vigenere_encrypt(plaintext, key):
    encrypted_text = []
    key = key.lower()  # Convertimos la clave a minúsculas
    key_index = 0  # Índice para recorrer la clave

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            if char.islower():
                encrypted_text.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            elif char.isupper():
                encrypted_text.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
            key_index += 1
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text)

# Función de desencriptación usando el algoritmo de Vigenère
def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    key = key.lower()  # Convertimos la clave a minúsculas
    key_index = 0  # Índice para recorrer la clave

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            if char.islower():
                decrypted_text.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
            elif char.isupper():
                decrypted_text.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
            key_index += 1
        else:
            decrypted_text.append(char)

    return ''.join(decrypted_text)

# Función para generar la clave extendida para el texto
def generar_clave_extendida(texto, clave):
    """Extiende la clave para que tenga la misma longitud que el texto."""
    clave_extendida = []
    key_index = 0
    for char in texto:
        if char.isalpha():  # Solo extiende la clave para caracteres alfabéticos
            clave_extendida.append(clave[key_index % len(clave)])
            key_index += 1
        else:
            clave_extendida.append(' ')  # Preserva espacios u otros caracteres
    return ''.join(clave_extendida)

# Función para guardar el archivo
def save_file(content, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"El archivo '{filename}' ha sido guardado.")

# Función para leer un archivo
def read_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        print(f"El archivo '{filename}' no existe.")
        return None

# Función para contar caracteres en un texto
def contar_caracteres(texto):
    """Cuenta y retorna el número de caracteres en el texto."""
    return len(texto)+1

# Función principal para medir tiempos y realizar procesos
def main():
    tiempos = {}

    # Leer el archivo generado para encriptar
    n = int(input("Introduce el número de palabras para el archivo: "))
    texto_generado = generar_texto_aleatorio(n)
    nombre_archivo_generado = f"texto_generado_{n}_palabras.txt"
    save_file(texto_generado, nombre_archivo_generado)

    start_time = time.time()
    print("Leyendo el archivo generado...")
    file_content = read_file(nombre_archivo_generado)
    tiempos['T-E1'] = (time.time() - start_time) * 1000  # Tiempo de lectura del archivo
    if not file_content:
        return

    # Contar caracteres del archivo original
    caracteres_originales = contar_caracteres(file_content)

    # Solicitar la clave de Vigenère
    key = input("Introduce la clave de Vigenère: ").strip()

    # Medir el tiempo para generar la clave extendida
    start_time = time.time()
    clave_extendida = generar_clave_extendida(file_content, key)
    tiempos['T-E2'] = (time.time() - start_time) * 1000  # Tiempo de generación de la clave

    # Encriptación
    start_time = time.time()
    print("\nEncriptando el archivo...")
    encrypted_content = vigenere_encrypt(file_content, key)
    encrypted_filename = f"encriptado_{nombre_archivo_generado}"
    save_file(encrypted_content, encrypted_filename)
    tiempos['T-E3'] = (time.time() - start_time) * 1000  # Tiempo de encriptación

    # Contar caracteres del archivo encriptado
    caracteres_encriptados = contar_caracteres(encrypted_content)

    # Desencriptación
    start_time = time.time()
    print("\nDesencriptando el archivo...")
    decrypted_content = vigenere_decrypt(encrypted_content, key)
    decrypted_filename = f"desencriptado_{nombre_archivo_generado}"
    save_file(decrypted_content, decrypted_filename)
    tiempos['T-E4'] = (time.time() - start_time) * 1000  # Tiempo de desencriptación

    # Contar caracteres del archivo desencriptado
    caracteres_desencriptados = contar_caracteres(decrypted_content)

    # Tiempos totales
    tiempos['T-Total'] = sum(tiempos.values())

    # Mostrar tiempos
    print("\n--- Tiempos de Ejecución ---")
    print(f"T-E1: Tiempo de ejecución para la etapa de lectura del archivo: {tiempos['T-E1']:.2f} ms")
    print(f"T-E2: Tiempo de ejecución para la generación de claves: {tiempos['T-E2']:.2f} ms")
    print(f"T-E3: Tiempo de ejecución para cifrar el texto: {tiempos['T-E3']:.2f} ms")
    print(f"T-E4: Tiempo de ejecución para descifrar el texto: {tiempos['T-E4']:.2f} ms")
    print(f"T-Total: Tiempo total de ejecución: {tiempos['T-Total']:.2f} ms")

    # Mostrar conteo de caracteres
    print("\n--- Conteo de Caracteres ---")
    print(f"Caracteres en el archivo original: {caracteres_originales}")
    print(f"Caracteres en el archivo encriptado: {caracteres_encriptados}")
    print(f"Caracteres en el archivo desencriptado: {caracteres_desencriptados}")

# Ejecutar el proceso
if __name__ == "__main__":
    main()
