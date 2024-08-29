import pyttsx3

def speak(text, voice_id=21):
    """
    Convierte texto a voz utilizando pyttsx3.

    Args:
        text: El texto que se desea convertir a voz.
        voice_id: El índice de la voz a utilizar (opcional, por defecto es 21).
    """

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Verifica si el índice de voz es válido
    if 0 <= voice_id < len(voices):
        engine.setProperty("voice", voices[voice_id].id)
    else:
        print(f"Advertencia: Índice de voz inválido ({voice_id}). Usando la voz predeterminada.")

    engine.say(text)
    engine.runAndWait()