import google.generativeai as genai
import os

# Configuración inicial
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
DEFAULT_MODEL = 'gemini-1.5-pro'
model = genai.GenerativeModel(DEFAULT_MODEL)
MAX_FILE_SIZE = 2000000
gemini_model = None  # Inicializa gemini_model como None
CONFIG_FILE_PATH = "/home/danielnezcano/.gemcli-py/config/config.txt"

def question(question_text, conversation_file_path):
    """
    Envía una pregunta a Gemini y obtiene la respuesta.

    Args:
        question_text: El texto de la pregunta.
        conversation_file_path: La ruta del archivo de conversación.

    Returns:
        La respuesta de Gemini.
    """

    global gemini_model, model

    if gemini_model:
        model = genai.GenerativeModel(gemini_model)

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
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:  # Captura cualquier excepción
            print(f"Error al usar el modelo {gemini_model}: {e}")
            set_gemini_model()

def summarize_conversation(conversation):
    """
    Resume una conversación larga.

    Args:
        conversation: El texto de la conversación.

    Returns:
        El resumen de la conversación.
    """

    prompt = f"Resumeme lo siguiente: {conversation}"
    response = model.generate_content(prompt)
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

def get_models():
    """
    Obtiene la lista de modelos disponibles y permite al usuario seleccionar uno.

    Returns:
        El nombre del modelo seleccionado.
    """

    models = list(genai.list_models())
    for i, model in enumerate(models, 1):
        name = model.name.replace("models/", "")
        print(f"{i}\t{name}")

    while True:
        try:
            choice = int(input("Elige un modelo (número): "))
            if 1 <= choice <= len(models):
                return models[choice - 1].name.replace("models/", "")
            else:
                print("Opción inválida. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número.")

def set_gemini_model():
    """
    Permite al usuario seleccionar un modelo y lo guarda en la configuración.
    """

    global gemini_model, model

    print("Elige el modelo")
    gemini_model = get_models()

    with open(CONFIG_FILE_PATH, "w") as f:
        f.write(gemini_model)

    model = genai.GenerativeModel(gemini_model)

def set_init_gemini_model():
    """
    Carga el modelo desde la configuración o establece el modelo predeterminado si no se encuentra.

    Returns:
        El nombre del modelo cargado o el modelo predeterminado.
    """

    global gemini_model

    try:
        with open(CONFIG_FILE_PATH, "r") as f:
            gemini_model = f.read().strip()
    except FileNotFoundError:
        gemini_model = DEFAULT_MODEL
        with open(CONFIG_FILE_PATH, "w") as f:
            f.write(gemini_model)

    return gemini_model

def gemini_model_user():
    """
    Devuelve el nombre del modelo actualmente en uso.

    Returns:
        El nombre del modelo.
    """

    global gemini_model
    return gemini_model