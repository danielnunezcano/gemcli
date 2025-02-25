import subprocess

def write_and_read_aux_file(file_path, editor="nvim"):

    # Asegurarse de que el archivo existe (si no, se crea vacío)
    with open(file_path, 'a+', encoding='utf-8'):
        pass

    # Abrir el editor para editar el archivo
    subprocess.call([editor, '+', file_path])

    # Leer el contenido del archivo
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().strip()

    return content