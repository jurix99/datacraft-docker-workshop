import gradio as gr
from utils.outbreak import outbreak

inputs = [
    gr.Dropdown(["Matplotlib", "Plotly", "Altair"], label="Plot Type"),
    gr.Slider(1, 4, 3.2, label="R"),
    gr.Dropdown(["January", "February", "March", "April", "May"], label="Month"),
    gr.CheckboxGroup(
        ["USA", "Canada", "Mexico", "UK"], label="Countries", value=["USA", "Canada"]
    ),
    gr.Checkbox(label="Social Distancing?"),
]
outputs = gr.Plot()

demo = gr.Interface(
    title="DATACRAFT x EKIMETRICS",
    description="Here's a sample outbreak forecasting app",
    fn=outbreak,
    inputs=inputs,
    outputs=outputs,
    examples=[
        ["Matplotlib", 2, "March", ["Mexico", "UK"], True],
        ["Altair", 2, "March", ["Mexico", "Canada"], True],
        ["Plotly", 3.6, "February", ["Canada", "Mexico", "UK"], False],
    ],
    cache_examples=True,
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8080)