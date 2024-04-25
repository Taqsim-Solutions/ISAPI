from PIL import Image
import os

def reducir_tamano_imagen(imagen_path, tamano_maximo_kb, destino_path):
    # Abrir la imagen
    imagen = Image.open(imagen_path)
    
    # Obtener el tamaño actual de la imagen en bytes
    tamano_actual_bytes = os.path.getsize(imagen_path)
    
    # Calcular el factor de compresión necesario para reducir el tamaño de la imagen
    factor_compresion = tamano_maximo_kb * 1024 / tamano_actual_bytes
    
    # Si la imagen ya está dentro del tamaño máximo, simplemente copiarla al destino
    if factor_compresion >= 1:
        imagen.save(destino_path)
        return
    
    # Reducir el tamaño de la imagen
    nueva_tamano = (int(imagen.width * factor_compresion), int(imagen.height * factor_compresion))
    imagen = imagen.resize(nueva_tamano, Image.ANTIALIAS)
    
    # Guardar la imagen reducida en el destino
    imagen.save(destino_path)

# Ejemplo de uso
imagen_original = "imagen_original.jpg"
imagen_destino = "imagen_reducida.jpg"
tamano_maximo_kb = 200

reducir_tamano_imagen(imagen_original, tamano_maximo_kb, imagen_destino)
