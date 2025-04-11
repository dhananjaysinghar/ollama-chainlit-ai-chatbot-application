import chainlit as cl
import requests
import json

chat_history = [{"role": "system", "content": "You are a helpful assistant."}]

def send_api_request(model, messages):
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": model,
            "messages": messages,
            "stream": True
        },
        stream=True
    )
    return response

async def process_response(response):
    answer = ""
    async_msg = cl.Message(content="")
    await async_msg.send()
    for line in response.iter_lines():
        if line:
            try:
                chunk = json.loads(line.decode("utf-8"))
                token = chunk.get("message", {}).get("content", "")
                answer += token
                await async_msg.stream_token(token)
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Invalid data: {e}")
                await async_msg.update(content="Invalid data")
    chat_history.append({"role": "assistant", "content": answer})
    await async_msg.update()

@cl.on_message
async def handle_message(message: cl.Message):
    chat_history.append({"role": "user", "content": message.content})

    response = send_api_request("llama3.2", chat_history)
    await process_response(response)


# chainlit run /Users/dhananjayasamantasinghar/Desktop/test-python/src/test/test_pyspark/chatbot.py
