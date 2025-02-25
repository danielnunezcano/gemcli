import custom_gemini as cgem
import os
import re

# Configuración inicial
MAX_FILE_SIZE = 2000000
CONFIG_FILE_PATH = "/home/daniel/.gemcli-py/config/config.txt"

def question(question_text, conversation_file_path):

    if os.path.exists(conversation_file_path):
        with open(conversation_file_path, "r", encoding="utf-8") as conversation_file:
            conversation = conversation_file.read()

        if os.path.getsize(conversation_file_path) > MAX_FILE_SIZE:
            conversation = summarize_conversation(conversation)
            save_conversation(conversation, conversation_file_path)

        prompt = f"Esta es la conversación que tuvimos anteriormente, HUMAN es lo que digo yo y GEMINI es lo que me contestaste pero no me respondas con GEMINI al principio: {conversation}\n\nte comento lo siguiente: {question_text}"
    else:
        prompt = question_text

    while True:
        try:
            response = None
            pdf_files = extract_files_paths(question_text,"pdf")
            image_files = extract_files_paths(question_text,"image")
            audio_files = extract_files_paths(question_text,"audio")

            if len(pdf_files) > 0:
                response = cgem.generate_pdf_response(prompt,pdf_files[0])
            elif len(image_files) > 0:
                response = cgem.generate_image_response(prompt,image_files)
            elif len(audio_files) > 0:
                response = cgem.generate_audio_response(prompt,audio_files[0])
            else:
                response = cgem.generate_response(prompt)
            return response
        except Exception as e:  # Captura cualquier excepción
            print(f"Error al usar el modelo: {e}")

def summarize_conversation(conversation):
    """
    Resume una conversación larga.

    Args:
        conversation: El texto de la conversación.

    Returns:
        El resumen de la conversación.
    """

    prompt = f"Resumeme lo siguiente: {conversation}"
    response = cgem.generate_response(prompt)
    return response.text

def save_conversation(conversation, conversation_file_path):
    """
    Guarda una conversación en un archivo.

    Args:
        conversation: El texto de la conversación.
        conversation_file_path: La ruta del archivo de conversación.
    """

    with open(conversation_file_path, "w", encoding="utf-8") as conversation_file:
        conversation_file.write("-------GEMINI----------\n")
        conversation_file.write(conversation + "\n")

import re

def extract_files_paths(text, file_type):
    """
    Extrae las rutas de archivos con una estructura específica de un texto.

    Args:
      text (str): El texto del que se extraerán las rutas.
      file_type (str): El tipo de archivo a buscar (por ejemplo, 'pdf', 'image', etc.).

    Returns:
      list: Una lista con las rutas de archivos encontradas.
    """
    if not file_type:
        raise ValueError("El argumento 'file_type' no puede estar vacío.")

    # Construir el patrón dinámico para encontrar rutas basadas en el tipo
    pattern = rf"{file_type}:'(.*?\..*?)'"
    paths = re.findall(pattern, text)
    return paths

