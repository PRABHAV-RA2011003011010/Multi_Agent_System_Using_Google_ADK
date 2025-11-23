import gradio as gr

# Simple chatbot logic
def chatbot_response(user_input, chat_history):
    if chat_history is None:
        chat_history = []
    
    # Example response logic (replace with your AI model)
    response = f"You said: {user_input}"
    
    # Append to chat history
    chat_history.append((user_input, response))
    return chat_history, ""

# Define Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## Chatbot UI Example")
    
    chatbot = gr.Chatbot()
    user_input = gr.Textbox(
        label="Type your message here",
        placeholder="Enter message...",
        lines=1
    )
    send_btn = gr.Button("Send")
    
    # Connect components
    send_btn.click(chatbot_response, inputs=[user_input, chatbot], outputs=[chatbot, user_input])
    
demo.launch()
