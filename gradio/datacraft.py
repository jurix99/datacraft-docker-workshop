# Import the Gradio library for creating web interfaces
import gradio as gr

# Import the 'outbreak' function from the 'utils.outbreak' module
from utils.outbreak import outbreak

# Define the inputs for the Gradio interface
inputs = [
    # Dropdown to select the type of plot
    gr.Dropdown(["Matplotlib", "Plotly", "Altair"], label="Plot Type"),
    # Slider to select the value of R (Reproduction Number)
    gr.Slider(1, 4, 3.2, label="R"),
    # Dropdown to select the month
    gr.Dropdown(["January", "February", "March", "April", "May"], label="Month"),
    # Checkbox group to select one or multiple countries
    gr.CheckboxGroup(
        ["USA", "Canada", "Mexico", "UK"], label="Countries", value=["USA", "Canada"]
    ),
    # Checkbox to indicate whether social distancing is applied
    gr.Checkbox(label="Social Distancing?"),
]
# Define the output as a plot
outputs = gr.Plot()
# Create the Gradio Interface
demo = gr.Interface(
    # Title of the web interface
    title="DATACRAFT x EKIMETRICS x Gradio",
    # Description of the web interface
    description="Here's a sample outbreak forecasting app",
    # The function to be called when the interface is used
    fn=outbreak,
    # List of inputs
    inputs=inputs,
    # List of outputs
    outputs=outputs,
    # Sample examples to be displayed
    examples=[
        ["Matplotlib", 2, "March", ["Mexico", "UK"], True],
        ["Altair", 2, "March", ["Mexico", "Canada"], True],
        ["Plotly", 3.6, "February", ["Canada", "Mexico", "UK"], False],
    ],
    # Cache examples for better performance
    cache_examples=True,
)
# Check if this script is the main program and then launch the web interface
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8080)