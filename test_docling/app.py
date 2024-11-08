import gradio as gr
import os
from test_docling.utils import convert_document
import time

def extract_info(file):
    # Start timing the process
    start_time = time.time()
    
    # Convert the document and extract information
    result = convert_document(file.name)
    
    # Calculate the time spent
    time_spent = time.time() - start_time
    
    # Determine the output filename
    base_name = os.path.splitext(os.path.basename(file.name))[0]
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_filename = os.path.join(output_dir, f"{base_name}.md")
    
    # Save the result to a file
    with open(output_filename, 'w') as f:
        f.write(result)
    
    # Print a preview of the result to the CLI
    print("Preview of the result:")
    print(result[:500])  # Print the first 500 characters as a preview
    
    # Return the time spent and the result separately
    return f"Time spent: {time_spent:.2f} seconds", result

iface = gr.Interface(
    fn=extract_info,
    inputs=gr.File(label="Upload Document"),
    outputs=[gr.Textbox(label="Time Spent"), gr.Textbox(label="Document Content")],
    title="Document Information Extractor"
)

if __name__ == "__main__":
    iface.launch()
