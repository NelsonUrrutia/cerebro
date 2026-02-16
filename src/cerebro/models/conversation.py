class Conversation:
    def __init__(self):
        self.context = []
        # TODO: move to Documents folder
        self.conversations_folder = "./src/cerebro/md_chats"

    def add_context(self, dialog: dict):
        """
        Adds new dialog into the conversation context
        Args:
            dialog (dict): Dict with prompt and response
        """
        self.context.append(dialog)

    def clear_context(self):
        """Clears context to start a new conversation"""
        self.context = []

    def save_conversation(self, title: str):
        """Saves the conversation"""

        file_name = title.strip().lower().replace(" ", "_").replace("|","")
        with open(
            f"{self.conversations_folder}/{file_name}.md", "w"
        ) as file_conversation:
            file_conversation.write(f"# {title}\n")
            for dialog in self.context:
                file_conversation.write(f"\n>>>{dialog.get("prompt")}\n")
                file_conversation.write(f"\n{dialog.get("response")}\n")
