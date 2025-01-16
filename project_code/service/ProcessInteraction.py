from project_code.client import ResponseQuestion
from project_code.client import CreateQuestion
import os

def process_user_input(user_input, conversation_file_path):
    question_file_path = conversation_file_path + "Question"
    CreateQuestion.create_question(user_input, question_file_path)
    response = ResponseQuestion.get_response(question_file_path, user_input)
    os.remove(question_file_path)  # Limpia el archivo temporal
    return response