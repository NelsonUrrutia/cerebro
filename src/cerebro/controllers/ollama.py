from ollama import chat


def ollama_chat(prompt: str):

    chunks = []

    stream = chat(
        model="llama3.1",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )

    for chunk in stream:
        print(chunk.message.content, end="", flush=True)
        chunks.append(chunk.message.content)
        if chunk.done:
            print("\n")

    return chunks
