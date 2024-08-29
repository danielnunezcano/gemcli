from .client import GeminiCustom as Gemini
from .client import Voice
from .service import ProcessInteraction
import os
import sys

checkVoice = False

def init():
    clear_screen()
    print("Utilizando "+Gemini.set_init_gemini_model())
    conversation_filename = get_conversation_filename()
    while True:
        if not process_interaction(conversation_filename):
            break 

def handle_interrupt(signal, frame):
    """Handles Ctrl+C interrupt."""
    print("\nCtrl+C pressed! Exiting...")
    clear_screen()
    sys.exit(0)  

def get_conversation_filename():
    """Gets conversation filename from arguments."""
    if len(sys.argv) < 1:
        print("No arguments provided.")
        sys.exit(1)
    if len(sys.argv) > 1:
        res = "/home/danielnezcano/.gemcli-py/conversations/" + sys.argv[1]
    if len(sys.argv) > 2:
        set_options(sys.argv[2])
    if len(sys.argv) > 3:
        set_options(sys.argv[3])
    return res

def set_options(argument):
    global checkVoice
    if argument == "-v":
        checkVoice = True
    elif argument == "-m":
        Gemini.set_gemini_model()

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
    print("Utilizando "+Gemini.gemini_model_user())
    print("-------HUMAN----------")
    print(processed_input)

    response = Gemini.question(processed_input, conversation)

    with open(conversation, "a+", encoding="utf-8") as conversation_file:
        conversation_file.write("-------HUMAN----------\n")
        conversation_file.write(processed_input + "\n")
        conversation_file.write("-------GEMINI----------\n")
        conversation_file.write(response + "\n")
    print("-------GEMINI----------")
    print(response)
    print("---------------------\n")
    if checkVoice == True:
        Voice.speak(response)

    return True
