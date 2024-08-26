import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-pro')
sizeFileMax = 2000000

def question(questionText, conversation):
    if os.path.exists(conversation):
        with open(conversation, "r", encoding="utf-8") as conversationFile:
            conver = conversationFile.read()
        if os.path.getsize(conversation) > sizeFileMax:
            resumeToGemini = "Hazme un resumen de lo siguiente: " + conver
            resume = model.generate_content(resumeToGemini)
            with open(conversation, "w", encoding="utf-8") as conversationFile:
                conversationFile.write("-------GEMINI----------" + "\n")
                conversationFile.write(resume.text + "\n")
        questionToGemini = "Esto es lo que me dijiste: " + conver + "te comento lo siguiente: " + questionText
    else:
        questionToGemini = questionText
    response = model.generate_content(questionToGemini)
    return response.text

def resume(conversation):
    if os.path.exists(conversation):
        with open(conversation, "r", encoding="utf-8") as conversationFile:
            conver = conversationFile.read()
        questionToGemini = "Resumeme lo siguiente: " + conver
    response = model.generate_content(questionToGemini)
    return response.text

