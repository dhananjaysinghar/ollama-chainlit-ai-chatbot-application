import chainlit as cl
import requests
import json

chat_history = [{"role": "system", "content": "You are a helpful assistant."}]

@cl.on_message
async def handle_message(message: cl.Message):
    chat_history.append({"role": "user", "content": message.content})
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3.2",  # use "llama3" if needed
            "messages": chat_history,
            "stream": True
        },
        stream=True
    )

    answer = ""
    async_msg = cl.Message(content="")
    await async_msg.send()

    for line in response.iter_lines():
        if line:
            data = line.decode("utf-8")
            chunk = json.loads(data)
            token = chunk.get("message", {}).get("content", "")
            answer += token
            await async_msg.stream_token(token)

    chat_history.append({"role": "assistant", "content": answer})
    await async_msg.update()
