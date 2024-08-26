import GeminiCustom as Gemini
import ProcessInteraction
import os
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        conversation = "conversations/"+sys.argv[1]
    else:
        print("No se proporcionaron argumentos.")

os.system('cls' if os.name == 'nt' else 'clear') 
while True:
    linea = input()
    if linea == ":exit":
        break
    contenido = ProcessInteraction.processUserInput(linea)
    os.system('cls' if os.name == 'nt' else 'clear') 
    print("-------HUMANO----------")
    print(contenido)
    response = Gemini.question(contenido, conversation)
    with open(conversation, "a+", encoding="utf-8") as conversationFile:
        pass
        conversationFile.write("-------HUMANO----------" + "\n")
        conversationFile.write(contenido + "\n")
        conversationFile.write("-------GEMINI----------" + "\n")
        conversationFile.write(response + "\n")
        print("-------GEMINI----------")
        print(response)
        print("---------------------\n")
