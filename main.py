from ollama import chat

# Current chat
# - Ask a question and get the response
# Current conversation
# - All the session's questions and responses


class CurrentChat:
    def __init__(self, prompt: str = "", response: list = []):
        self.prompt = prompt
        self.response = response

    def set_prompt(self, new_prompt: str):
        self.prompt = new_prompt

    def set_response(self, chunk):
        self.response.append(chunk)

    def save_chat(self):
        file_name = self.prompt.lower().replace(" ", "_")
        full_response_content = "".join(chunk for chunk in self.response)

        with open(f"./chats/{file_name}.md", "w") as new_chat:
            new_chat.write(full_response_content)


current_chat = CurrentChat()


def ollama_chat(message: str):
    stream = chat(
        model="llama3.1",
        messages=[{"role": "user", "content": message}],
        stream=True,
    )
    for chunk in stream:
        print(chunk.message.content, end="", flush=True)
        current_chat.set_response(chunk.message.content)
        if chunk.done:
            print("\n")


def main():
    print("Exit with command /exit")
    print("Save chat /save")
    while True:
        message = input(">>> Send a message: ").strip()
        if message == "/exit":
            return False
        if message == "/save":
            current_chat.save_chat()

        if not message == "/save":
            current_chat.set_prompt(message.strip())
            ollama_chat(message)


main()
