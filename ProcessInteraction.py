import ResponseQuestion
import CreateQuestion
import os

def processUserInput(linea):
    question = "question"
    CreateQuestion.createQuestion(linea, question)
    response = ResponseQuestion.responseQuestion(question, linea)       
    os.remove(question)
    return response
