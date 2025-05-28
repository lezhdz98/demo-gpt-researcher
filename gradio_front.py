import gradio as gr
import requests

def generate_report(query, report_type):
    try:
        response = requests.get(
            f"http://localhost:8000/report/{report_type}",
            params={"query": query}
        )
        data = response.json()
        report = data.get("report", "No report generated.")
        sources = "\n".join(f"- {url}" for url in data.get("source_urls", []))
        costs = data.get("research_costs", {})
        return report, sources, str(costs)
    except Exception as e:
        return f"Error: {str(e)}", "", ""

with gr.Blocks(title="🧠 GPT Researcher Demo") as demo:
    gr.Markdown("## 🧠 GPT Researcher\nEnter a query and choose a report type.")
    
    with gr.Row():
        with gr.Column(scale=1):  # Empty column to help centering
            pass
        with gr.Column(scale=2):  # Main content in center column
            query = gr.Textbox(label="Query", placeholder="e.g. AI in healthcare")
            report_type = gr.Dropdown(["research_summary", "detailed_report"], label="Report Type")
            submit_btn = gr.Button("Generate Report")

            report_output = gr.Textbox(label="Generated Report")
            sources_output = gr.Textbox(label="Source URLs", lines=5)
            costs_output = gr.Textbox(label="Research Costs")

        with gr.Column(scale=1):  # Empty column on right
            pass

    submit_btn.click(
        generate_report,
        inputs=[query, report_type],
        outputs=[report_output, sources_output, costs_output]
    )

if __name__ == "__main__":
    demo.launch()

