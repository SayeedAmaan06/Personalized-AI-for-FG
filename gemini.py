import google.generativeai as genai

genai.configure(api_key='AIzaSyBp6VuWQ74zgTrVjNRzGjLxkDOzUiVrtiI')

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

def finance(userinput):
    response = chat.send_message(
        userinput)    
    return response.text
       