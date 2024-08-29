from . import WriteAuxFile

def get_response(question_file_path, user_input):
    if user_input.lower() == ":e":  # Manejo de comandos en minúsculas
        response = WriteAuxFile.write_and_read_aux_file(question_file_path)
    else:
        with open(question_file_path, "r", encoding="utf-8") as question_file:
            response = question_file.read()

    return response