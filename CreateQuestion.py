def createQuestion(linea, theme):
    with open(theme, "w", encoding="utf-8") as questionFile:
        while True:
            if linea == "":
                linea = input()
            if linea == ":q" or linea == ":e":
                break
            questionFile.write(linea + "\n")
            linea = ""    
