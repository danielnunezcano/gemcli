import subprocess

def writeAndReadAuxFile(nombre_archivo):
    with open(nombre_archivo, 'a+', encoding='utf-8') as f:
        pass  # Esto asegura que el archivo se crea si no existe
    # Abrir nvim para editar el archivo temporal
    subprocess.call(['nvim', '+', nombre_archivo])

    # Leer el contenido del archivo temporal después de que nvim lo cierre
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        frase = f.read().strip()

    # Eliminar el archivo temporal
    return frase

