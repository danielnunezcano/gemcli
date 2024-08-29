from . import WriteAuxFile

def create_question(user_input, question_file_path):
    with open(question_file_path, "w", encoding="utf-8") as question_file:
        while True:
            if not user_input:  # Verifica si la entrada está vacía
                user_input = input()

            if user_input.lower() in (":q", ":e"):  # Maneja comandos en minúsculas
                break

            question_file.write(user_input + "\n")
            user_input = ""  # Reinicia la entrada para la siguiente iteración

    if user_input.lower() == ":e":
        user_input = WriteAuxFile.write_and_read_aux_file(question_file_path)

    return user_input  # Devuelve la última entrada del usuario (puede ser útil)
