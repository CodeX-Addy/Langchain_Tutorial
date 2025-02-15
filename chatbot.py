import json
import requests
import gradio as gr
from gradio import Textbox, Interface

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json',
}

## Maintains history
conversation_history = []

def generate_response(prompt):
    conversation_history.append(prompt)
    full_prompt = "\n".join(conversation_history)

    data = {
        "model": "gemma:7b-instruct-q2_K",
        "stream": False,
        "prompt": full_prompt,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        conversation_history.append(actual_response)
        return actual_response
    else:
        print("Error:", response.status_code, response.text)
        return None

## Gradio interface
face = Interface(
    fn=generate_response,
    inputs=Textbox(
        lines=2, placeholder="Enter your prompt here...", show_label=False),
    outputs="text",
    title="Gemma-7b",
    description="Write a message!",
)

face.launch()
