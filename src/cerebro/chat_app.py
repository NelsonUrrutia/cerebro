from ollama import chat
from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Header, Input, Label


class ChatApp(App):
    CSS = """
        #main_prompt_input{
            dock: bottom;
            width: 100%;
            height: 3;
            margin-bottom: 1
        }

        #message_log{
            color: white;
            background: #333;
            width: 100%;
            padding: 1;
            margin: 1;
        }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Input(placeholder=">>> Send a message", id="main_prompt_input")
        yield VerticalScroll(Label(id="message_log"))
        yield VerticalScroll(Label(id="chat_response"))

    def on_input_submitted(self, event: Input.Submitted) -> None:
        submitted_text = event.value
        input_widget = self.query_one("#main_prompt_input", Input)
        message_log = self.query_one("#message_log", Label)

        new_message = Label(f"{submitted_text}")
        message_log.mount(new_message)
        input_widget.clear()

        self.llama_chat(submitted_text)

    def llama_chat(self, message: str) -> None:
        stream = chat(
            model="llama3.1",
            messages=[{"role": "user", "content": message}],
            stream=True,
        )
        for chunk in stream:
            label = self.query_one("#chat_response", Label)
            response = Label(f"{chunk.message.content}")
            label.mount(response)


app = ChatApp()
app.run()
