import WriteAuxFile

def responseQuestion(question, linea):
    
    if linea == ":e":
        response = WriteAuxFile.writeAndReadAuxFile(question)
    else:
        with open(question, "r", encoding="utf-8") as questionFile:
            response = questionFile.read()  
    return response
