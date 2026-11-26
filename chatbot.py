import gradio as gr
import requests

def chat(message, history):

    url = "http://localhost:11434/api/chat"

    # Convert Gradio history into Ollama message format
    messages = []

    for item in history:
        messages.append({
            "role": item["role"],
            "content": item["content"]
        })

    # Add current user message
    messages.append({
        "role": "user",
        "content": message
    })

    response = requests.post(
        url,
        json={
            "model": "llama3.2:1b",
            "messages": messages,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()

    result = response.json()

    return result["message"]["content"]


demo = gr.ChatInterface(
    fn=chat,
    title="Llama 3.2 Chatbot",
    description="Chat with your local Ollama LLM"
)

if __name__ == "__main__":
    demo.launch()


demo.launch()