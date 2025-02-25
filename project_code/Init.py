import re
from .client import GeminiCustom as Gemini
from .client import Voice
from .service import ProcessInteraction
import os
import sys
from InquirerPy import inquirer


checkVoice = False
actual_conversation = ""

def init():
    clear_screen()
    conversation_filename = get_conversation_filename()
    clear_screen()
    print(f"Conversación: {actual_conversation}")
    while True:
        if not process_interaction(conversation_filename):
            break

def conversation_list():
    folder = "/home/daniel/.gemcli-py/conversations"
    files_menu = ["<Crear nueva conversación>"]
    global actual_conversation
    try:
        files = os.listdir(folder)
        for file in files:
            files_menu.append(file)
    except FileNotFoundError:
        print("Carpeta no encontrada.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    actual_conversation = inquirer.select(
        message="Elige una conversación:",
        choices=files_menu,
        pointer="➤",  # Marcador personalizado
    ).execute()

    if(actual_conversation=="<Crear nueva conversación>"):
        print("Elige nombre para la conversación: ")
        actual_conversation = input()
    return actual_conversation

def handle_interrupt(signal, frame):
    """Handles Ctrl+C interrupt."""
    print("\nCtrl+C pressed! Exiting...")
    clear_screen()
    sys.exit(0)  

def get_conversation_filename():
    """Gets conversation filename from arguments."""
    if len(sys.argv) <= 1:
        res = "/home/daniel/.gemcli-py/conversations/" + conversation_list()
    if len(sys.argv) > 1:
        set_options(sys.argv[2])
    return res

def set_options(argument):
    global checkVoice
    if argument == "-v":
        checkVoice = True

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def process_interaction(conversation):
    """Processes user input and gets a response from Gemini."""
    user_input = input()
    if user_input == ":exit":
        return False

    processed_input = ProcessInteraction.process_user_input(user_input, conversation)
    clear_screen()
    print(f"Conversación: {actual_conversation}")
    print("-------HUMAN----------")
    print(processed_input)

    response = Gemini.question(processed_input, conversation)
    with open(conversation, "a+", encoding="utf-8") as conversation_file:
        conversation_file.write("-------HUMAN----------\n")
        conversation_file.write(processed_input + "\n")
        conversation_file.write("-------GEMINI----------\n")
        conversation_file.write(response + "\n")
    print("-------GEMINI----------")
    print(text_style(response))
    print("---------------------\n")
    if checkVoice == True:
        Voice.speak(response)

    return True

def text_style(text):
    return text_style_list(text_style_code(text_style_bold(text)))

def text_style_bold(text):
    regex_bold_gemini=r"\*\*(.+?)\*\*"
    regex_bold_print=r"\033[1;32m\1\033[0m"
    return re.sub(regex_bold_gemini,regex_bold_print,text)

def text_style_code(text):
    regex_cursive_gemini = r"```(.*?)```"
    regex_cursive_print = r"-----code------\n\033[3;37m\1\033[0m---------------"
    return re.sub(regex_cursive_gemini, regex_cursive_print, text, flags=re.S)

def text_style_list(text):
    return text.replace("* ","  \u2022 ")

