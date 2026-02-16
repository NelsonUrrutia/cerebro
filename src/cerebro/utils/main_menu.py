from cerebro.controllers.conversation import new_conversation


def main_menu():
    while True:
        print("================")
        print("CEREBRO COMMANDS")
        print("================\n")
        print("/new => Creates a new convesation")
        print("/documents => Shows saved documents")
        print("/exit => Exits Cerebro")

        command = input("\n>>> Run a command:").strip()

        if command == "/exit":
            return False
        if command == "/new":
            new_conversation()
        if command == "/documents":
            print("Clear terminal")
            print("Show documents modal")
