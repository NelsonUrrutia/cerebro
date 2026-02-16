Here's an example of a basic chat app UI created using the `textual` library in Python:

**chat_app.py**
```python
import textual as t
from textual import events
from textual.app import Compositor

class ChatApp(t.App):
    CSS = """
    Screen {
        align: center;
        vertical-align: middle;
    }
    
    .chat-log {
        background-color: #f0f0f0;
        padding: 10px;
        border-radius: 10px;
    }
    
    .message {
        background-color: #ffffff;
        padding: 5px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    
    .input-field {
        width: 100%;
        padding: 5px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }
    """

    def on_mount(self) -> None:
        self.compose(
            Compositor(self),
            t.Header("Chat App"),
            t.Div(
                classes=("chat-log",),
                children=[
                    t.Label("", id="chat-log", style={"color": "black"}),
                ],
            ),
            t.Input(
                placeholder="Type a message...",
                classes=("input-field",),
                on_submit=self.on_message_submit,
                id="message-input",
            ),
        )

    def on_message_submit(self, event: t.events.Input) -> None:
        message = event.input
        self.query_one("#chat-log").update(f"User: {message}\n")

def main():
    app = ChatApp()
    return app

if __name__ == "__main__":
    app = main()
    app.run()
```
This code creates a basic chat app UI with the following features:

1. A header at the top of the screen with the text "Chat App".
2. A log area below the header where messages are displayed.
3. An input field at the bottom of the screen where users can type their messages.

When a user submits a message, it is added to the chat log with the username "User".

To run this code, save it as `chat_app.py` and execute it using Python (e.g., `python chat_app.py`). This will launch the chat app UI in your terminal or command prompt.