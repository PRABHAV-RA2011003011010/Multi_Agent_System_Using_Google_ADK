import os
from dotenv import load_dotenv
import gradio as gr
from huggingface_hub import InferenceClient

# Load token
load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

client = InferenceClient(token=HF_TOKEN)
llm = "meta-llama/Llama-3.1-8B-Instruct"


def chatbot_response(message, history):
    """
    message = current user message (string)
    history = list of dicts: [{"role": "...", "content": "..."}]
    """

    if history is None:
        history = []

    # Add user message
    history.append({"role": "user", "content": message})

    # Send chat history to model
    completion = client.chat.completions.create(
        model=llm,
        messages=history
    )

    bot_reply = completion.choices[0].message["content"]

    # Add assistant reply
    history.append({"role": "assistant", "content": bot_reply})

    return "", history


with gr.Blocks() as demo:
    gr.Markdown("## 🦙 LLaMA Chatbot (Gradio 6 + HF InferenceClient)")

    chatbot = gr.Chatbot()   # In Gradio 6 this uses dict-based message history
    user_input = gr.Textbox(placeholder="Type your message…", label="Your Message")
    send = gr.Button("Send")

    send.click(
        chatbot_response,
        inputs=[user_input, chatbot],
        outputs=[user_input, chatbot]
    )

demo.launch(share=True)
