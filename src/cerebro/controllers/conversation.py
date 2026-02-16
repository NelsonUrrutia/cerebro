from cerebro.controllers.ollama import ollama_chat
from cerebro.models.conversation import Conversation

conversation = Conversation()


def new_conversation():
    print("\nConversation commands")
    print("/save => Saves conversation")
    print("/end => Ends the conversation")
    print("/help => Shows available commands")
    print("\n")

    while True:
        prompt = input(">>> Send a prompt: ").strip()

        match prompt:
            case "/end":
                print("exit conversation")
                return False
            case "/save":
                save_conversation()
                return False
            case "/help":
                print("/save => Saves conversation")
                print("/end => Ends the conversation")
            case _:
                prompt_to_ollama(prompt)


def prompt_to_ollama(prompt: str):
    chunks = ollama_chat(prompt)

    dialog = {
        "prompt":prompt,
        "response": "".join(chunks)
    }

    conversation.add_context(dialog)

def save_conversation():
    title = input("\n>>Set a title to the conversation: ").strip()
    conversation.save_conversation(title)
