from phe import paillier
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import time

# Medir tiempo total de ejecución
start_time_total = time.time()

# Generar claves Paillier
start_time_keygen = time.time()
public_key, private_key = paillier.generate_paillier_keypair()
end_time_keygen = time.time()

# Ruta del archivo 10 palabras
#input_file = "C:/Users/User/Desktop/Pasantias/generador/Lorem10.txt"
#output_file = "C:/Users/User/Desktop/Pasantias/Salida/Lorem10CIFRADO.txt"

# Ruta del archivo 100 palabras
#input_file = "C:/Users/User/Desktop/Pasantias/generador/Lorem100.txt"
#output_file = "C:/Users/User/Desktop/Pasantias/Salida/Lorem100CIFRADO.txt"

# Ruta del archivo 1000 palabras
#input_file = "C:/Users/User/Desktop/Pasantias/generador/Lorem1000.txt"
#output_file = "C:/Users/User/Desktop/Pasantias/Salida/Lorem1000CIFRADO.txt"

# Ruta del archivo 10000 palabras
#input_file = "C:/Users/User/Desktop/Pasantias/generador/Lorem10000.txt"
#output_file = "C:/Users/User/Desktop/Pasantias/Salida/Lorem10000CIFRADO.txt"

# Ruta del archivo 100000 palabras
#input_file = "C:/Users/User/Desktop/Pasantias/generador/Lorem100000.txt"
#output_file = "C:/Users/User/Desktop/Pasantias/Salida/Lorem100000CIFRADO.txt"

# Ruta del archivo 1000000 palabras
#input_file = "C:/Users/User/Desktop/Pasantias/generador/Lorem1000000.txt"
#output_file = "C:/Users/User/Desktop/Pasantias/Salida/Lorem1000000CIFRADO.txt"

# Ruta del archivo 10 000 000 palabras
input_file = "C:/Users/User/Desktop/Pasantias/generador/Lorem10000000.txt"
output_file = "C:/Users/User/Desktop/Pasantias/Salida/Lorem10000000CIFRADO.txt"



# Leer archivo de entrada
start_time_read = time.time()
with open(input_file, 'rb') as f_in:
    file_data = f_in.read()
end_time_read = time.time()

# Número de caracteres de entrada
input_length = len(file_data)

# Generar clave simétrica para AES
aes_key = get_random_bytes(16)  # Clave de 128 bits
print("Clave AES original:", aes_key)

# Cifrar la clave AES con Paillier
encrypted_aes_key = [public_key.encrypt(byte) for byte in aes_key]
print("\nClave AES cifrada:", encrypted_aes_key)

# Cifrar el archivo con AES
start_time_encrypt = time.time()
cipher = AES.new(aes_key, AES.MODE_EAX)
with open(output_file, 'wb') as f_out:
    nonce = cipher.nonce
    f_out.write(nonce)  # Guardar el nonce al principio del archivo
    ciphertext = cipher.encrypt(file_data)
    f_out.write(ciphertext)
end_time_encrypt = time.time()

# Número de caracteres de salida
output_length = len(nonce) + len(ciphertext)

print(f"\nArchivo cifrado guardado en: {output_file}")

# Ruta del archivo cifrado 10 palabras
#input_file = "C:/Users/User/Desktop/Pasantias/Salida/Lorem10CIFRADO.txt"
#output_file = "C:/Users/User/Desktop/Pasantias/Decifrado/Lorem10DESCIFRADO.txt"

# Ruta del archivo cifrado 100 palabras
#input_file = "C:/Users/User/Desktop/Pasantias/Salida/Lorem100CIFRADO.txt"
#output_file = "C:/Users/User/Desktop/Pasantias/Decifrado/Lorem100DESCIFRADO.txt"

# Ruta del archivo cifrado 1000 palabras
#input_file = "C:/Users/User/Desktop/Pasantias/Salida/Lorem1000CIFRADO.txt"
#output_file = "C:/Users/User/Desktop/Pasantias/Decifrado/Lorem1000DESCIFRADO.txt"

# Ruta del archivo cifrado 10000 palabras
#input_file = "C:/Users/User/Desktop/Pasantias/Salida/Lorem10000CIFRADO.txt"
#output_file = "C:/Users/User/Desktop/Pasantias/Decifrado/Lorem10000DESCIFRADO.txt"

# Ruta del archivo cifrado 100000 palabras
#input_file = "C:/Users/User/Desktop/Pasantias/Salida/Lorem100000CIFRADO.txt"
#output_file = "C:/Users/User/Desktop/Pasantias/Decifrado/Lorem100000DESCIFRADO.txt"

# Ruta del archivo cifrado 1000000 palabras
#input_file = "C:/Users/User/Desktop/Pasantias/Salida/Lorem1000000CIFRADO.txt"
#output_file = "C:/Users/User/Desktop/Pasantias/Decifrado/Lorem1000000DESCIFRADO.txt"

# Ruta del archivo cifrado 10000000 palabras
input_file = "C:/Users/User/Desktop/Pasantias/Salida/Lorem10000000CIFRADO.txt"
output_file = "C:/Users/User/Desktop/Pasantias/Decifrado/Lorem10000000DESCIFRADO.txt"



# Descifrar la clave AES
decrypted_aes_key = bytes([private_key.decrypt(enc_byte)
                          for enc_byte in encrypted_aes_key])
print("Clave AES descifrada:", decrypted_aes_key)

# Abrir el archivo cifrado y descifrarlo
start_time_decrypt = time.time()
with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
    # Leer el nonce del archivo
    nonce = f_in.read(16)

    # Crear el objeto de descifrado AES
    cipher = AES.new(decrypted_aes_key, AES.MODE_EAX, nonce=nonce)

    # Leer y descifrar el resto del archivo en chunks
    while chunk := f_in.read(8192):
        plaintext = cipher.decrypt(chunk)
        f_out.write(plaintext)
end_time_decrypt = time.time()

print(f"\nArchivo descifrado guardado en: {output_file}")

# Medir tiempo total de ejecución
end_time_total = time.time()

# Imprimir tiempos de ejecución en milisegundos
print ("\nTiempos 100 palabras")
print ("\nTiempos de ejecución en milisegundos:")
print(f"\nTiempo de generación de clave: {(end_time_keygen - start_time_keygen) * 1000} milisegundos")
print(f"Tiempo de lectura del archivo de entrada: {(end_time_read - start_time_read) * 1000} milisegundos")
print(f"Tiempo de cifrado del texto: {(end_time_encrypt - start_time_encrypt) * 1000} milisegundos")
print(f"Tiempo de descifrado del texto: {(end_time_decrypt - start_time_decrypt) * 1000} milisegundos")
print(f"Tiempo total de ejecución: {(end_time_total - start_time_total) * 1000} milisegundos")

# Imprimir número de caracteres de entrada y salida
print(f"\nNúmero de caracteres de entrada: {input_length}")
print(f"Número de caracteres de salida: {output_length}")