import gradio as gr
from agent.graph import graph
import sys
import os

# ensure project root is visible
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def ask(question):

    result = graph.invoke({
        "question": question,
        "result": ""
    })

    response = result["result"]

    # check if response contains image path
    if isinstance(response, dict) and "image" in response:
        return response["text"], response["image"]

    return response, None


with gr.Blocks(title="VoltAI") as demo:

    

    # Title
    gr.Markdown("## VoltAI — Electronics Engineering Copilot")

    with gr.Row():

        with gr.Column():
            question = gr.Textbox(
                label="Ask an ECE Question",
                placeholder="Whats Tickling Your Brain Cells Today!!!"
            )

            ask_btn = gr.Button("Ask VoltAI")

        with gr.Column():
            answer = gr.Textbox(label="VoltAI Response")
            plot = gr.Image(label="Generated Plot", visible=True)

    ask_btn.click(
        fn=ask,
        inputs=question,
        outputs=[answer, plot]
    )


demo.launch()