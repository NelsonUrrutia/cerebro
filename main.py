from ollama import chat
from ollama import ChatResponse

stream= chat(model='llama3.1', messages=[{
    'role':'user',
    'content':'Why do I need to use venv in python?'
}], stream = True)

# print(response['message']['content'])
for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)


stream= chat(model='llama3.1', messages=[{
    'role':'user',
    'content':'How to run a Python project without activating venv, for example running a cli tool? '
}], stream = True)

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
